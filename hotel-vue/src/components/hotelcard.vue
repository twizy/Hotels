<template>
    <div class="row mx-2">

        <div class="card col-lg-3 col-sm-6 m-1" :key="i.id" v-for="i in filteredHotel">
            <img class="card-img-top">
            <div class="card-body">

                <h5 class="card-title">{{i.hotel}} hotel</h5>
                <p class="card-text">{{i.hotel}} is a good hotel placed in {{i.province}}. And it has more comfortable and profitable services</p>
                
                <a class="btn btn-secondary" @click.prevent="hotelDetails(i.id)">
                    <router-link to="hotel-details" class="text-white" >View hotel</router-link>
                </a>

            </div>
        </div>

    </div>
</template>

<script>

import axios from 'axios';
import { EventBus } from '../event-bus.js';

export default {
    data(){
        return{
            allhotelslist:[],
            searchedValue:''
        }
    },
    methods:{
        getHotel(){
            axios.get('http://localhost:8000/api/hotel/hotel-list/')
            .then(res=>{
                this.allhotelslist = res.data
            })
            .catch(erro=>{
                console.log(error)
            })
        },
        hotelDetails(id){
            EventBus.$emit('details',id)
        }
    },
    computed:{
        filteredHotel(){
            return this.allhotelslist.filter(item =>
            item.hotel.toLowerCase().includes(
                this.searchedValue.toLowerCase()
            )
            );
        }
    },
    created(){
        this.getHotel()
        EventBus.$on('searchvalue',(value) =>{
            this.searchedValue = value
        })
    },
}
</script>

<style scoped>
   
</style>
