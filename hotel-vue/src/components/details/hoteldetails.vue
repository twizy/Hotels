<template>
    <div>

        <div class="jumbotron jumbotron-fluid">
            <div class="container">
                <h1 class="display-4">{{$store.state.fullDetailState.hotel}}</h1>
                <p class="lead">This is a modified jumbotron that occupies the entire horizontal space of its parent.</p>
            </div>
        </div>

        <div class="card-group">
            <div class="card m-2">
                <img class="card-img-top" src="" >
                <div class="card-body">
                <h5 class="card-title">Outside</h5>
                <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                </div>
            </div>

            <div class="card m-2">
                <img class="card-img-top" src="" >
                <div class="card-body">
                <h5 class="card-title">Inside</h5>
                <p class="card-text">Started in : {{$store.state.fullDetailState.date}}</p>
                </div>
            </div>

        </div>

        <div>

        <table class="table table-responsive mx-2">
            <thead>
                <tr>
                    <th scope="col">Room No</th>
                    <th scope="col">Type</th>
                    <th scope="col">Price</th>
                    <th scope="col">Duration</th>
                </tr>
            </thead>

            <!-- I will fix very soon the mix of v-if and v-for -->
            <!-- <tbody>
                <tr :key="r.id" v-for="r in hotelRooms" v-if="r.hotel == $store.state.fullDetailState.hotel">
                    <td>{{r.room_number}}</td>
                    <td>{{r.room}}</td>
                    <td>{{r.price}}</td>
                    <td>1 day</td>
                </tr>
            </tbody> -->

            <tbody>
                <tr :key="r.id" v-for="r in hotelRooms" v-if="r.hotel == $store.state.fullDetailState.hotel">
                    <td>{{r.room_number}}</td>
                    <td>{{r.room}}</td>
                    <td>{{r.price}}</td>
                    <td>1 day</td>
                </tr>
            </tbody>
            
        </table>

        </div>
 
    </div>
</template>

<script>
import axios from 'axios';
import { EventBus } from '../../event-bus.js';

export default {
    data(){
        return{
            fullDetails:{
                gotId:'',
                hotel:'',
                province:'',
                date:''
            },
            hotelRooms:[]
        }
    },
    methods:{
        getHotelDetails(){
            axios.get(`http://localhost:8000/api/hotel/hotel-details/${this.fullDetails.gotId}`)
                .then(res=>{
                    this.$store.state.fullDetailState.hotel = res.data.hotel
                    this.$store.state.fullDetailState.province = res.data.province
                    this.$store.state.fullDetailState.date = res.data.date
                    this.getHotelRooms()
                })
                .catch(erro=>{
                    console.log(error)
            })
        },
        getHotelRooms(){
            axios.get('http://localhost:8000/api/hotel/room-list/')
                .then(res=>{
                    this.hotelRooms = res.data
                })
                .catch(erro=>{
                    console.log(error)
            })
        }
    },
    created(){
        
        EventBus.$on('details',id =>{
            this.fullDetails.gotId = id
            this.getHotelDetails()
        })
        
    },
    mounted () {
       this.findItems()
    }
}
</script>

<style scoped>

</style>