from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from health_metrics.views import HealthMetricViewSet

# Django REST Framework router
router = DefaultRouter()
router.register(r'health-metrics', HealthMetricViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),           # Административен панел
    path('api/', include(router.urls)),        # Основни API маршрути
]