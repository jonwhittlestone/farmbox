from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from order import api as order_api

admin.site.site_header = 'Village Greens'
admin.site.site_title = 'Village Greens Admin'
admin.site.index_title = 'Village Greens Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path(r'api/order/input-sheet/<int:f_event_id>/',
        login_required(order_api.download_input_xlsx), name='download_input_xlsx'),

    path('', admin.site.urls),
]
