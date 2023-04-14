from django.contrib import admin
from studentapp.models import Student
from studentapp.models import Course


# Register your models here.
admin.site.register(Student)
admin.site.register(Course)