from datetime import datetime

from django.shortcuts import HttpResponse, render


# Create your views here.
def index(request):
    product = [
        {"name": "Laptop", "price": 199.99},
        {"name": "Mouse", "price": 499.99},
        {"name": "Keyboard", "price": 799.99},
    ]
    context = {
        "product": product,
        "price_threshold": 500,
    }

    return render(request, "product.html", context=context)
