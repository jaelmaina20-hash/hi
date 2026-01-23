from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartViewSet, add_item, remove_item, summary


router = DefaultRouter()
router.register(r'cart', CartViewSet, basename='cart')
urlpatterns = [
    path('add_item', add_item, name='add-item'),
    path('remove_item', remove_item, name='remove-item'),
    path('summary', summary, name='summary'),
    path('api/', include(router.urls)),
]
