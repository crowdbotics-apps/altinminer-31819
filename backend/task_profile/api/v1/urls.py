from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    TaskerProfileViewSet,
    CustomerProfileViewSet,
    NotificationViewSet,
    InviteCodeViewSet,
)

router = DefaultRouter()
router.register("customerprofile", CustomerProfileViewSet)
router.register("invitecode", InviteCodeViewSet)
router.register("taskerprofile", TaskerProfileViewSet)
router.register("notification", NotificationViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
