<template>
    <div id="app">

    </div>
</template>

<script>
    import searchBar from './components/searchBar.vue';
    import article from './components/article.vue';

    import store from 'main.js'

    export default {
        name: 'app',
        components: { searchBar, article},
        data: () {
            return {
                header: 'Available News Article Results',
                error: 'No Available Search Results',
            }
        },
        computed: {
            updateNumberOfSearches() {
                this.$store.dispatch('incrementSearches');
            }
        }
    }

</script>

<style>

</style>