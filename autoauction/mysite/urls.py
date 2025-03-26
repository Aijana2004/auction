from rest_framework import routers
from .views import *
from django.urls import path, include

router = routers.SimpleRouter()

router.register(r'user', UserProfileViewSet, basename='user')

router.register(r'feedback', FeedbackViewSet, basename='feedback')


urlpatterns = [
    path('', include(router.urls)),


    path('car/', CarListAPIView.as_view(), name=' car_list'),
    path('car/create/', CarCreateAPIView.as_view(), name='car_create'),
    path('car/edit/<int:pk>/', CarUpdateAPIView.as_view(), name='car_edit'),
    path('auction/', AuctionListApiView.as_view(), name=' auction_list'),
    path('auction/create/', AuctionCreateAPIView.as_view(), name='auction_create'),
    path('auction/edit/<int:pk>/', AuctionUpdateAPIView.as_view(), name='auction_edit'),
    path('bid/', BidListAPIView.as_view(), name=' bid_list'),
    path('bid/create/', BidCreateAPIView.as_view(), name='bid_create'),
    path('bid/edit/<int:pk>/', BidUpdateAPIView.as_view(), name='bid_edit'),

]
