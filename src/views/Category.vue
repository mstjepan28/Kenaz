<template>
<main class="main">
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
			newsList: [
				{id: 1, title: "1 item Margot' breathlessly reimagines Anne Fran's sister", author:"John Smith", date: 1642616107134, comments: 21,  imgURL: "https://images.unsplash.com/photo-1642425146609-6c8ff4589d18?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2832&q=80"},
				{id: 2, title: "2 item Margot' breathlessly reimagines Anne Fran's sister", author:"John Smith", date: 1642616107134, comments: 22,  imgURL: "https://images.unsplash.com/photo-1642590044683-d72bfab9eb35?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2370&q=80"},
				{id: 3, title: "3 item Margot' breathlessly reimagines Anne Fran's sister", author:"John Smith", date: 1642616107134, comments: 23,  imgURL: "https://images.unsplash.com/photo-1593642532842-98d0fd5ebc1a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2369&q=80"},
				{id: 4, title: "4 item Margot' breathlessly reimagines Anne Fran's sister", author:"John Smith", date: 1642616107134, comments: 24,  imgURL: "https://images.unsplash.com/photo-1642548666500-7990b88e691f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2778&q=80"},
				{id: 5, title: "5 item Margot' breathlessly reimagines Anne Fran's sister", author:"John Smith", date: 1642616107134, comments: 25,  imgURL: "https://images.unsplash.com/photo-1638913665258-ddd2bceafb30?ixlib=rb-1.2.1&ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2370&q=80"},
				{id: 6, title: "6 item Margot' breathlessly reimagines Anne Fran's sister", author:"John Smith", date: 1642616107134, comments: 26,  imgURL: "https://images.unsplash.com/photo-1642524859252-448170eb1b11?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2369&q=80"},
				{id: 7, title: "7 item Margot' breathlessly reimagines Anne Fran's sister", author:"John Smith", date: 1642616107134, comments: 27,  imgURL: "https://images.unsplash.com/photo-1643061476185-46e56973b5b5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1775&q=80"},
				{id: 8, title: "8 item Margot' breathlessly reimagines Anne Fran's sister", author:"John Smith", date: 1642616107134, comments: 23,  imgURL: "https://images.unsplash.com/photo-1593642532842-98d0fd5ebc1a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2369&q=80"},
				{id: 9, title: "9 item Margot' breathlessly reimagines Anne Fran's sister", author:"John Smith", date: 1642616107134, comments: 24,  imgURL: "https://images.unsplash.com/photo-1642548666500-7990b88e691f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2778&q=80"},
				{id: 10, title: "10 item Margot' breathlessly reimagines Anne Fran's sister", author:"John Smith", date: 1642616107134, comments: 25,  imgURL: "https://images.unsplash.com/photo-1638913665258-ddd2bceafb30?ixlib=rb-1.2.1&ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2370&q=80"},
				{id: 11, title: "11 item Margot' breathlessly reimagines Anne Fran's sister", author:"John Smith", date: 1642616107134, comments: 26,  imgURL: "https://images.unsplash.com/photo-1642524859252-448170eb1b11?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2369&q=80"},
				{id: 12, title: "12 item Margot' breathlessly reimagines Anne Fran's sister", author:"John Smith", date: 1642616107134, comments: 27,  imgURL: "https://images.unsplash.com/photo-1643061476185-46e56973b5b5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1775&q=80"},
				{id: 13, title: "13 item Margot' breathlessly reimagines Anne Fran's sister", author:"John Smith", date: 1642616107134, comments: 27,  imgURL: "https://images.unsplash.com/photo-1643061476185-46e56973b5b5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1775&q=80"},
			],

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