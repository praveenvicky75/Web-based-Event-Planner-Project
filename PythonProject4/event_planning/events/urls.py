from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HallViewSet, DecorationViewSet, FoodServiceViewSet, EventViewSet, BookingViewSet, MeView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'halls', HallViewSet, basename='hall')
router.register(r'decorations', DecorationViewSet, basename='decoration')
router.register(r'food-services', FoodServiceViewSet, basename='foodservice')
router.register(r'events', EventViewSet, basename='event')
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = [
    # JWT
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # current user
    path('me/', MeView.as_view(), name='me'),

    # all resources
    path('', include(router.urls)),
]
