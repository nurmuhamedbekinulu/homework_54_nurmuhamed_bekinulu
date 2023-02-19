from django.urls import path
from webapp.views.base import index_view


urlpatterns =[
    path("", index_view, name='index'),
    path("category/add/", add_category_view, name='article_add'),
    path("category/<int:pk>", category_detail_view, name='article_detail')
]