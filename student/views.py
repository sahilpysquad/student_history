from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.views.generic.edit import CreateView
from django.contrib import messages
from .form import FileUploadForm
from .models import FileUpload


class FileUploadCreateView(CreateView):
    model = FileUpload
    form_class = FileUploadForm
    template_name = "student/file_upload_form.html"

    def post(self, request, *args, **kwargs):
        csv_file = request.FILES.get("media_file")
        course = request.POST.get("course")
        if not csv_file.name.endswith(".csv"):
            messages.error(request, "Upload .csv file.")
            # return HttpResponseRedirect(reverse("student:upload-file"))
            return render(request, template_name="student/file_upload_form.html", context={"form": FileUploadForm()})
        datasets = csv_file.read().decode("utf-8")
        lines = datasets.split("\n")
        data = {}
        for line in lines:
            print(line)
        return render(request, template_name="student/file_upload_form.html")
