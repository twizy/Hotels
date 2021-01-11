<template>
    <div v-if="$store.state.allQuarters.length > 0">

        <table class="table table-responsive mx-2">
            <thead>
                <tr>
                    <th colspan="4" scope="col">List of all quarter</th>
                </tr>
            </thead>

            <tbody>
                <tr :key="i.id" v-for="i in $store.state.allQuarters">
                    <td>{{i.quarter}} - {{i.state}}</td>
                    <td>
                        <a class="btn btn-danger" @click.prevent="deleteQuarter(i.id)">Delete</a>
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
        getQuarter(){
            axios.get('http://localhost:8000/api/hotel/quarter-list/')
            .then(res=>{
                this.$store.state.allQuarters = res.data
            })
            .catch(erro=>{
                console.log(error)
            })
        },
        deleteQuarter(id){
            axios.delete(`http://localhost:8000/api/hotel/quarter-delete/${id}`)
            .then(res=>{
                this.getQuarter()
            })
            .catch(erro=>{
                console.log(error)
            })
            
            
        }
        
    },created(){
        this.getQuarter()
    }
}
</script>

<style scoped>

</style>

