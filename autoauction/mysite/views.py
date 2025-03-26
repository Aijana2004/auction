from requests import Response
from rest_framework import viewsets, generics, status
from .serializers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from .filters import CarFilter
from .permissions import CheckCreateCar,CheckOwnerCar,CheckCreateBid,CheckOwnerBid


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers


class CarListAPIView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarListSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CarFilter
    search_fields =['model','year','transmission','fuel_type','brand']
    ordering_fields = ['price']



class CarCreateAPIView(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarCreateSerializers
    permission_classes = [CheckCreateCar]


class CarUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarCreateSerializers
    permission_classes = [CheckCreateCar,CheckOwnerCar]


class AuctionListApiView(generics.ListAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializers


class AuctionCreateAPIView(generics.CreateAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionCreateSerializers
    permission_classes = [CheckCreateCar]


class AuctionUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionCreateSerializers
    permission_classes = [CheckCreateCar, CheckOwnerCar]


class BidListAPIView(generics.ListAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidSerializers


class BidCreateAPIView(generics.CreateAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidCreateSerializers
    permission_classes = [CheckCreateBid]


class BidUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidCreateSerializers
    permission_classes = [CheckCreateBid,CheckOwnerBid]


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializers