from django.shortcuts import render, get_object_or_404

from .models import Product

from category.models import Category


def store(request, category_slug):

    categories = None
    product = None
    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        products_count = products.count()

    else:

        products = Product.objects.all().filter(is_available=True)
        
        products_count = products.count()
    categories = Category.objects.all()

    context = {
        'products': products,
        'products_count':products_count,
        'categories': categories,
    }

    return render(request, 'store/store.html', context)

def display_category(request, category_slug=None):
    categories = None
    product = None
    if category_slug is not None:
        categories = get_object_or_404(Category, category_slug)
        products = Product.objects.filter(Category=categories, is_available=True)
        products_count = products.count()





