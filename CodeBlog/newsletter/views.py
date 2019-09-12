# from django.shortcuts import render

from rest_framework.permissions import BasePermission, IsAdminUser, AllowAny, SAFE_METHODS
from rest_framework import generics
from .CustomAnonRateThrottle import CustomAnonRateThrottle

from .serializers import SubscriberSerializer
from .models import Subscriber


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
    
class SubscriberDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
    permission_classes = [IsAdminUser|ReadOnly]
    throttle_classes = [CustomAnonRateThrottle]


# Email link from newsletter to frontend 
# when user clicks the unsubscribe button get the
# email param from the url on the frontend and send a
# put or patch request with subscribed set to false
class SubscriberCreateView(generics.CreateAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
    permission_classes = [AllowAny]
    throttle_classes = [CustomAnonRateThrottle]
    
