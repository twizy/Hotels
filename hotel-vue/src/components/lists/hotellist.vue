<template>
    <div v-if="$store.state.allHotels.length > 0">

        <table class="table table-responsive mx-2">
            <thead>
                <tr>
                    <th colspan="4" scope="col">List of all hotel</th>
                </tr>
            </thead>

            <tbody>
                <tr :key="i.id" v-for="i in $store.state.allHotels">
                    <td>{{i.hotel}} - {{i.province}}</td>
                    <td>
                        <a class="btn btn-danger" @click.prevent="deleteHotel(i.id)">Delete</a>
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
        getHotel(){
            axios.get('http://localhost:8000/api/hotel/hotel-list/')
            .then(res=>{
                this.$store.state.allHotels = res.data
            })
            .catch(erro=>{
                console.log(error)
            })
        },
        deleteHotel(id){
            axios.delete(`http://localhost:8000/api/hotel/hotel-delete/${id}`)
            .then(res=>{
                this.getHotel()
            })
            .catch(erro=>{
                console.log(error)
            })
        }
    },
    created(){
        this.getHotel()
    }
}
</script>

<style scoped>

</style>

