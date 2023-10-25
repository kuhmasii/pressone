from django.urls import path

from items import views


app_name = 'items'

urlpatterns = [
    path("create/", views.item_api, name="item-create"),
    path("<int:item_id>/", views.item_api, name="item-detail"),
    
    # url route for generic
    path("generic/create/", views.item_create, name='item-generic-create'),
    path("generic/<int:id>/", views.item_retrieve, name='item-generic-detail')
]