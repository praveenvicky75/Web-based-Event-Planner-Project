from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Custom user with role (customer/admin)
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')

    def __str__(self):
        return f"{self.username} ({self.role})"


class Hall(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    capacity = models.PositiveIntegerField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    # created_by: which admin created this hall (optional)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='halls')

    def __str__(self):
        return self.name


class Decoration(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    compatible_halls = models.ManyToManyField(Hall, blank=True, related_name='decorations')

    def __str__(self):
        return self.name


class FoodService(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100, help_text='eg: South Indian, Pure Veg, Non-Veg')
    price_per_person = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.category})"


class Event(models.Model):
    EVENT_TYPES = [
        ('wedding', 'Wedding'),
        ('birthday', 'Birthday'),
        ('conference', 'Conference'),
        ('other', 'Other'),
    ]
    title = models.CharField(max_length=200)
    event_type = models.CharField(max_length=50, choices=EVENT_TYPES, default='other')
    description = models.TextField(blank=True)
    date = models.DateField()
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    hall = models.ForeignKey(Hall, on_delete=models.SET_NULL, null=True, blank=True)
    decoration = models.ForeignKey(Decoration, on_delete=models.SET_NULL, null=True, blank=True)
    food_service = models.ForeignKey(FoodService, on_delete=models.SET_NULL, null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='events')

    def __str__(self):
        return f"{self.title} - {self.date}"


class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='bookings')
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings')
    guests = models.PositiveIntegerField(default=0)
    total_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking {self.id} by {self.customer}"
