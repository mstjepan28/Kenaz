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
        }
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