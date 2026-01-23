from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, checkout


router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='orders')

urlpatterns = [
    path('checkout/', checkout, name='checkout' ),
    path('api/', include(router.urls))
]
