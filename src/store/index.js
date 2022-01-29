import mockData from "../assets/data/mockData";

export default {
    state () {
        return {
            categoryList: null,
            articleList: null,
            authorList: null
        }
    },
    getters: {
        getAuthorById: (state, getters) => (authorId) => {
            return state.authorList.filter(author => author.id == authorId)[0]
        },
        getArticlesByCategory: (state, getters) => (category) => {
            category = category.toLowerCase();
            return state.articleList.filter(article => article.category == category)
        },
        getArticles: (state, getters) => (quantity) => {
            if(!state.articleList) return null;
            return state.articleList.slice(0, quantity);
        },
    },
    mutations: {
        setCategoryList(state, categoryList){
            state.categoryList = categoryList;
        },
        setArticleList(state, articleList){
            state.articleList = articleList;
        },
        setAuthorList(state, authorList){
            state.authorList = authorList;
        },
    },
    actions: {
        fetchCategoryList({ commit }){
            const categoryList = mockData.categoryList;
            commit('setCategoryList', categoryList);
        },
        fetchArticleList({ commit }){ 
            const articleList = mockData.articles;
            commit('setArticleList', articleList);
        },
        fetchAuthorList({ commit }){ 
            const authorList = mockData.authors;
            commit('setAuthorList', authorList);
        }
    }
}