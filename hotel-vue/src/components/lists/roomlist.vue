<template>
    <div v-if="$store.state.allRooms.length > 0">

        <table class="table table-responsive mx-2">
            <thead>
                <tr>
                    <th colspan="4" scope="col">List of all rooms</th>
                </tr>
            </thead>

            <tbody>
                <tr :key="i.id" v-for="i in $store.state.allRooms">
                    <td>{{i.hotel}} <br> Type {{i.room}} <br> Room no {{i.room_number}} for {{i.price}} FBU</td>
                    <td>
                        <a class="btn btn-danger" @click.prevent="deleteRoom(i.id)">Delete</a>
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
        getRoom(){
            axios.get('http://localhost:8000/api/hotel/room-list/')
            .then(res=>{
                this.$store.state.allRooms = res.data
            })
            .catch(erro=>{
                console.log(error)
            })
        },
        deleteRoom(id){
            axios.delete(`http://localhost:8000/api/hotel/room-delete/${id}`)
            .then(res=>{
                this.getRoom()
            })
            .catch(erro=>{
                console.log(error)
            })
        }
        
    },created(){
        this.getRoom()
    }
}
</script>

<style scoped>

</style>

