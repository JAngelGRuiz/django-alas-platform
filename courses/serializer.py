from rest_framework import serializers
from .models import Discount, Course_Type, Course, Subject


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = "__all__"


class CourseTypeSerializar(serializers.ModelSerializer):
    class Meta:
        model = Course_Type
        fields = "__all__"


class CourseSerializar(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class SubjectSerializar(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"
