export default {
    namespaced: true,
    state () {
        return {
            modalImgURL: null,
        }
    },
    mutations: {
        setImgURL(state, imgURL){
            state.modalImgURL = imgURL
        }
    },
}