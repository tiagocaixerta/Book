import debug_toolbar
from book import views
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth import views as auth_views
from django.http import HttpResponse  # <- adicionado

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__debug__/", include(debug_toolbar.urls)),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
    path("update_server/", views.update, name="update"),
    path("hello/", views.hello_world, name="hello_world"),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    re_path("book/(?P<version>(v1|v2))/", include("order.urls")),
    re_path("book/(?P<version>(v1|v2))/", include("product.urls")),

    # Página inicial simples
    path("", lambda request: HttpResponse("<h1>Bem-vindo à API!</h1>"), name="home"),
]
