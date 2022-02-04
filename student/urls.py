from django.urls import path
from .views import FileUploadCreateView

urlpatterns = [
    path("uploadfile/", FileUploadCreateView.as_view(), name="upload-file"),
]
