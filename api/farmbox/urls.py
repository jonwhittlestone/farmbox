from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from order import api as order_api
from sheets.views import fetch as order_sheet_fetcher
from sheets.views import cloud_product_sheet_fetch, local_product_sheet_fetch
from sheets.views import local_fetch as local_order_sheet_fetcher
from cloudstore.views import dropbox_example, restore_db
from shared.views import factory_reset

admin.site.site_header = "Village Greens"
admin.site.site_title = "Village Greens Admin"
admin.site.index_title = "Village Greens Admin"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path(
        r"api/order/input-sheet/<int:f_event_id>/",
        login_required(order_api.download_input_xlsx),
        name="download_input_xlsx",
    ),
    path(
        r"api/order/customer-sheet-pdf/<int:order_id>/",
        login_required(order_api.download_customer_sheet_pdf),
        name="download_customer_sheet_pdf",
    ),
    path(
        r"api/order/customer-sheet-pdf/fulfillment-event/<int:f_event_id>/",
        login_required(order_api.download_event_customer_sheet_pdf),
        name="download_event_customer_sheet_pdf",
    ),
    path(
        r"api/order/customer-sheet-xlsx/fulfillment-event/<int:f_event_id>/",
        login_required(order_api.download_event_customer_sheet_xlsx),
        name="download_event_customer_sheet_xlsx",
    ),
    path(
        r"sheets/local-fetch/",
        login_required(local_order_sheet_fetcher),
        name="local_order_sheet_fetcher",
    ),
    path(
        r"sheets/fetch/",
        login_required(order_sheet_fetcher),
        name="order_sheet_fetcher",
    ),
    path(
        r"sheets/fetch-products/",
        login_required(cloud_product_sheet_fetch),
        name="cloud_product_sheet_fetcher",
    ),
    path(
        r"sheets/local-fetch-products/",
        login_required(local_product_sheet_fetch),
        name="local_product_sheet_fetcher",
    ),
    path("shared/factory-reset", login_required(factory_reset), name="factory_reset"),
    path("cloudstore/restore-db", login_required(restore_db), name="restore_db"),
    path("dropbox-example", dropbox_example, name="dropbox_example"),
    path("", admin.site.urls),
]
