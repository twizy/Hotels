import home from './pages/home.vue';
import hotel from './pages/hotel.vue';
import province from './pages/province.vue';
import state from './pages/state.vue';
import quarter from './pages/quarter.vue';
import room from './pages/room.vue';
import reservation from './pages/reservation.vue';

// Update imports
import updateprovince from './pages/updatepages/province.vue';

// Details imports
import hoteldetails from './pages/detailspages/hotel.vue';

export const routes = [
    { path: '/', component: home },
    { path: '/hotel', component: hotel },
    { path: '/province', component: province },
    { path: '/state', component: state },
    { path: '/quarter', component: quarter },
    { path: '/room', component: room },
    { path: '/reservation', component: reservation },

    // Update pages

    { path: '/update-province', component: updateprovince },

    // Details pages

    { path: '/hotel-details', component: hoteldetails },
];