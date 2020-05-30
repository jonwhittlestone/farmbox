import os
import shutil
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.conf import settings
from sheets.reader import collect_files_for_reading, OrderSheet as OrderSheetReader
from  order.models import OrderFormFailure, OrderForm
from order.exceptions import OrderFormReaderException
from cloudstore.models import cloud_fetcher, remove_remote_form_after_fetch_success, upload_form_to_processed_folder

def local_fetch(request):
    '''Used in debugging'''
    forms_status = {
        'processed': 0,
        'failure': 0
    }
    for count, f in enumerate(collect_files_for_reading(settings.LOCAL_FETCH_SHEETS_DIR)):
        r = OrderSheetReader()
        try:
            order = r.read_to_model(f)
            remove_remote_form_after_fetch_success(r.obj.filename)
            upload_form_to_processed_folder(f,order)
            forms_status['processed'] += 1
            messages.add_message(request,
                            messages.SUCCESS, f'{r.obj.filename} processed.')
        except OrderFormReaderException as e:
            OrderFormFailure.objects.create(reason=e, form=r.obj)
            forms_status['failure'] += 1
            messages.add_message(request,
                            messages.WARNING, f'{r.obj.filename} failure.')
            continue
    url = reverse('admin:order_orderformfailure_changelist')
    return redirect(url)


def fetch(request):
    forms_status = {
        'processed': 0,
        'failure': 0
    }
    containing_dir, zip_path, files_meta = cloud_fetcher()
    for count, f in enumerate(collect_files_for_reading(containing_dir)):
        r = OrderSheetReader()
        try:
            order = r.read_to_model(f)
            remove_remote_form_after_fetch_success(r.obj.filename)
            upload_form_to_processed_folder(f,order)
            forms_status['processed'] += 1

        except OrderFormReaderException as e:
            OrderFormFailure.objects.create(reason=e, form=r.obj)
            forms_status['failure'] += 1
            continue

    # SCENARIOS
    #   'No new-orders found in Dropbox
    #       - orders_processed ==  0 and order_failures == 0
    #   'Orders fetched and processed'
    #       - orders_processed > 0 and order_failures == 0
    #   'Some orders processed but also some failures. Please check "Order Form Failures" or persisting files in 'new-orders' folder
    #       - orders_processed > 0 and order_failures > 0
    #   'There were Order form failures. Please see below'
    #       - orders_processed == 0 and orders_failures > 0

    if forms_status['processed'] == 0 and forms_status['failure'] == 0:
        os.remove(zip_path)
        shutil.rmtree(containing_dir)
        messages.add_message(request,
                        messages.WARNING, 'No new-orders found in Dropbox')
        return redirect(f'/admin/order/fulfillmentevent/')

    if forms_status['processed'] > 0 and forms_status['failure'] == 0:
        os.remove(zip_path)
        extracted_dir = os.path.join(settings.MEDIA_ROOT,settings.NEW_ORDERS_FOLDER)
        shutil.rmtree(extracted_dir)
        messages.add_message(request,
                            messages.SUCCESS, 'Orders fetched and processed')
        return redirect(f'/admin/order/fulfillmentevent/')

    if forms_status['processed'] > 0 and forms_status['failure'] > 0:
        os.remove(zip_path)
        extracted_dir = os.path.join(settings.MEDIA_ROOT,settings.NEW_ORDERS_FOLDER)
        shutil.rmtree(extracted_dir)
        messages.add_message(request,
                            messages.WARNING, 'Some orders processed but also some failures. Please check below. The failed files will persist in the "new-orders" folder')
        return redirect(f'/admin/order/orderformfailure/')

    os.remove(zip_path)
    extracted_dir = os.path.join(settings.MEDIA_ROOT,settings.NEW_ORDERS_FOLDER)
    shutil.rmtree(extracted_dir)
    messages.add_message(request,
                        messages.WARNING, 'There were Order form failures. Please see below. The failed files will persist in the "new-orders" Dropbox folder')
    return redirect(f'/admin/order/orderformfailure/')
