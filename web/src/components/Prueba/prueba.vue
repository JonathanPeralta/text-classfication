<template lang="html">
    <div class="container">
        <div class="row" >
            <div class="col-md-2">
                <h2>PRUEBAAA</h2>
            </div>
             <div class="col-md-12">
                <b-button size="sm" :to="{name:'nuevo'}" variant="primary">Agregar</b-button>
            </div>
            <div class="col-md-12">
                <b-table striped hover :items="books" :fields="fields">
                    <template v-slot:cell(action)="data">
                        <b-button size="sm" variant="primary" :to="{name:'editar',params:{prueba:data.item.id}}">
                            Editar
                        </b-button>
                        <b-button size="sm" variant="danger" :to="{name:'delete',params:{prueba:data.item.id}}">
                            Eliminar
                        </b-button>
                    </template>
                </b-table>
            </div>
        </div>
    </div>  
</template>

<script>
import axios from 'axios'

export default {
    data(){
        return {
            fields:[{key:'title',label:"Titulo"},
                    {key:'description',label:"Description"},
                    {key:'action',label:"Acción"}],
            books:[],
            
        }
    },
    methods:{
        getPrueba(){
            const path = 'http://localhost:8000/api/v1.0/pruebas/';
            axios.get(path).then((response) => {
                console.log(response);
                
                this.books = response.data
            }).catch((error)=>{
                console.log(error)
            });
        },
    },
    created(){
            // alert("ASD")
            this.getPrueba()
        }
}
</script>

<style>

</style>