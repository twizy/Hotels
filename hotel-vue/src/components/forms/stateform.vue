<template>

    <div class="mb-3 mx-2">
        <form action="">
            <input type="text" class="form-control" name="pro" v-model="$store.state.staState.state" placeholder="State"> <br>
            <select class="form-select" aria-label="Default select example" v-model="$store.state.staState.province">
                <option :key="i.id" v-for="i in $store.state.allProvinces">{{i.province}}</option>
            </select> <br>
            <button class="btn btn-outline-primary" @click.prevent="addState">Add state</button>
        </form>
    </div>

</template>

<script>

import axios from 'axios'

export default {
    methods:{
        addState(){
            const myForm={
                state:this.$store.state.staState.state,
                province:this.$store.state.staState.province
            }

            var checkExitingObject = this.$store.state.allStates.filter(function (elm){
                if (elm.state.toLowerCase() == myForm.state.toLowerCase() && 
                elm.province.toLowerCase() == myForm.province.toLowerCase())
                {
                    return elm; // returns length = 1 (object exists in array)
                }
            });

            if(checkExitingObject.length == 0){

                axios.post('http://localhost:8000/api/hotel/state-create/',myForm)
                .then(res=>{
                    this.getState()
                })
                .catch(error=>console.error(error))
                .finally(
                    this.$store.state.staState.state = "",
                    this.$store.state.staState.province = "")

            }
            else if(checkExitingObject.length == 1){
                console.log("State exists in that Province")
            }
            else{
               console.log("Sorry put valid input") 
            }
            
        },
        getState(){
            axios.get('http://localhost:8000/api/hotel/state-list/')
            .then(res=>{
                this.$store.state.allStates = res.data
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
        this.getState()
    }
    
}
</script>

<style scoped>

</style>