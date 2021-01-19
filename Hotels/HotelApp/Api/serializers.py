from rest_framework import serializers
from ..models import *
from django.contrib.auth.models import User
from rest_framework.fields import CurrentUserDefault


class ApiGenderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genders
        fields = '__all__'

    def create(self, validated_data):
        return Genders.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.gender = validated_data["gender"]
        instance.save()
        return instance

class ApiRoomTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = RoomType
        fields = '__all__'

    def create(self, validated_data):
        return RoomType.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.room = validated_data["room"]
        instance.save()
        return instance

class ApiProvinceSerializer(serializers.ModelSerializer):
    # province = serializers.CharField(max_length=200)

    class Meta:
        model = Provinces
        fields = '__all__'

    def create(self, validated_data):
        return Provinces.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.province = validated_data["province"]
        instance.save()
        return instance

class ApiStateSerializer(serializers.ModelSerializer):
    province = serializers.CharField()
    class Meta:
        model = States
        fields = '__all__'

    def create(self, validated_data):
        province_data = validated_data.pop('province')
        province_new_data_instance, created = Provinces.objects.get_or_create(province=province_data)
        state_data = States.objects.create(**validated_data, province=province_new_data_instance)
        return state_data

    def update(self, instance, validated_data):
        province_name = validated_data.get('province')
        province_id = Provinces.objects.get(province=province_name)
        instance.state = validated_data["state"]
        instance.province = province_id
        instance.save()
        return instance

class ApiQuarterSerializer(serializers.ModelSerializer):
    state = serializers.CharField()
    class Meta:
        model = Quarters
        fields = '__all__'
        
    def create(self, validated_data):
        state_data = validated_data.pop('state')
        state_new_data_instance, created = States.objects.get_or_create(state=state_data)
        quarter_data = Quarters.objects.create(**validated_data, state=state_new_data_instance)
        return quarter_data

    def update(self, instance, validated_data):
        state_name = validated_data.get('state')
        state_id = States.objects.get(state=state_name)
        instance.quarter = validated_data["quarter"]
        instance.state = state_id
        instance.save()
        return instance

class ApiHotelSerializer(serializers.ModelSerializer):
    province = serializers.CharField()

    class Meta:
        model = Hotels
        fields = '__all__'
        
    def create(self, validated_data):
        province_data = validated_data.pop('province')
        province_new_data_instance, created = Provinces.objects.get_or_create(province=province_data)
        hotel_data = Hotels.objects.create(**validated_data, province=province_new_data_instance)
        return hotel_data

    def update(self, instance, validated_data):
        province_name = validated_data.get('province')
        province_id = Provinces.objects.get(province=province_name)
        instance.name = validated_data["name"]
        instance.province = province_id
        instance.photo_outside = validated_data["photo_outside"]
        instance.photo_inside = validated_data["photo_inside"]
        instance.photo_room = validated_data["photo_room"]
        instance.save()
        return instance

class ApiRoomSerializer(serializers.ModelSerializer):
    hotel = serializers.CharField()
    room = serializers.CharField()
    photo_room = serializers.ImageField()

    class Meta:
        model = Rooms
        fields = '__all__'
        
    def create(self, validated_data):
        hotel_data = validated_data.pop('hotel')
        room_type_data = validated_data.pop('room')
        photo_room_data = validated_data["photo_room"]
        hotel_new_data_instance, created = Hotels.objects.get_or_create(hotel=hotel_data)
        room_new_data_instance, created = RoomType.objects.get_or_create(room=room_type_data)
        room_data = Rooms.objects.create(**validated_data, hotel=hotel_new_data_instance,room=room_new_data_instance,photo_room=photo_room_data)
        return room_data

    def update(self, instance, validated_data):
        hotel_name = validated_data.get('hotel')
        hotel_id = Hotels.objects.get(hotel=hotel_name)
        instance.hotel = hotel_id
        instance.room = validated_data["room"]
        instance.room_number = validated_data["room_number"]
        instance.price = validated_data["price"]
        instance.save()
        return instance

class ApiReservationSerializer(serializers.ModelSerializer):
    hotel = serializers.CharField()
    room_number = serializers.CharField()

    class Meta:
        model = Reservations
        fields = '__all__'
        
    # def save(self):
    #     client = CurrentUserDefault()  # <= magic!
        
    def create(self, validated_data):
        hotel_data = validated_data.pop('hotel')
        room_number_data = validated_data.pop('room_number')
        validated_data['client'] = self.context['request'].client

        client_new_data_instance, created = Clients.objects.get_or_create(client=validated_data['client'])
        hotel_new_data_instance, created = Hotels.objects.get_or_create(hotel=hotel_data)
        room_number_new_data_instance, created = Rooms.objects.get_or_create(room_number=room_number_data)
        reservation_data = Reservations.objects.create(**validated_data, client=client_new_data_instance, hotel=hotel_new_data_instance, room_number=room_number_new_data_instance)
        return reservation_data

    def update(self, instance, validated_data):
        instance.client = validated_data["client"]
        instance.hotel = validated_data["hotel"]
        instance.room = validated_data["room"]
        instance.taken = validated_data["taken"]
        instance.transaction_code = validated_data["transaction_code"]
        instance.save()
        return instance
