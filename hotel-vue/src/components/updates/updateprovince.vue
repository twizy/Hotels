<template>

    <div class="mb-3 mx-2">
        <form action="">
            <input type="text" class="form-control" name="pro" v-model="gotProvince" placeholder="Province"> <br>
            <button class="btn btn-outline-primary" @click.prevent="updateProvince">Update</button>
        </form>
    </div>

</template>

<script>

import axios from 'axios';
import { EventBus } from '../../event-bus.js';

export default {
    data(){
        return{
            gotId:'',
            gotProvince:''
        }
    },
    methods:{
        updateProvince(){
            const myForm={
                id:this.gotId,
                province:this.gotProvince
            }

            console.error(myForm)

            axios.put(`http://localhost:8000/api/hotel/province-update/${this.gotId}`,myForm)
            .then(res=>{
                console.error(res)
            })
            .catch(error=>console.error(error))
            // .finally(this.gotProvince = "")
            
        },
        getProvince(){
            axios.get(`http://localhost:8000/api/hotel/province-details/${this.gotId}`)
            .then(res=>{
                this.gotProvince = res.data.province
            })
            .catch(erro=>{
                console.log(error)
            })
        },
    },
    created(){
        EventBus.$on('updateValue',id =>{
            this.gotId = id
            this.getProvince()
        });
    }
    
}
</script>

<style scoped>

</style>