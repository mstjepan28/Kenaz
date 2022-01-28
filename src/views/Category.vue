<template>
<main v-if="newsList" class="main">
	<h2 class="categoryTitle">{{curCategory}}</h2>
	<CategoryNewsCard :key="news.id" :news="news" v-for="news in curPageContent"/>
	<Pagination :totalPages="totalPages" @changePage="setPage"/>
</main>
</template>

<script>
import CategoryNewsCard from "@/components/categoryNewsCard.vue";
import Pagination from "@/components/pagination.vue";

export default {
	name: 'Category',
	components: { CategoryNewsCard, Pagination },
	
	data(){
		return{
			newsList: null,

			page: 1,
			itemPerPage: 6
		}
	},
	computed:{
		curPageContent(){
			const end = this.page * this.itemPerPage; 
			const start = end - this.itemPerPage;
			
			return this.newsList.slice(start, end);
		},
		totalPages(){
			return Math.ceil(this.newsList.length / this.itemPerPage);
		},
		curCategory(){
			const curCategory = this.$route.params.id;
			return curCategory.charAt(0).toUpperCase() + curCategory.slice(1);
		}
	},
	methods: {
		setPage(newPage){
			this.page = newPage;
		}
	},
	mounted(){
		this.newsList = this.$store.state.newsList
	}
}
</script>

<style lang="scss" scoped>
@import "@/styles/main.scss";
.main{
	min-width: fit-content;

	display: flex;
	flex-direction: column;

	background-color: white;

	& > .categoryTitle{
		@include fontStyle($bitter, 24px, bold, 28px, #363F48);
		padding: 16px 0 0 32px;
	}
}

</style>