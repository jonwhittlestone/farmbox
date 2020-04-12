from django.http import JsonResponse
from order.models import Order, FulfillmentEvent

def input_sheet_header_column() -> dict:
    headers = {
        'Name',
        'Address',
        'Email'
    }
    return headers

def build_input_dataframe(f_event_id):
    df = False
    return df

def download_input_xlsx(request, f_event_id):
    df = build_input_dataframe(f_event_id)
    return JsonResponse({'sanity':'check', 'event_id': f_event_id})