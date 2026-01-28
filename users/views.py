from django.shortcuts import render
from rest_framework import viewsets
from .models import Customer, UserProfile
from .serializers import CustomerSerializer


# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


def create_profile(request):
    user_profile = UserProfile.objects.create(  
        username = 'jael',
        email = 'jael@gmail.com',
        ssn = '123-4556-4456',
        bio ='fcvgybhjn')
   
   
   
    print(user_profile.ssn)
    print(user_profile.bio)  
    return render(user_profile, '')
   
      