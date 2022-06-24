import App from './App.vue'
import { createApp } from 'vue'
import { createStore } from 'vuex'

const store = createStore({
    state() {
        return {
            recentSearch: '',
            number_of_searches: 0,
        }
    },
    mutations: {
        updateSearches(state, num) {
            state.number_of_searches+=num;
        }, 
        set_to_most_recent_search(state, newSearch) {
            state.recentSearch = newSearch;
        }
    },
    actions: {
        incementSearches(context) {
            context.commit('updateSearches', 1);
        },
        updateSearch(context, recent) {
            context.commit('set_to_most_recent_search', recent);
        }
    }
});

createApp(App).use(store)
.$mount("#app");