<template>
    <div v-if="$store.state.allStates.length > 0">

        <table class="table table-responsive mx-2">
            <thead>
                <tr>
                    <th colspan="4" scope="col">List of all state</th>
                </tr>
            </thead>

            <tbody>
                <tr :key="i.id" v-for="i in $store.state.allStates">
                    <td>{{i.state}} - {{i.province}}</td>
                    <td>
                        <a class="btn btn-danger" @click.prevent="deleteState(i.id)">Delete</a>
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
        getState(){
            axios.get('http://localhost:8000/api/hotel/state-list/')
            .then(res=>{
                this.$store.state.allStates = res.data
            })
            .catch(erro=>{
                console.log(error)
            })
        },
        deleteState(id){
            axios.delete(`http://localhost:8000/api/hotel/state-delete/${id}`)
            .then(res=>{
                this.getState()
            })
            .catch(erro=>{
                console.log(error)
            })
            
            
        }
        
    },created(){
        this.getState()
    }
}
</script>

<style scoped>

</style>

