<template>
    <div>
        <h1>Hotels</h1>

        <app-hotel></app-hotel>

        <app-hotel-list></app-hotel-list>

    </div>
</template>

<script>

import hotelform from '../components/forms/hotelform.vue';
import hotellist from '../components/lists/hotellist.vue';

export default {
    components:{
        'app-hotel':hotelform,
        'app-hotel-list':hotellist
    }
}
</script>

<style scoped>

</style>