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

	<header>
		<Carousel
			v-if="articleList"
			:id="'newsCarousel'"
			:articleList="articleList.slice(0, 7)"
		/>
	</header>

	<div class="app_content">
		<router-view/>

		<aside class="app_content_sidebar">
			<SidebarContent/>
			<SocialMediaSection/>
			<!--
			<VideoPlayer :videoLink="'https://www.youtube.com/embed/QhqGCPMfkNM'"/> 
			-->

			<div class="bannerContainer">
				<Banner/>
				<Banner/>
			</div>
		</aside>
	</div>

	<Banner 
		v-if="curRoute == 'Home' || curRoute == 'Category'"
		class="only-home"
	/>
	<Carousel
		v-if="curRoute == 'Home' && articleList"
		class="only-home"

		:id="'imageCarousel'" 
		:articleList="articleList.slice(0, 7)" 
		:imagesOnly="true" 
		@openImgModal="openImgModal"
	/>
	
	<Footer />
</template>

<script>
import Modal from "@/components/modal.vue";
import Navbar from "@/components/navbar.vue";
import Banner from "./components/banner.vue";
import Carousel from "./components/carousel.vue";
import Footer from "./components/footer.vue";

import SocialMediaSection from "@/components/socialMediaSection.vue";
import SidebarContent from "@/components/sidebarContent.vue";
import VideoPlayer from "@/components/videoPlayer.vue";

export default {
	components: { Modal, Navbar, Banner, Carousel, SocialMediaSection, SidebarContent, VideoPlayer, Footer },
	data(){
		return{
			categoryList: null,
			articleList: null,
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

		this.$store.dispatch('fetchArticleList');
		this.articleList = this.$store.state.articleList; 
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
	
	display: flex;
	column-gap: 16px;

	& > .app_content_sidebar{
		& > .bannerContainer{
			display: flex;
			justify-content: space-between;

			padding: 20px;
			margin-top: 16px;

			background-color: $background-darker;

			& > .banner{
				width: 128px;
				height: 128px;

				margin: 0;
			}
		}
	}
}

.only-home{
	width: 100%;
	max-width: $content_width;
}
</style>
