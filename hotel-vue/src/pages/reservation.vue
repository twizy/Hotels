<template>
    <div>
        <h1>Reservations</h1>

        <app-reservation></app-reservation>

        <app-reservation-list></app-reservation-list>

    </div>
</template>

<script>

import reservationform from '../components/forms/reservationform.vue';
import reservationlist from '../components/lists/reservationlist.vue';

export default {
    components:{
        'app-reservation':reservationform,
        'app-reservation-list':reservationlist
    }
}
</script>

<style scoped>

</style>