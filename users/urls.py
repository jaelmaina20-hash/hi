from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet
from . import views


router = DefaultRouter()
router.register(r'customer', CustomerViewSet, basename='customer')

urlpatterns = [
    path('', include(router.urls)),
    path('user_profile', views.create_profile, name ='create-profile'),
    ]
