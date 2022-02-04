from django.db import models
from django.contrib.postgres.fields import ArrayField


class Student(models.Model):
    DEPARTMENTS = (
        ("IT", "Information Technology"),
        ("CE", "Computer Engineering"),
        ("ME", "Mechanical Engineering"),
        ("PE", "Power Engineering"),
        ("EE", "Electrical Engineering")
    )
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    phone = models.IntegerField()
    department = models.CharField(choices=DEPARTMENTS, max_length=2)
    start_first_year = models.IntegerField()
    detain_year = ArrayField(models.IntegerField(), blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.fname, self.lname)


class GradeHistory(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    first_year_spi = models.IntegerField(blank=True, null=True)
    second_year_spi = models.IntegerField(blank=True, null=True)
    third_year_spi = models.IntegerField(blank=True, null=True)
    fourth_year_spi = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.student.fname


class FileUpload(models.Model):
    COURSE_CHOICES = (
        ("BSC", "Bachelor of Science (BSC)"),
        ("BE", "Bachelor of Engineering (BE)"),
        ("BCA", "Bachelor of Computer Applications (BCA)"),
        ("BPT", "Bachelor of Physiotherapy (BPT)"),
        ("CCC", "Course on Computer Concepts (CCC)"),
        ("BA", "Bachelor of Arts (BA)"),
        ("BCOM", "Bachelor of Commerce (BCOM)"),
        ("MBBS", "Bachelor of Medicine (MBBS)"),
    )
    name = models.CharField(max_length=30, null=True, blank=True)
    media_file = models.FileField()
    course = models.CharField(choices=COURSE_CHOICES, max_length=5, default="BE")

    def __str__(self):
        return self.name
