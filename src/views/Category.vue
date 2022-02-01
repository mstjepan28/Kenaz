<template>
<header>
	<Carousel
		v-if="articleList"
		:id="'newsCarousel'"
		:articleList="articleList.slice(0, 7)"
	/>
</header>

<div class="main">
	<main v-if="articleList" class="main_content">
		<h2 class="categoryTitle">{{curCategory}}</h2>

		<categoryArticleCard :key="news.id" :news="news" v-for="news in curPageContent"/>
		<Pagination :totalPages="totalPages" ref="pagination" @changePage="setPage"/>

	</main>

	<Sidebar/>
</div>

<Banner class="banner_bottom"/>

</template>

<script>
import Carousel from "@/components/carousel.vue";
import Banner from "@/components/banner.vue";
import Sidebar from "@/components/sidebar/sidebar.vue";

import categoryArticleCard from "@/components/cards/categoryArticleCard.vue";
import Pagination from "@/components/pagination.vue";

export default {
	name: 'Category',
	components: { Carousel, Banner, Sidebar, categoryArticleCard, Pagination },
	
	data(){
		return{
			articleList: null,

			page: 1,
			itemPerPage: 6
		}
	},
	computed:{
		curPageContent(){
			const end = this.page * this.itemPerPage; 
			const start = end - this.itemPerPage;
			
			return this.articleList.slice(start, end);
		},
		totalPages(){
			return Math.ceil(this.articleList.length / this.itemPerPage);
		},
		curCategory(){
			const curCategory = this.$route.params.id;
			if(!curCategory) return "";

			return curCategory.charAt(0).toUpperCase() + curCategory.slice(1);
		}
	},
	methods: {
		setPage(newPage){
			this.page = newPage;
		},
		setCategoryContent(){
			this.page = 1;
			this.$refs.pagination?.setPage(this.page);

			this.$store.dispatch("fetchArticleList");
			this.articleList = this.$store.getters.getArticlesByCategory(this.curCategory);	
		}
	},
	mounted(){
		this.setCategoryContent();
	},
	watch:{
		curCategory(){
			this.setCategoryContent();
		}
	}
}
</script>

<style lang="scss" scoped>
@import "@/styles/main.scss";
.main{
	display: flex;
	column-gap: 16px;
	
	& > .main_content{
		min-width: fit-content;

		display: flex;
		flex-direction: column;

		background-color: white;

		& > .categoryTitle{
			@include fontStyle($bitter, 24px, bold, 28px, #363F48);
			padding: 16px 0 0 32px;
		}
	}
}

.banner_bottom{
	max-width: 620px;
}
</style>