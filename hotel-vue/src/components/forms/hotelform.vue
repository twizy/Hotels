<template>

    <div class="mb-3 mx-2">
        <form action="" enctype="multipart/form-data">
            <input type="text" class="form-control" v-model="$store.state.quaState.hotel" placeholder="Hotel name"> <br>
            
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
          
            <input class="form-control form-control-md" id="formFileSm" type="file" @change="onfileselect()"> <br>

           
            
            <button class="btn btn-outline-primary" @click.prevent="addHotel">Add hotel</button>
        </form>
    </div>

</template>

<script>

import axios from 'axios'

export default {
    data(){
        return{
            selectfile:"",
        }
    },
    methods:{
        addHotel(){
            var datas = new FormData()

            datas.append('hotel', this.$store.state.quaState.hotel)
            datas.append('province', this.$store.state.quaState.province)
            datas.append('photo_outside', null)
            datas.append('photo_inside', null)
            datas.append('photo_room', this.selectfile) //it means this.selectfile will have event.target.files[0].
            datas.append('date', '2021-01-09')

            console.log(datas)
            // const myForm={
            //     hotel:this.$store.state.quaState.hotel,
            //     province:this.$store.state.quaState.province,
            //     photo_outside:null,
            //     photo_inside:null,
            //     photo_room:this.selectfile,
            //     date:'2021-01-09'
            // }

            // console.log(myForm)

            // var checkExitingObject = this.$store.state.allHotels.filter(function (elm){
            //     if (elm.hotel.toLowerCase() == myForm.hotel.toLowerCase() && 
            //     elm.province.toLowerCase() == myForm.province.toLowerCase())
            //     {
            //         return elm; // returns length = 1 (object exists in array)
            //     }
            // });

            // if(checkExitingObject.length == 0){





            axios.post('http://localhost:8000/api/hotel/hotel-create/',datas)
                .then(res=>{
                    this.getHotel()
                })
                .catch(error=>console.error(error))
                .finally(
                    this.$store.state.quaState.hotel = "",
                    this.$store.state.quaState.province = "",
                    this.$store.state.quaState.photo_outside = "",
                    this.$store.state.quaState.photo_inside = "",
                    this.$store.state.quaState.photo_room = "",
                    this.$store.state.quaState.date = "",)






            // }
            // else if(checkExitingObject.length == 1){
            //     console.log("Hotel exists")
            // }
            // else{
            //    console.log("Sorry put valid input") 
            // }

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
        onfileselect(){
            this.selectfile = event.target.files[0];
        }
    },
    created(){
        this.getHotel()
    }
    
}
</script>

<style scoped>

</style>