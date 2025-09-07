from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Hall, Decoration, FoodService, Event, Booking

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Role', {'fields': ('role',)}),
    )
    list_display = ('username', 'email', 'role', 'is_staff', 'is_superuser')

admin.site.register(Hall)
admin.site.register(Decoration)
admin.site.register(FoodService)
admin.site.register(Event)
admin.site.register(Booking)
