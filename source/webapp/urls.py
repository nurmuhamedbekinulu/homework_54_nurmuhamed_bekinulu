from django.urls import path
from webapp.views.base import index_view
from webapp.views.category import add_category_view, category_detail_view
from webapp.views.product import add_product_view, product_detail_view


urlpatterns =[
    path("", index_view, name='index'),
    path("category/add/", add_category_view, name='add_category'),
    path("category/<int:pk>", category_detail_view, name='category_detail'),
    path("product/add/", add_product_view, name='add_product'),
    path("product/<int:pk>", product_detail_view, name='product_detail')
]