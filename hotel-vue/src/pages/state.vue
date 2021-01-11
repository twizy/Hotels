<template>
    <div>
        <h1>States</h1>

        <app-state></app-state>

        <app-state-list></app-state-list>

    </div>
</template>

<script>

import stateform from '../components/forms/stateform.vue';
import statelist from '../components/lists/statelist.vue';

export default {
    components:{
        'app-state':stateform,
        'app-state-list':statelist
    }
}
</script>

<style scoped>

</style>