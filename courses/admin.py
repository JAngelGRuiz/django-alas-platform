from django.contrib import admin
from .models import Course, Discount, Type, Subject, Classes

# Register your models here.
admin.site.register([Course, Discount, Type, Subject, Classes])
