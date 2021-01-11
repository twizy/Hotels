import hotel from './pages/hotel.vue';
import province from './pages/province.vue';
import state from './pages/state.vue';
import quarter from './pages/quarter.vue';
import room from './pages/room.vue';
import reservation from './pages/reservation.vue';

export const routes = [
    { path: '/hotel', component: hotel },
    { path: '/province', component: province },
    { path: '/state', component: state },
    { path: '/quarter', component: quarter },
    { path: '/room', component: room },
    { path: '/reservation', component: reservation },
];