from rest_framework import serializers
from .models import CustomUser, Hall, Decoration, FoodService, Event, Booking

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role']


class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = ['id', 'name', 'location', 'capacity', 'price_per_day', 'created_by']


class DecorationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Decoration
        fields = ['id', 'name', 'description', 'price', 'compatible_halls']


class FoodServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodService
        fields = ['id', 'name', 'category', 'price_per_person']


class EventSerializer(serializers.ModelSerializer):
    hall = HallSerializer(read_only=True)
    hall_id = serializers.PrimaryKeyRelatedField(queryset=Hall.objects.all(), source='hall', write_only=True, required=False)
    decoration = DecorationSerializer(read_only=True)
    decoration_id = serializers.PrimaryKeyRelatedField(queryset=Decoration.objects.all(), source='decoration', write_only=True, required=False)
    food_service = FoodServiceSerializer(read_only=True)
    food_service_id = serializers.PrimaryKeyRelatedField(queryset=FoodService.objects.all(), source='food_service', write_only=True, required=False)

    class Meta:
        model = Event
        fields = ['id', 'title', 'event_type', 'description', 'date', 'start_time', 'end_time', 'hall', 'hall_id', 'decoration', 'decoration_id', 'food_service', 'food_service_id', 'created_by']
        read_only_fields = ['created_by']

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['created_by'] = request.user
        return super().create(validated_data)


class BookingSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)
    event_id = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all(), source='event', write_only=True)

    customer = UserSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'event', 'event_id', 'customer', 'guests', 'total_price', 'status', 'created_at']
        read_only_fields = ['customer', 'status', 'created_at']

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['customer'] = request.user
        # optionally compute price here (hall + decoration + food)
        event = validated_data.get('event')
        guests = validated_data.get('guests', 0)
        total = 0
        if event and event.hall:
            total += float(event.hall.price_per_day)
        if event and event.decoration:
            total += float(event.decoration.price)
        if event and event.food_service:
            total += float(event.food_service.price_per_person) * guests
        validated_data['total_price'] = total
        return super().create(validated_data)
