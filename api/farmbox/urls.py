from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from order import api as order_api
from sheets.views import fetch as order_sheet_fetcher
from tutorial.views import list_files, download_files, sign_in, callback, sign_out

admin.site.site_header = 'Village Greens'
admin.site.site_title = 'Village Greens Admin'
admin.site.index_title = 'Village Greens Admin'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path(r'api/order/input-sheet/<int:f_event_id>/',
        login_required(order_api.download_input_xlsx), name='download_input_xlsx'),
    path(r'sheets/fetch/', login_required(order_sheet_fetcher), name='order_sheet_fetcher'),
    path('drive/list-files', login_required(list_files), name='drive_list'),
    path('drive/download-files', login_required(download_files), name='drive_download'),
    path('signin', sign_in, name='signin'),
    path('signout', sign_in, name='signout'),
    path('callback', callback, name="callback"),
    path('', admin.site.urls),
]
