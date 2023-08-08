from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from django.urls import path, include
from .views import DiscountView, CourseTypeView, CourseView

router = routers.DefaultRouter()
router.register(r"discounts", DiscountView, "Discounts")
router.register(r"courses", CourseView, "courses")
router.register(r"type/course", CourseTypeView, "course_types")

urlpatterns = [
    path("", include(router.urls)),
]
