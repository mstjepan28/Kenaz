import data from "../assets/data";

export default {
    state () {
        return {
            categoryList: [],
            newsList: []
        }
    },
    getters: {
        getCategoryList(state){
            return state.categoryList
        }
    },
    mutations: {
        setCategoryList(state, categoryList){
            state.categoryList = categoryList;
        },
        setNewsList(state, newsList){
            state.newsList = newsList;
        }
    },
    actions: {
        fetchCategoryList({ commit }){
            const categoryList = data.categoryList;
            commit('setCategoryList', categoryList);
        },
        fetchNewsList({ commit }){ 
            const newsList = data.newsList;
            commit('setNewsList', newsList);
        }
    }
}