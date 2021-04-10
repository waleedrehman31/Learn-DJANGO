from django.urls import path
from products.views import (
    dynamic_lookup_view,
    product_create_view,
    product_delete_view,
    product_list_view,
    product_update_view
)

app_name = "products"
urlpatterns = [
    path('create/', product_create_view),
    path('<int:id>/update/', product_update_view),
    path('list/', product_list_view, name='product-list'),
    path('<int:id>/', dynamic_lookup_view, name='product-detail'),
    path('<int:id>/delete', product_delete_view, name='product-delete'),
]
