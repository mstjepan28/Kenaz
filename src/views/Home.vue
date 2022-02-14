<template>
<header>
	<Carousel
		v-if="articleList"
		:id="'mainCarousel'"
		:articleList="articleList.slice(0, 7)"
	/>
</header>

<div class="main">
	<main v-if="categoryList" class="main_content">
		<NewsSection :newsCategory="categoryList[0]" contentPlacement="1x3"/>
		<NewsSection :newsCategory="categoryList[2]" contentPlacement="1x3"/>

		<Banner />

		<NewsSection :newsCategory="categoryList[1]" contentPlacement="2x2"/>
		
		<Banner style="margin: 17px 0 27px 0"/>

		<NewsSectionCarousel
			id="newsCarousel"
			:newsCategory="{category: 'News Carousel', color: '#FCC44D'}" 
			:articleList="articleList.slice(0, 7)"
		/>

		<div class="carouselGrouping">
			<NewsSectionCarousel
				id="editorials"
				contentPlacement="1x1"
				:newsCategory="{category: 'Editorials', color: '#A99765'}" 
				:articleList="articleList.slice(0, 7)"
			/>
			<NewsSectionCarousel
				id="localNews"
				contentPlacement="1x1"
				:newsCategory="{category: 'Local news', color: '#A99765'}" 
				:articleList="articleList.slice(0, 7)"
			/>
		</div>
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
/>

</template>

<script>
import Carousel from "@/components/carousel.vue";
import NewsSection from "@/components/newsSection.vue";
import NewsSectionCarousel from "@/components/newsSectionCarousel.vue";
import Banner from "@/components/banner.vue";
import Sidebar from "@/components/sidebar/sidebar.vue";

export default {
	name: 'Home',
	components: { Carousel, NewsSection, NewsSectionCarousel, Banner, Sidebar },
	
	data(){
		return{
			categoryList: null,
			articleList: null
		}
	},
	mounted(){
		this.$store.dispatch("fetchArticleList");
		this.$store.dispatch('fetchCategoryList');

		this.categoryList = this.$store.state.dataStore.categoryList;
		this.articleList = this.$store.getters.getArticles(7);
	}
}
</script>

<style lang="scss" scoped>
@import "@/styles/main.scss";

.main{
	display: flex;
	justify-content: space-between;
	.main_content{
		min-width: fit-content;

		*{
			margin-bottom: 16px;

			&:last-child{
				margin-bottom: 0px 
			}
		}

		.carouselGrouping{
			display: flex;
			justify-content: space-between;

		}
	}
}

</style>