<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Hotel</a>
            
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <router-link to="/">Home</router-link>
                    </li>

                    <li class="nav-item">
                        <router-link to="/hotel">Hotels</router-link>
                    </li>

                    <li class="nav-item">
                        <router-link to="/province">Provinces</router-link>
                    </li>

                    <li class="nav-item">
                        <router-link to="/state">States</router-link>
                    </li>

                    <li class="nav-item">
                        <router-link to="/quarter">Quartes</router-link>
                    </li>

                    <li class="nav-item">
                        <router-link to="/room">Rooms</router-link>
                    </li>

                    <li class="nav-item">
                        <router-link to="/reservation">Reservations</router-link>
                    </li>
                </ul>

                <app-search></app-search>
                
            </div>
        </div>
    </nav>
</template>


<script>

import search from './search.vue';

export default {
    components:{
        'app-search':search
    }
}
</script>

<style scoped>

</style>