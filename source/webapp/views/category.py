from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Category
from django.http import HttpResponseNotFound
from django.urls import reverse


def add_category_view(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'category_create.html')
    category_data = {
        'category_name': request.POST.get('category_name'),
        'description': request.POST.get('description')
    }
    category = Category.objects.create(**category_data)
    return redirect('category_detail', pk=category.pk)


def category_detail_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'category.html', context={
        'category': category
        })