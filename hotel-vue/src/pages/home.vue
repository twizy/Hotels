<template>
    <div>
        <h1>All hotels</h1>

            <app-hotel-card></app-hotel-card>

    </div>
</template>

<script>

import hotelcard from '../components/hotelcard.vue';

export default {
    components:{
        'app-hotel-card':hotelcard,
    },
    
    
}
</script>

<style scoped>

</style>