from django import template
from order.models import FulfillmentEvent
from django.urls import reverse

register = template.Library()

def newest_event():
    '''Helper function to get forthcoming f_event & its link'''
    url = None
    f_event = FulfillmentEvent.newest_event()
    if f_event:
        url = reverse('admin:order_order_changelist')
        url = f'{url}?fulfillment_event__id__exact={f_event.id}'

    return {
        'f_event': f_event,
        'order_changelist_filtered_url': url
    }


@register.inclusion_tag('admin/event_orders_header.html', takes_context=True)
def event_orders_header(context):
    return {
        'newest_event': newest_event()
    }
