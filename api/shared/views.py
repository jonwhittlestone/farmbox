from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render, redirect
from shared.environments import FactoryReset

def factory_reset(request):
    try:
        FactoryReset().run()
        messages.add_message(request,
            messages.SUCCESS, 'Orders, Products, Fulfillment Events have been reset')
    except Exception as e:
        print(e)
        messages.add_message(request,
            messages.WARNING, 'There was an error performing the factory reset')

    url = reverse('admin:index')
    return redirect(url)
