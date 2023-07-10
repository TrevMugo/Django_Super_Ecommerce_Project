from django.shortcuts import render
from .models import Product


def index(request):
    return render(request, 'index.html')


def add_product(request):
    if request.method == "POST":
        prod_name = request.POST.get("p-name")
        prod_qtty = request.POST.get("p-qtty")
        prod_size = request.POST.get("p-size")
        prod_price = request.POST.get("p-price")

        context = {
            "prod_name": prod_name,
            "prod_qtty": prod_qtty,
            "prod_size": prod_size,
            "prod_price": prod_price,
            "success": "Product saved successfully!"
        }

        query = Product(name=prod_name, qtty=prod_qtty,
                        size=prod_size, price=prod_price)
        query.save()
        return render(request, 'add-product.html', context)
    return render(request, 'add-product.html')


def all_products(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'products.html', context)
