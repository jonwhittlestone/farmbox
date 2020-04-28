import os
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from sheets.reader import collect_files_for_reading, OrderSheet as OrderSheetReader

def fetch(request):
    # collect_files
    files = collect_files_for_reading(os.path.join(settings.PROJECT_DIR,'order'))
    # foreach file:
    r = OrderSheetReader()
    r.read_to_model(files[0])

    # extract order details
    messages.add_message(request,
                         messages.INFO, 'X orders fetched and processed. Y have been added to Fulfillment Event DD/MM/YYYY')
    return redirect(f'/admin/order/fulfillmentevent/')
    

