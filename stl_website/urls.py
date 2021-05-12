from django.conf.urls import url, include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^upload/", include("stl_upload.urls")),
    url(r"", include("users.urls")),
]
