from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from ..models import *
from django.contrib.auth.models import User

# Province views

@api_view(['GET'])
def ApiProvincesList(request):
    provinces = Provinces.objects.all()
    serializer = ApiProvinceSerializer(provinces, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ApiProvincesDetails(request, pk):
    provinces = Provinces.objects.get(id=pk)
    serializer = ApiProvinceSerializer(provinces, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def ApiProvincesCreate(request):
    serializer = ApiProvinceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def ApiProvincesUpdate(request, pk):
    provinces = Provinces.objects.get(id=pk)
    serializer = ApiProvinceSerializer(instance=provinces, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def ApiProvincesDelete(request, pk):
    provinces = Provinces.objects.get(id=pk)
    provinces.delete()
    return Response("Deleted")

# States views

@api_view(['GET'])
def ApiStatesList(request):
    states = States.objects.all()
    serializer = ApiStateSerializer(states, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ApiStatesDetails(request, pk):
    states = States.objects.get(id=pk)
    serializer = ApiStateSerializer(states, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def ApiStatesDelete(request, pk):
    states = States.objects.get(id=pk)
    states.delete()
    return Response("Deleted")

@api_view(['POST'])
def ApiStatesCreate(request):
    serializer = ApiStateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def ApiStatesUpdate(request, pk):
    states = States.objects.get(id=pk)
    serializer = ApiStateSerializer(instance=states, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Quarter views

@api_view(['GET'])
def ApiQuartersList(request):
    quarters = Quarters.objects.all()
    serializer = ApiQuarterSerializer(quarters, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ApiQuartersDetails(request, pk):
    quarters = Quarters.objects.get(id=pk)
    serializer = ApiQuarterSerializer(quarters, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def ApiQuartersDelete(request, pk):
    quarters = Quarters.objects.get(id=pk)
    quarters.delete()
    return Response("Deleted")

@api_view(['POST'])
def ApiQuartersCreate(request):
    serializer = ApiQuarterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def ApiQuartersUpdate(request, pk):
    quarters = Quarters.objects.get(id=pk)
    serializer = ApiQuarterSerializer(instance=quarters, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Reservations views

@api_view(['GET'])
def ApiReservationsList(request):
    reservations = Reservations.objects.all()
    serializer = ApiReservationSerializer(reservations, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ApiReservationsDetails(request, pk):
    reservations = Reservations.objects.get(id=pk)
    serializer = ApiReservationSerializer(reservations, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def ApiReservationsDelete(request, pk):
    reservations = Reservations.objects.get(id=pk)
    reservations.delete()
    return Response("Deleted")

@api_view(['POST'])
def ApiReservationsCreate(request):
    serializer = ApiReservationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def ApiReservationsUpdate(request, pk):
    reservations = Reservations.objects.get(id=pk)
    serializer = ApiReservationSerializer(instance=reservations, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Rooms views

@api_view(['GET'])
def ApiRoomsList(request):
    rooms = Rooms.objects.all()
    serializer = ApiRoomSerializer(rooms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ApiRoomsDetails(request, pk):
    rooms = Rooms.objects.get(id=pk)
    serializer = ApiRoomSerializer(rooms, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def ApiRoomsDelete(request, pk):
    rooms = Rooms.objects.get(id=pk)
    rooms.delete()
    return Response("Deleted")

@api_view(['POST'])
def ApiRoomsCreate(request):
    serializer = ApiRoomSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def ApiRoomsUpdate(request, pk):
    rooms = Rooms.objects.get(id=pk)
    serializer = ApiRoomSerializer(instance=rooms, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Hotels views

@api_view(['GET'])
def ApiHotelsList(request):
    hotels = Hotels.objects.all()
    serializer = ApiHotelSerializer(hotels, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ApiHotelsDetails(request, pk):
    hotels = Hotels.objects.get(id=pk)
    serializer = ApiHotelSerializer(hotels, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def ApiHotelsDelete(request, pk):
    hotels = Hotels.objects.get(id=pk)
    hotels.delete()
    return Response("Deleted")

@api_view(['POST'])
def ApiHotelsCreate(request):
    serializer = ApiHotelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def ApiHotelsUpdate(request, pk):
    hotels = Hotels.objects.get(id=pk)
    serializer = ApiHotelSerializer(instance=hotels, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)





