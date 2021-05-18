from django.conf.urls import url
from .views import submit_input, UserProcessApiView, UploadStl

urlpatterns = [
    # url(r"^upload/", upload, name="upload"),
    url(r"^inputs/", submit_input, name="inputs"),
    url(r"^saveProcess", UserProcessApiView.as_view(), name='saveProcess'),
    url(r"^upload_stl", UploadStl.as_view(), name="upload")
]
