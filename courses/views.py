from django.shortcuts import render
from rest_framework import viewsets
from .serializer import DiscountSerializer, CourseTypeSerializar, CourseSerializar
from .models import Discount, Course_Type, Course


# Create your views here.
class DiscountView(viewsets.ModelViewSet):
    serializer_class = DiscountSerializer
    queryset = Discount.objects.all()


class CourseTypeView(viewsets.ModelViewSet):
    serializer_class = CourseTypeSerializar
    queryset = Course_Type.objects.all()


class CourseView(viewsets.ModelViewSet):
    serializer_class = CourseSerializar
    queryset = Course.objects.all()
