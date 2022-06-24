<template>

</template>


<script>

export default {
    name: 'searchBar',
    data: () {
        return {
            allSearches = [],
            currentSearchKeyword = "",
            autocomplete = false,
            resultsOfCurrentSearch = [],
        }
    },
    computed: {
        setRecentSearch() {
            this.$store.dispatch('updateSearch', this.currentSearchKeyword);
        },
        setAutocomplete() {
            if (autocomplete) {
                autocomplete = false;
            }
            else {
                autocomplete = true;
            }
        },
    },
    methods: {
        insertToHistory() {
            allSearches.push(this.currentSearchKeyword);
        },
        filterResultsByNetwork(keyword) {
            
        },
        filterResultsByKeyword(keyword) {

        }
        getAllResults() {
            fetch('', {method: 'GET', headers: {'content-type': 'application/json'},})
            .then(results => 
                results.json()
            )
            .then(allResults => {
                for (int i = 0; i < allResults.length; ++i) {
                    this.resultsOfCurrentSearch.push(allResults[i]);
                }
            })
            .catch(err => {console.log(err); });
        }
    }

};
</script>