from django.shortcuts import render, get_object_or_404
from . import models


# Create your views here.
def index(request):
    products = models.Product.objects.all()
    return render(request, 'index.html', {'products': products})


def product_details(request, slug):
    product = models.Product.objects.get(slug=slug)
    return render(request, 'product_detail.html', {
        'products': product
    })


def search(request):
    if request.method == "POST":
        result = request.POST['q']
        product = models.Product.objects.filter(product_name__contains=result)
        return render(request, 'search_detail.html', {'products': product})
    result = {}
    return render(request, 'search_detail.html', {'results': result})


def product_list_by_category(request, slug):
    category = get_object_or_404(models.Category, slug=slug)
    products = models.Product.objects.filter(product_category=category)
    context = {'category': category, 'products': products}
    return render(request, 'search_detail.html', context)


def get_categories(request):
    categories = models.Category.objects.all()
    return render(request, 'index.html', {'categories': categories})
