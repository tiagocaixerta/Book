from django.contrib import admin
from django.urls import path, re_path, include
from django.http import JsonResponse

def api_home(request):
    return JsonResponse({
        "message": "Bem-vindo à API!",
        "endpoints": [
            "/book/v1/products/",
            "/book/v1/orders/"
        ]
    })

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", api_home),

    # Para v1
    path("book/v1/products/", include("product.urls")),
    path("book/v1/orders/", include("order.urls")),

    # Para v2
    path("book/v2/products/", include("product.urls")),
    path("book/v2/orders/", include("order.urls")),
]
