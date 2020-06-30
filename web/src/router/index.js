import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import prueba from '@/components/prueba/prueba'
import edit from '@/components/prueba/edit'
import eliminar from '@/components/prueba/delete'
import nuevo from '@/components/prueba/nuevo'
import VueResource from 'vue-resource';

Vue.use(VueResource);
Vue.use(Router)
// Vue.component('Footer', require('../components/Footer.vue')); 

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/prueba',
      name: 'prueba',
      component: prueba
    },
    {
      path: '/prueba/:prueba/editar',
      name: 'editar',
      component: edit
    },
    {
      path: '/prueba/:prueba/eliminar',
      name: 'delete',
      component: eliminar
    },
    {
      path: '/prueba/nuevo',
      name: 'nuevo',
      component: nuevo
    }
  ],
  mode:'history'
})
