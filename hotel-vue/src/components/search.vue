<template>
    <div>
        <form class="d-flex">
            <input @keyup.prevent="searching()" class="form-control me-2" type="search" placeholder="Search" aria-label="Search" v-model="value">
        </form>
    </div>
</template>

<script>

import { EventBus } from '../event-bus.js';

export default {
    data(){
        return{
            value:''
        }
    },
    methods:{
        searching(){
            EventBus.$emit('searchvalue', this.value)
            // console.log(this.value)
        }
    }
}
</script>

<style scoped>
   
</style>
