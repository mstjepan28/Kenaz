<template>
<header>
	<Carousel
		v-if="articleList"
		:id="'newsCarousel'"
		:articleList="articleList.slice(0, 7)"
	/>
</header>

<div class="main">
	<main v-if="categoryList" class="main_content">
		<NewsSection :newsCategory="categoryList[0]" :contentPlacement="'1x3'"/>
		<NewsSection :newsCategory="categoryList[2]" :contentPlacement="'1x3'"/>

		<Banner />

		<NewsSection :newsCategory="categoryList[1]" :contentPlacement="'2x2'"/>
		
		<Banner />
	</main>

	<Sidebar/>
</div>

<Banner />

<Carousel
	v-if="articleList"
	class="only-home"

	:id="'imageCarousel'" 
	:articleList="articleList.slice(0, 7)" 
	:imagesOnly="true" 
	@openImgModal="openImgModal"
/>

</template>

<script>
import Carousel from "@/components/carousel.vue";
import NewsSection from "@/components/newsSection.vue";
import Banner from "@/components/banner.vue";
import Sidebar from "@/components/sidebar/sidebar.vue";

export default {
	name: 'Home',
	components: { Carousel, NewsSection, Banner, Sidebar },
	
	data(){
		return{
			categoryList: null,
			articleList: null
		}
	},
	mounted(){
		this.$store.dispatch("fetchArticleList");
		this.$store.dispatch('fetchCategoryList');

		this.categoryList = this.$store.state.categoryList;
		this.articleList = this.$store.getters.getArticles(7);
	}
}
</script>

<style lang="scss" scoped>
@import "@/styles/main.scss";

.main{
	display: flex;
	column-gap: 16px;
	.main_content{
		min-width: fit-content;

		& > *{
			margin-bottom: 16px;

			&:last-child{
				margin-bottom: 0px 
			}
		}
	}
}

</style>