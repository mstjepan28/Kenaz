<template>
	<Modal 
		:id="'imgModal'" 
		ref="imageModal"
	/>

	<Navbar
		v-if="categoryList"
		:categoryList="categoryList"
	/>

	<Banner/>

	<div class="app_content">
		<router-view/>
	</div>

	<Footer />
</template>

<script>
import Modal from "@/components/modal.vue";
import Banner from "./components/banner.vue";
import Footer from "./components/footer.vue";
import Navbar from "@/components/navbar/navbar.vue";

export default {
	components: { Modal, Navbar, Banner, Footer },
	data(){
		return{
			categoryList: null,
		}
	},
	computed:{
		curRoute(){
			return this.$route.name;
		}
	},
	methods:{
		openImgModal(imgURL){
			this.$refs.imageModal.openWithImg(imgURL)
		}
	},
	mounted(){
		this.$store.dispatch('fetchCategoryList');
		this.categoryList = this.$store.state.categoryList;
	}
}

</script>

<style lang="scss">
@import "@/styles/main.scss";

#app{
	width: 100%;
	min-height: 100vh;

	display: flex;
	flex-direction: column;
	align-items: center;

	background-color: $background;
}

.app_content{
	width: 100%;
	max-width: $content_width;
}

</style>
