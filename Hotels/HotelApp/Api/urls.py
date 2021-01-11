from django.urls import path, include
from .views import *

app_name = 'HotelApp'

urlpatterns = [

    # Provinces Api Urls
    path('province-list/', ApiProvincesList, name="province-list"),
    path('province-create/', ApiProvincesCreate, name="province-create"),
    path('province-details/<str:pk>/', ApiProvincesDetails, name="province-details"),
    path('province-update/<str:pk>/', ApiProvincesUpdate, name="province-update"),
    path('province-delete/<str:pk>/', ApiProvincesDelete, name="province-delete"),

    # States Api Urls
    path('state-list/', ApiStatesList, name="state-list"),
    path('state-create/', ApiStatesCreate, name="state-create"),
    path('state-details/<str:pk>/', ApiStatesDetails, name="state-details"),
    path('state-update/<str:pk>/', ApiStatesUpdate, name="state-update"),
    path('state-delete/<str:pk>/', ApiStatesDelete, name="state-delete"),

    # Quarters Api Urls
    path('quarter-list/', ApiQuartersList, name="quarter-list"),
    path('quarter-create/', ApiQuartersCreate, name="quarter-create"),
    path('quarter-details/<str:pk>/', ApiQuartersDetails, name="quarter-details"),
    path('quarter-update/<str:pk>/', ApiQuartersUpdate, name="quarter-update"),
    path('quarter-delete/<str:pk>/', ApiQuartersDelete, name="quarter-delete"),

    # Reservations Api Urls
    path('reservation-list/', ApiReservationsList, name="reservation-list"),
    path('reservation-create/', ApiReservationsCreate, name="reservation-create"),
    path('reservation-details/<str:pk>/', ApiReservationsDetails, name="reservation-details"),
    path('reservation-update/<str:pk>/', ApiReservationsUpdate, name="reservation-update"),
    path('reservation-delete/<str:pk>/', ApiReservationsDelete, name="reservation-delete"),

    # Rooms Api Urls
    path('room-list/', ApiRoomsList, name="room-list"),
    path('room-create/', ApiRoomsCreate, name="room-create"),
    path('room-details/<str:pk>/', ApiRoomsDetails, name="room-details"),
    path('room-update/<str:pk>/', ApiRoomsUpdate, name="room-update"),
    path('room-delete/<str:pk>/', ApiRoomsDelete, name="room-delete"),

     # Hotels Api Urls
    path('hotel-list/', ApiHotelsList, name="hotel-list"),
    path('hotel-create/', ApiHotelsCreate, name="hotel-create"),
    path('hotel-details/<str:pk>/', ApiHotelsDetails, name="hotel-details"),
    path('hotel-update/<str:pk>/', ApiHotelsUpdate, name="hotel-update"),
    path('hotel-delete/<str:pk>/', ApiHotelsDelete, name="hotel-delete"),

]