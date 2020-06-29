<template>
  <div class="container">
      <div class="row">
          <div class="col-md-12">
              <h2>Nuevo</h2>
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
                          <div class="form-group row">
                            <label class="btn btn-primary">
                                <i class="fa fa-folder-open-o" aria-hidden="true"></i>&nbsp;Seleccionar un archivo
                                <input type="file" accept=".pdf,.docx" required @change="onFileSelected" name="myfile">
                            </label>
                        </div>
                          <div class="row">
                              <div class="col-text-left">
                                  <b-button type="submit" variant="primary">Nuevo</b-button>
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
                // title:"",
                // description:"",
                archive:null
            }
        }
           
    },
     methods:{
        onSubmit(evt){
            evt.preventDefault();
            const path = `http://localhost:8000/api/v1.0/prueba/`;
            axios.post(path,this.form,{ headers: {
                    'Content-Type': 'multipart/form-data'
                  }}).then((response) => {
                console.log(response);
                // location.href="/prueba/"
            }).catch((error)=>{
                console.log(error)
            });
            
        },
        onFileSelected(event){
               const file = event.target.files[0];
               
               const formData = new FormData();
               formData.append("archive", file);
               this.form = formData;
               
        }

    },
    // created(){
        // this.getPrueba();
    // }
   
}
</script>

<style>

</style>