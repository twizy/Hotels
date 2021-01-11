<template>

    <div class="mb-3 mx-2">
        <form action="">
            <input type="text" class="form-control" v-model="$store.state.quaState.name" placeholder="Hotel name"> <br>
            
            <select class="form-select" aria-label="Default select example" v-model="$store.state.quaState.province">
                <option :key="i.id" v-for="i in $store.state.allProvinces">{{i.province}}</option>
            </select> <br>

            <input class="form-control form-control-md" id="formFileSm" type="file"> <br>
           
            <!-- <input type="file", @change="processFile($event)">

                methods: {
                processFile(event) {
                this.someData = event.target.files[0]
                }
                
            } -->

            <input class="form-control form-control-md" id="formFileSm" type="file"> <br>
          
            <input class="form-control form-control-md" id="formFileSm" type="file"> <br>
            
            <button class="btn btn-outline-primary" @click.prevent="addHotel">Add hotel</button>
        </form>
    </div>

</template>

<script>

import axios from 'axios'

export default {
    methods:{
        addHotel(){
            const myForm={
                name:this.$store.state.quaState.name,
                province:this.$store.state.quaState.province,
                photo_outside:null,
                photo_inside:null,
                photo_room:null,
                date:'2021-01-09'
            }

            console.log(myForm)

            axios.post('http://localhost:8000/api/hotel/hotel-create/',myForm)
            .then(res=>{
                this.getHotel()
            })
            .catch(error=>console.error(error))
            .finally(
                this.$store.state.quaState.name = "",
                this.$store.state.quaState.province = "",
                this.$store.state.quaState.photo_outside = "",
                this.$store.state.quaState.photo_inside = "",
                this.$store.state.quaState.photo_room = "",
                this.$store.state.quaState.date = "",)
            
        },
        getHotel(){
            axios.get('http://localhost:8000/api/hotel/hotel-list/')
            .then(res=>{
                this.$store.state.allHotels = res.data
            })
            .catch(erro=>{
                console.log(error)
            })

            axios.get('http://localhost:8000/api/hotel/province-list/')
            .then(res=>{
                this.$store.state.allProvinces = res.data
            })
            .catch(erro=>{
                console.log(error)
            })
        },
    },
    created(){
        this.getHotel()
    }
    
}
</script>

<style scoped>

</style>