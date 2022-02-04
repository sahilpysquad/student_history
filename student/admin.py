from django.contrib import admin
from .models import Student, GradeHistory, FileUpload


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("fname", "department", "start_first_year", "detain_year")


@admin.register(GradeHistory)
class GradeHistoryAdmin(admin.ModelAdmin):
    list_display = (
        "student",
        "first_year_spi",
        "second_year_spi",
        "third_year_spi",
        "fourth_year_spi",
    )


@admin.register(FileUpload)
class GradeHistoryAdmin(admin.ModelAdmin):
    pass
