<template>

    <div class="mb-3 mx-2">
        <form action="">
            <select class="form-select" aria-label="Default select example" v-model="$store.state.rooState.hotel">
                <option :key="i.id" v-for="i in $store.state.allHotels">{{i.name}}</option>
            </select> <br>
            <select class="form-select" aria-label="Default select example" v-model="$store.state.rooState.room">
                <option v-for="ii in $store.state.allHotelRooms">{{ii}}</option>
            </select> <br>
            <input type="number" class="form-control" name="pro" v-model="$store.state.rooState.room_number" placeholder="Room number"> <br>
            <input type="number" class="form-control" name="pro" v-model="$store.state.rooState.price" placeholder="Price"> <br>

            <button class="btn btn-outline-primary" @click.prevent="addRoom()">Add room</button>
        </form>
    </div>

</template>

<script>

import axios from 'axios'

export default {
    methods:{
        addRoom(){
            const myForm={
                hotel: this.$store.state.rooState.hotel,
                room: this.$store.state.rooState.room,
                room_number: this.$store.state.rooState.room_number,
                price: this.$store.state.rooState.price,
            }

            console.log(myForm)

            axios.post('http://localhost:8000/api/hotel/room-create/',myForm)
            .then(res=>{
                this.getRoom(),
                this.getHotel()
            })
            .catch(error=>console.error(error))
            .finally(
                this.$store.state.rooState.hotel = "",
                this.$store.state.rooState.room = "",
                this.$store.state.rooState.room_number = "",
                this.$store.state.rooState.price = "")
            
        },
        getRoom(){
            axios.get('http://localhost:8000/api/hotel/room-list/')
            .then(res=>{
                this.$store.state.allRooms = res.data
            })
            .catch(erro=>{
                console.log(error)
            })
        },
        getHotel(){
            axios.get('http://localhost:8000/api/hotel/hotel-list/')
            .then(res=>{
                this.$store.state.allHotels = res.data
            })
            .catch(erro=>{
                console.log(error)
            })
        },
    },
    created(){
        this.getRoom(),
        this.getHotel()
    }
    
}
</script>

<style scoped>

</style>