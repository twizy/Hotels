<template>
    <div v-if="$store.state.allProvinces.length > 0">

        <table class="table table-responsive mx-2">
            <thead>
                <tr>
                    <th colspan="4" scope="col">List of all provinces</th>
                </tr>
            </thead>

            <tbody>
                <tr :key="i.id" v-for="i in $store.state.allProvinces">
                    <td>{{i.province}}</td>
                    <td>
                        <a class="btn btn-danger" @click.prevent="deleteProvince(i.id)">Delete</a>
                    </td>
                    <td>
                        <a class="btn btn-secondary" @click.prevent="updateProvince(i.id)">
                            <router-link to="update-province">Update</router-link>
                        </a>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
import axios from 'axios';
import { EventBus } from '../../event-bus.js';

export default {
    
    methods:{
        getProvinceList(){
            axios.get('http://localhost:8000/api/hotel/province-list/')
            .then(res=>{
                this.$store.state.allProvinces = res.data
            })
            .catch(erro=>{
                console.log(error)
            })
        },
        deleteProvince(id){
            axios.delete(`http://localhost:8000/api/hotel/province-delete/${id}`)
            .then(res=>{
                this.getProvince()
            })
            .catch(erro=>{
                console.log(error)
            })
        },
        updateProvince(id){
            EventBus.$emit('updateValue', id)
            console.log(id)
        }
        
    },created(){
        this.getProvinceList()
    }
}
</script>

<style scoped>

</style>

