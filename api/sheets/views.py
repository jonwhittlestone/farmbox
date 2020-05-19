import os
import shutil
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from sheets.reader import collect_files_for_reading, OrderSheet as OrderSheetReader
from  order.models import OrderFormFailure, OrderForm
from order.exceptions import OrderFormReaderException
from cloudstore.models import cloud_fetcher, remove_remote_form_after_fetch_success, upload_form_to_processed_folder

def fetch(request):
    exceptions = 0
    count = 0
    containing_dir, zip_path, files_meta = cloud_fetcher()
    for count, f in enumerate(collect_files_for_reading(containing_dir)):
        r = OrderSheetReader()
        try:
            order = r.read_to_model(f)
            remove_remote_form_after_fetch_success(r.obj.filename)
            upload_form_to_processed_folder(f,order)

        except OrderFormReaderException as e:
            exceptions = exceptions + 1
            OrderFormFailure.objects.create(reason=e, form=r.obj)
            messages.add_message(request,
                                messages.ERROR, f'{count} orders fetched and processed but see failure(s). Please check reason and try again.')
            continue

    if count == 0 and exceptions == 0:
        os.remove(zip_path)
        shutil.rmtree(containing_dir)
        messages.add_message(request,
                        messages.WARNING, 'No new-orders found in Dropbox')
        return redirect(f'/admin/order/fulfillmentevent/')

    if exceptions == 0 and count > 0:
        os.remove(zip_path)
        extracted_dir = os.path.join(settings.MEDIA_ROOT,settings.NEW_ORDERS_FOLDER)
        shutil.rmtree(extracted_dir)
        messages.add_message(request,
                            messages.SUCCESS, 'Orders fetched and processed.')
        return redirect(f'/admin/order/fulfillmentevent/')


    os.remove(zip_path)
    extracted_dir = os.path.join(settings.MEDIA_ROOT,settings.NEW_ORDERS_FOLDER)
    shutil.rmtree(extracted_dir)
    return redirect(f'/admin/order/orderformfailure/')
