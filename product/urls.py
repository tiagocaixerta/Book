

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import include, path
from rest_framework import routers


from product.viewsets.category_viewset import CategoryViewSet
from product.viewsets.product_viewset import ProductViewSet

router = routers.SimpleRouter()
router.register(r"product", ProductViewSet, basename="product")
router.register(r"category", CategoryViewSet, basename="category")

from product import viewsets

router = routers.SimpleRouter()
router.register(r"product", viewsets.ProductViewSet, basename="product")
router.register(r"category", viewsets.CategoryViewSet, basename="category")


urlpatterns = [
    path("", include(router.urls)),
]
