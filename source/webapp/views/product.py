from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Product, Category
from django.http import HttpResponseNotFound
from django.urls import reverse


def add_product_view(request: WSGIRequest):
    if request.method == "GET":
        categories = Category.objects.all()
        return render(request, 'product_create.html', context={
            'categories': categories
        })
    product_data = {
        'product_name': request.POST.get('product_name'),
        'description': request.POST.get('description'),
        'category': Category.objects.get(id=request.POST['category']),
        'price': request.POST.get('price'),
        'image_url': request.POST.get('image_url')
    }
    product = Product.objects.create(**product_data)
    return redirect('product_detail', pk=product.pk)


def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', context={
        'product': product
    })
