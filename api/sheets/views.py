from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def fetch(request):
    # collect_files

    # foreach file:

    # insert orderform record

    # extract order details
    messages.add_message(request,
                         messages.INFO, 'X orders fetched and processed. Y have been added to Fulfillment Event DD/MM/YYYY')
    return redirect('/admin/order/fulfillmentevent/?id=2')
    

