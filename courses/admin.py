from django.contrib import admin
from .models import Course, Discount, Course_Type, Subject, Lesson

# Register your models here.
admin.site.register([Course, Discount, Course_Type, Subject, Lesson])
