<template>
    <div>
        <h1>Provinces</h1>
        <app-province></app-province>

        <app-province-list></app-province-list>

    </div>
</template>

<script>

import provinceform from '../components/forms/provinceform.vue';
import provincelist from '../components/lists/provincelist.vue';

export default {
    components:{
        'app-province':provinceform,
        'app-province-list':provincelist
    }
}
</script>

<style scoped>

</style>