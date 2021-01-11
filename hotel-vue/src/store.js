import Vue from 'vue';
import Vuex from 'vuex';
import Axios from 'axios';

Vue.use(Vuex,Axios);

export const store = new Vuex.Store({
    state: {
        proState: {
            province: ''
        },
        staState: {
            province: '',
            state: ''
        },
        quaState: {
            state: '',
            quarter: ''
        },
        hotState: {
            name: '',
            province: '',
            photo_outside: null,
            photo_inside: null,
            photo_room: null,
            date: '2021-01-09'
        },
        rooState: {
            hotel: '',
            room: '',
            room_number: '',
            price: 0
        },

        allProvinces: [],
        allHotelRooms: ['Room type', 'Single occupation', 'Double occupation', 'Both occupation'],
        allRooms: [],
        allStates: [],
        allQuarters: [],
        allReservations: [],
        allHotels: []
    }
});