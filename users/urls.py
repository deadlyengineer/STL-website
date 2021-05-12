from django.conf.urls import url, include
from .views import dashboard, register

urlpatterns = [
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^register/", register, name="register"),
    url(r"", dashboard, name="dashboard"),
]
