from django.http import JsonResponse, HttpResponse, FileResponse
from order.models import Order, FulfillmentEvent
from sheets.generate import InputSheet, CustomerSheet, event_customer_sheets, event_customer_sheets_xlsx
import pandas as pd

import pandas as pd
from io import BytesIO as IO
import xlsxwriter

def download_event_customer_sheet_pdf(request, f_event_id):
    '''Create customer sheets for all orders in event, and concatenate'''
    path = event_customer_sheets(f_event_id)
    pdf = open(path, 'rb')
    response = FileResponse(pdf)
    return response

def download_event_customer_sheet_xlsx(request, f_event_id):
    '''Create customer sheets for all orders in event, and concatenate'''
    df = event_customer_sheets_xlsx(f_event_id)
    excel_file = IO()
    xlwriter = pd.ExcelWriter(
        excel_file, engine='xlsxwriter', options={'encoding': 'utf-8'})
    df.to_excel(xlwriter, 'Worksheet 1', index=False)
    xlwriter.save()
    xlwriter.close()

    # rewind buffer otherwise we'll get nothing when read()
    excel_file.seek(0)
    # set mime type so browser knows what to do
    response = HttpResponse(excel_file.read(),
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    # set the file name
    response['Content-Disposition'] = f'attachment; filename=evt-CUSTOMER.xlsx'
    return response

def download_customer_sheet_pdf(request, order_id):
    generator = CustomerSheet(Order.objects.get(id=order_id))
    path = generator.to_pdf()
    pdf = open(path, 'rb')
    response = FileResponse(pdf)
    return response

def download_input_xlsx(request, f_event_id):
    generator = InputSheet()
    df = generator.to_df(f_event_id)
    excel_file = IO()
    xlwriter = pd.ExcelWriter(
        excel_file, engine='xlsxwriter', options={'encoding': 'utf-8'})
    df.to_excel(xlwriter, 'Worksheet 1', index=False)
    xlwriter.save()
    xlwriter.close()

    # rewind buffer otherwise we'll get nothing when read()
    excel_file.seek(0)
    # set mime type so browser knows what to do
    response = HttpResponse(excel_file.read(),
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    # set the file name
    response['Content-Disposition'] = f'attachment; filename=evt-INPUT.xlsx'
    return response
