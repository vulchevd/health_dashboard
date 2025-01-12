from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotificationViewSet

# Django REST Framework router
router = DefaultRouter()
router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

