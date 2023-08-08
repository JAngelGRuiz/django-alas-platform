from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.views import APIView
from .serializer import (
    DiscountSerializer,
    CourseTypeSerializar,
    CourseSerializar,
    SubjectSerializar,
)
from .models import Discount, Course_Type, Course, Subject


# Create your views here.
class DiscountView(viewsets.ModelViewSet, mixins.CreateModelMixin):
    serializer_class = DiscountSerializer
    queryset = Discount.objects.all()

    def create(self, request, *args, **kwargs):
        print("POST request", request.data)

        return super().list(request, *args, **kwargs)


class CourseTypeView(viewsets.ModelViewSet):
    serializer_class = CourseTypeSerializar
    queryset = Course_Type.objects.all()


class CourseView(viewsets.ModelViewSet):
    serializer_class = CourseSerializar
    queryset = Course.objects.all()


class SubjectView(viewsets.ModelViewSet):
    serializer_class = SubjectSerializar
    queryset = Subject.objects.all()
