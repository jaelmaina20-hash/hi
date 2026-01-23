from django.shortcuts import render
from rest_framework import viewsets
from .models import Order, OrderItem
from .serializers import OrderSerializer
from rest_framework.response import Response
from django.db import transaction
from rest_framework.decorators import action

# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
@action(detail=True, methods=['post'])
def checkout(self, request, pk=None):
    """Custom method to convert Cart to Order"""
    cart = self.get_object()
    items = cart.items.all()
    
    if not items.exists():
        return Response({"error": "Cart is empty"}, status=status.HTTP_400_BAD_REQUEST)

    with transaction.atomic():
        # 1. Create the Order
        order = Order.objects.create(
            customer=cart.customer,
            status='Pending'
        )

        total = 0
        for item in items:
            # 2. Check Stock
            if item.product.stock < item.quantity:
                return Response({f"error": f"Not enough stock for {item.product.name}"}, status=status.HTTP_400_BAD_REQUEST)
            
            # 3. Create OrderItem (Capture current price)
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price_at_purchase=item.product.price
            )
            
            # 4. Deduct Stock
            item.product.stock -= item.quantity
            item.product.save()
            
            total += item.product.price * item.quantity

        # 5. Update Total and Clear Cart
        order.total_price = total
        order.save()
        items.delete() 

    return Response({"message": "Order placed!", "order_id": order.id})
