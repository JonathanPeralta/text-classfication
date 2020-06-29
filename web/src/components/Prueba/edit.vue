<template>
  <div class="container">
      <div class="row">
          <div class="col-md-12">
              <h2>Editar</h2>
          </div>
      </div>
      <div class="row">
          <div class="col">
              <div class="card">
                  <div class="card-body">
                      <form @submit="onSubmit">
                          <div class="form-group row">
                                <label for="title" class="col-sm-2 col-form-label">
                                    Título
                                </label>
                                <div class="col-md-6">
                                    <input type="text" name="title" class="form-control" v-model.trim="form.title">
                                </div>
                          </div>
                           <div class="form-group row">
                                <label for="description" class="col-sm-2 col-form-label">
                                    Descripción
                                </label>
                                <div class="col-md-6">
                                    <textarea type="text" row="3" name="description" class="form-control"  v-model.trim="form.description"></textarea>
                                </div>
                          </div>
                          <div class="row">
                              <div class="col-text-left">
                                  <b-button type="submit" variant="primary">Editar</b-button>
                                  <b-button  variant="submit" class="btn-large-space btn-danger" :to="{name:'prueba'}">Cancelar</b-button>
                              </div>
                          </div>
                      </form>
                  </div>
              </div>
          </div>
      </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    data (){
        return{
            prueba:this.$route.params.prueba,
            form:{
                title:"",
                description:""
            }
        }
           
    },
     methods:{
        onSubmit(evt){
            evt.preventDefault();
            
            const path = `http://localhost:8000/api/v1.0/pruebas/${this.prueba}/`;
            axios.put(path,this.form).then((response) => {
                console.log(response);
                
                this.form.title = response.data.title;
                this.form.description = response.data.description;

            }).catch((error)=>{
                console.log(error)
            });
            
        },

        getPrueba(){
            const path = `http://localhost:8000/api/v1.0/pruebas/${this.prueba}/`;
            axios.get(path).then((response) => {
                console.log(response);
                
                this.form.title = response.data.title;
                this.form.description = response.data.description;

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