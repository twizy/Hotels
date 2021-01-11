<template>
    <div>
        <h1>Quarters</h1>

        <app-quarter></app-quarter>

        <app-quarter-list></app-quarter-list>

    </div>
</template>

<script>

import quarterform from '../components/forms/quarterform.vue';
import quarterlist from '../components/lists/quarterlist.vue';

export default {
    components:{
        'app-quarter':quarterform,
        'app-quarter-list':quarterlist
    }
}
</script>

<style scoped>

</style>