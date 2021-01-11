<template>
    <div v-if="$store.state.allReservations.length > 0">

        <table class="table table-responsive mx-2">
            <thead>
                <tr>
                    <th colspan="4" scope="col">List of all reservation</th>
                </tr>
            </thead>

            <tbody>
                <tr :key="i.id" v-for="i in $store.state.allReservations">
                    <td>{{i.province}}</td>
                    <td>
                        <a class="btn btn-danger" @click.prevent="deleteReservation(i.id)">Delete</a>
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
        getReservation(){
            axios.get('http://localhost:8000/api/hotel/reservation-list/')
            .then(res=>{
                this.$store.state.allReservations = res.data
            })
            .catch(erro=>{
                console.log(error)
            })
        },
        deleteReservation(id){
            axios.delete(`http://localhost:8000/api/hotel/reservation-delete/${id}`)
            .then(res=>{
                this.getReservation()
            })
            .catch(erro=>{
                console.log(error)
            })
            
            
        }
        
    },created(){
        this.getReservation()
    }
}
</script>

<style scoped>

</style>

