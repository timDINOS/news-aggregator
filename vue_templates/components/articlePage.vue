<template>
    <head>
        <title>{{title}}</title>
    </head>
    <body>
    </body>
</template>



<script>

export default {
    name: 'articlePage',
    props: {
        title: String,
        source: String,
        full_text: String,
        images: {
            type: Array
        },
        movies: {
            type: Array
        },
        link: ""
    },
    data: () {
        return {
            articleTitle: "",
            articleSource: "",
            articleText: "",
            articleImages: [],
            articleMovies: [],
            articleLink: "",
        }
    },
    mounted: {
        initPage() {
            articleTitle = title;
            articleSource = source;
            articleText = full_text;
            articleLink = link;
            if (images != null) {
                articleImages = images;
            }
            if (movies != null) {
                articleMovies = movies;
            }
        }
    }
};

</script>


<style>


</style>
