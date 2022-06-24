<template>
    <div class="card">
        <img class="card-img-top" src={{thumbnail}} />
        <div class="card-body">
            <h1 class="card-title">{{title}}</h1>
            <h3 class="card-title">From {{source}}</h3>
            <p class="card-text">{{summary}}</p>
        </div>
    </div>
</template>


<script>
    export default {
         name: 'article',
         props: {
             entry: Object, 
         },
         components: {
             articlePage
         },
         data: () {
            return {
                title: "",
                source: "",
                keywords: [],
                summary: "",
                full_text: "",
                url: "",
                date: "",
                thumbnail: "",
                images: [],
                movies: [],
            }
         },
         mounted: {
             initArticle() {
                 title = entry.title;
                 source = entry.source;
                 url = entry.link;
                 date = entry.date;
                 thumbnail = entry.thumbnail;
                 keywords = entry.keywords;
                 summary = entry.summary;
                 full_text = entry.text;
                 if (entry.images != null) {
                     images = entry.images;
                 }
                 if (entry.movies != null) {
                     movies = entry.movies;
                 }
             },
         },
         methods: {

         },
    };
</script>


<style>

</style>