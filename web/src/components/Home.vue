<template>
  <section id="hero">
    <div class="hero-container">
      <div class="wow fadeIn">
        <div class="hero-logo">
          <img class="" src="../assets/img/example-logo.png" alt="logo(si hubiera)">
        </div>

        <h1>Bienvenido</h1>
        <h2>Una plataforma de busqueda de empleo<span class="rotating">...</span></h2>
        <form @submit="onSubmit">
          <div class="actions row justify-content-around">
            <div class="col-md-4">
                <div class="form-group">
                  <input type="file" required @change="onFileSelected" class="form-control" accept=".pdf,.docx" name="cv" id="cv">
                  <label for="cv">Sube tu CV</label>
                </div>
            </div>
                  </div>
          <div v-if='mostrar' class="row justify-content-around">
            <div class="col-md-4">
                <div class="box">
                  <p>Subiste: {{nombredearchivo}}</p>
                </div>
            </div>
          </div>
          <div v-if='mostrar' class="row justify-content-around">
            <div class="col-md-4">
                <div class="submit-button">
                  <button type="submit" class="btn btn-danger">Recomiendame empleos!</button>
                </div>
            </div>
          </div>
        </form>
      </div>
    </div>
  </section>
  
</template>

<script>
import axios from 'axios'

export default {
  data (){
        return{
            // prueba:this.$route.params.prueba,
            form:{
                archive:null
            },
            mostrar:false,
            nombredearchivo:""
        }
           
    },
     methods:{
        onSubmit(evt){
            evt.preventDefault();
            const path = `http://localhost:8000/api/v1.0/prueba/`;
            axios.post(path,this.form,{ headers: {
                    'Content-Type': 'multipart/form-data'
                  }}).then((response) => {
                console.log(response.data);
                
                if(response.data.res == "ok"){
                  this.$router.push({name:'recomendation',params:{p:response.data.text}})
                }
                // location.href="/prueba/"
            }).catch((error)=>{
                console.log(error)
            });
            
        },
        onFileSelected(event){
              const file = event.target.files[0];
              console.log(file);
              this.nombredearchivo = file.name;
              this.mostrar = true;
               const formData = new FormData();
               formData.append("archive", file);
               this.form = formData;
               
        }

    },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
/* h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
} */
  /* @import './assets/css/style.css'; */
</style>
