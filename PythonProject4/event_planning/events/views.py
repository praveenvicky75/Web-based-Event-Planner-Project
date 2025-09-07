from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import CustomUser, Hall, Decoration, FoodService, Event, Booking
from .serializers import (UserSerializer, HallSerializer, DecorationSerializer,
                          FoodServiceSerializer, EventSerializer, BookingSerializer)
from .permissions import IsAdminUserRole, IsCustomerOrAdminReadOnly
from rest_framework.views import APIView

# Admin-only management for halls, decorations, food services
class HallViewSet(viewsets.ModelViewSet):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer
    permission_classes = [permissions.IsAuthenticated & IsAdminUserRole]  # admin only

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class DecorationViewSet(viewsets.ModelViewSet):
    queryset = Decoration.objects.all()
    serializer_class = DecorationSerializer
    permission_classes = [permissions.IsAuthenticated & IsAdminUserRole]

class FoodServiceViewSet(viewsets.ModelViewSet):
    queryset = FoodService.objects.all()
    serializer_class = FoodServiceSerializer
    permission_classes = [permissions.IsAuthenticated & IsAdminUserRole]

# Events: admin creates events, everyone can list and view
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('date')
    serializer_class = EventSerializer
    # Allow anyone read-only, creation only for admin
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAuthenticated, IsAdminUserRole]
        else:
            permission_classes = [permissions.AllowAny]
        return [perm() for perm in permission_classes]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

# Bookings: customers create bookings; admin can change status and view all
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all().order_by('-created_at')
    serializer_class = BookingSerializer

    def get_permissions(self):
        if self.action in ['create']:
            permission_classes = [permissions.IsAuthenticated]  # customer or admin can create (customer expected)
        elif self.action in ['update', 'partial_update', 'destroy']:
            # only admin can change status or delete
            permission_classes = [permissions.IsAuthenticated, IsAdminUserRole]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [perm() for perm in permission_classes]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and user.role == 'admin':
            return Booking.objects.all().order_by('-created_at')
        elif user.is_authenticated:
            return Booking.objects.filter(customer=user).order_by('-created_at')
        return Booking.objects.none()

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

# current user detail
class MeView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        return Response(UserSerializer(request.user).data)
