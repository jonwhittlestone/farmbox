from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

admin.site.site_header = 'Village Greens'
admin.site.site_title = 'Village Greens Admin'
admin.site.index_title = 'Village Greens Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True)))
]
