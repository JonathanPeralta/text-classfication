<template>
  <div id="app">
    <router-view/>
    <!-- <Home/> -->
    <!-- <Footer/> -->
  </div>
</template>

<script>

import Footer from './components/Footer';
import Home from './components/Home';
import Recomendation from './components/Recomendation';

export default {
  name: 'App',
  components:{
    'Home':Home,
    'Footer':Footer,
    'Recomendation':Recomendation
  }
}
</script>

<style>
#app {
  /* font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50; */
  /* margin-top: 60px; */
}
</style>
