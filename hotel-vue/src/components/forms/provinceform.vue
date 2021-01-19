<template>

    <div class="mb-3 mx-2">
        <form action="">
            <input type="text" class="form-control" name="pro" v-model="$store.state.proState.province" placeholder="Province"> <br>
            <button class="btn btn-outline-primary" @click.prevent="addProvince">
                Add province
            </button>

        </form>

        

    </div>

</template>

<script>

import axios from 'axios'

export default {
    methods:{
        addProvince(){
            const myForm={
                province:this.$store.state.proState.province
            }

            var checkExitingObject = this.$store.state.allProvinces.filter(function (elm){
                if (elm.province.toLowerCase() == myForm.province.toLowerCase())
                {
                return elm; // returns length = 1 (object exists in array)
                }
            });

            if(checkExitingObject.length == 0){

                axios.post('http://localhost:8000/api/hotel/province-create/',myForm)
                .then(res=>{
                    this.getProvince()
                })
                .catch(error=>console.error(error))
                .finally(this.$store.state.proState.province = "")

            }
            else if(checkExitingObject.length == 1){
                console.log("Province exists")
            }
            else{
               console.log("Sorry put valid input") 
            }

        },
        getProvince(){
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
        this.getProvince()
    }
    
}
</script>

<style scoped>

</style>