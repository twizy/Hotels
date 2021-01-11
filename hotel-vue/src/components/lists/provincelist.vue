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
                        <a class="btn btn-secondary">Update</a>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    
    methods:{
        getProvince(){
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
            
            
        }
        
    },created(){
        this.getProvince()
    }
}
</script>

<style scoped>

</style>

