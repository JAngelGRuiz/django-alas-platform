from rest_framework import routers
from django.urls import path, include
from .views import loginView

router = routers.DefaultRouter()
router.register(r"login", loginView, "login")

urlpatterns = [
    path("/login", include(router.urls)),
]
