<template>
    <div class="container">
    <div class="row">
        <div class="col-md-12">
            <div class="section-title">
                <h3>Ofertas de empleo recomendadas</h3>
            </div>
        </div>
        <div class="col-md-4">
            <div class="post">
                <a class="post-img" href="blog-post.html"><img src="" alt=""></a>
                <div class="post-body">
                    <div class="post-meta">
                        <a class="post-category cat-1" href="category.html">Web Design</a>
                        <span class="post-date">March 27, 2018</span>
                    </div>
                    <h3 class="post-title"><a href="">Pagedraw UI Builder Turns Your Website Design Mockup Into Code Automatically</a></h3>
                </div>
            </div> 
        </div>
        <div class="col-md-4">
            <div class="post">
                <a class="post-img" href=""><img src="" alt=""></a>
                <div class="post-body">
                    <div class="post-meta">
                        <a class="post-category cat-2" href="">JavaScript</a>
                        <span class="post-date">March 27, 2018</span>
                    </div>
                    <h3 class="post-title"><a href="">Chrome Extension Protects Against JavaScript-Based CPU Side-Channel Attacks</a></h3>
                </div>
            </div>
        </div>
        <div class="col-md-4">
            <div class="post">
                <a class="post-img" href="blog-post.html"><img src="" alt=""></a>
                <div class="post-body">
                    <div class="post-meta">
                        <a class="post-category cat-3" href="">Jquery</a>
                        <span class="post-date">March 27, 2018</span>
                    </div>
                    <h3 class="post-title"><a href="">Ask HN: Does Anybody Still Use JQuery?</a></h3>
                </div>
            </div>
        </div>

        <div class="clearfix visible-md visible-lg"></div>

        <div class="col-md-4">
            <div class="post">
                <a class="post-img" href="blog-post.html"><img src="" alt=""></a>
                <div class="post-body">
                    <div class="post-meta">
                        <a class="post-category cat-2" href="category.html">JavaScript</a>
                        <span class="post-date">March 27, 2018</span>
                    </div>
                    <h3 class="post-title"><a href="">Why Node.js Is The Coolest Kid On The Backend Development Block!</a></h3>
                </div>
            </div>
        </div>
        <div class="col-md-4">
            <div class="post">
                <a class="post-img" href="blog-post.html"><img src="" alt=""></a>
                <div class="post-body">
                    <div class="post-meta">
                        <a class="post-category cat-4" href="category.html">Css</a>
                        <span class="post-date">March 27, 2018</span>
                    </div>
                    <h3 class="post-title"><a href="">CSS Float: A Tutorial</a></h3>
                </div>
            </div>
        </div>
        <div class="col-md-4">
            <div class="post">
                <a class="post-img" href="blog-post.html"><img src="" alt=""></a>
                <div class="post-body">
                    <div class="post-meta">
                        <a class="post-category cat-1" href="category.html">Web Design</a>
                        <span class="post-date">March 27, 2018</span>
                    </div>
                    <h3 class="post-title"><a href="">Tell-A-Tool: Guide To Web Design And Development Tools</a></h3>
                </div>
            </div>
        </div>
    </div>
    </div>
    
</template>

<script>
require('@/assets/css/recomendations.css')

export default {
    data(){
        return{
            lista:this.$route.params.p,
        }
        
    },
    methods:{

    },
    created(){
        console.log(this.lista);
        
    }
}
</script>

<style>

</style>