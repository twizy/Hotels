<template>
    <div>
        <h1>Rooms</h1>

        <app-room></app-room>

        <app-room-list></app-room-list>

    </div>
</template>

<script>

import roomform from '../components/forms/roomform.vue';
import roomlist from '../components/lists/roomlist.vue';

export default {
    components:{
        'app-room':roomform,
        'app-room-list':roomlist
    }
}
</script>

<style scoped>

</style>