import os
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from sheets.reader import collect_files_for_reading, OrderSheet as OrderSheetReader
from  order.models import OrderFormFailure
from order.exceptions import OrderFormReaderException

def fetch(request):
    # collect_files
    files = collect_files_for_reading(os.path.join(settings.PROJECT_DIR,'order'))
    # foreach file:
    r = OrderSheetReader()
    try:
        order = r.read_to_model(files[0])
        messages.add_message(request,
                            messages.SUCCESS, 'Orders fetched and processed.')
        return redirect(f'/admin/order/fulfillmentevent/')
    except OrderFormReaderException as e:
        # f = files[0]
        OrderFormFailure.objects.create(reason=e, form=r.obj)
        messages.add_message(request,
                            messages.ERROR, '0 orders fetched and processed. 1 Failure(s). Please check reason and try again.')
        return redirect(f'/admin/order/orderformfailure/')
