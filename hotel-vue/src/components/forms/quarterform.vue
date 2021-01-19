<template>

    <div class="mb-3 mx-2">
        <form action="">
            <input type="text" class="form-control" name="pro" v-model="$store.state.quaState.quarter" placeholder="Quarter"> <br>
            <select class="form-select" aria-label="Default select example" v-model="$store.state.quaState.state">
                <option :key="i.id" v-for="i in $store.state.allStates">{{i.state}}</option>
            </select> <br>
            <button class="btn btn-outline-primary" @click.prevent="addQuarter()">Add quarter</button>
        </form>
    </div>

</template>

<script>

import axios from 'axios'

export default {
    methods:{
        addQuarter(){
            const myForm={
                state:this.$store.state.quaState.state,
                quarter:this.$store.state.quaState.quarter
            }

            var checkExitingObject = this.$store.state.allQuarters.filter(function (elm){
                if (elm.state.toLowerCase() == myForm.state.toLowerCase() && 
                elm.quarter.toLowerCase() == myForm.quarter.toLowerCase())
                {
                    return elm; // returns length = 1 (object exists in array)
                }
            });

            if(checkExitingObject.length == 0){

            axios.post('http://localhost:8000/api/hotel/quarter-create/',myForm)
                .then(res=>{
                    this.getQuarter()
                })
                .catch(error=>console.error(error))
                .finally(
                    this.$store.state.quaState.state = "",
                    this.$store.state.quaState.quarter = "")

            }
            else if(checkExitingObject.length == 1){
                console.log("Quarter exists in that State")
            }
            else{
               console.log("Sorry put valid input") 
            }
 
        },
        getQuarter(){
            axios.get('http://localhost:8000/api/hotel/quarter-list/')
            .then(res=>{
                this.$store.state.allQuarters = res.data
            })
            .catch(erro=>{
                console.log(error)
            })

            axios.get('http://localhost:8000/api/hotel/state-list/')
            .then(res=>{
                this.$store.state.allStates = res.data
            })
            .catch(erro=>{
                console.log(error)
            })
        },
    },
    created(){
        this.getQuarter()
    }
    
}
</script>

<style scoped>

</style>