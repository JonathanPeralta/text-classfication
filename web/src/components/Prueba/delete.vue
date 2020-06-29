<template>
  <div class="container">
      <div class="row">
          <div class="col-md-12">
              <h3>Borrar esta wea</h3>
                <p>Title : {{this.element.title}}</p>
                <p>Description : {{this.element.description}}</p>
          </div>
          <div class="col-md-12">
              <b-button v-on:click="eliminar" variant="danger">
                  Eliminar
              </b-button>
          </div>
      </div>
  </div>
</template>

<script>
import axios from 'axios'


export default {
    
    data()
    {
        return{
            prueba:this.$route.params.prueba,
            element:{
                title:"",
                description:""
            }
        }
    },
    methods:{
        getPrueba(){
              const path = `http://localhost:8000/api/v1.0/pruebas/${this.prueba}/`;
                axios.get(path).then((response) => {
                    console.log(response);
                    
                    this.element.title = response.data.title;
                    this.element.description = response.data.description;

                }).catch((error)=>{
                    console.log(error)
                });
        },

        eliminar(){

            const path = `http://localhost:8000/api/v1.0/pruebas/${this.prueba}/`;
                axios.delete(path).then((response) => {
                  location.href="/prueba"

                }).catch((error)=>{
                    console.log(error)
                });

        }
    },
    created(){
        this.getPrueba();
    }
}
</script>

<style>

</style>