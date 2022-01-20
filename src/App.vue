<template>
	<Navbar :categoryList="categoryList"/>

	<Banner :imgSrc="''"/>

	<NewsCarousel :newsList="newsList"/>

	<router-view/>
</template>

<script>
import Navbar from "@/components/navbar.vue";
import Banner from "./components/banner.vue";
import NewsCarousel from "./components/newsCarousel.vue";

export default {
	components: { Navbar, Banner, NewsCarousel },
	data(){
		return{
			categoryList: [
                { category: "NEWS", color: "#299EC3", newsList: [] },
                { category: "BUSINESS", color: "#EE6151", newsList: [] },
                { category: "SPORT", color: "#84C14F", newsList: [] },
                { category: "LIFE", color: "#5DCFF3", newsList: [] },
                { category: "TECH", color: "#FCC44D", newsList: [] },
                { category: "TRAVEL", color: "#A99765", newsList: [] },
            ],

			newsList: [
				{id: 1, title: "'1 item Margot' breathlessly reimagines Anne Fran's sister", date: 1642616107134, comments: 21,  imgURL: "https://images.unsplash.com/photo-1642425146609-6c8ff4589d18?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2832&q=80"},
				{id: 2, title: "'2 item Margot' breathlessly reimagines Anne Fran's sister", date: 1642616107134, comments: 22,  imgURL: "https://images.unsplash.com/photo-1642590044683-d72bfab9eb35?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2370&q=80"},
				{id: 3, title: "'3 item Margot' breathlessly reimagines Anne Fran's sister", date: 1642616107134, comments: 23,  imgURL: "https://images.unsplash.com/photo-1593642532842-98d0fd5ebc1a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2369&q=80"},
				{id: 4, title: "'4 item Margot' breathlessly reimagines Anne Fran's sister", date: 1642616107134, comments: 24,  imgURL: "https://images.unsplash.com/photo-1642548666500-7990b88e691f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2778&q=80"},
				{id: 5, title: "'5 item Margot' breathlessly reimagines Anne Fran's sister", date: 1642616107134, comments: 25,  imgURL: "https://images.unsplash.com/photo-1638913665258-ddd2bceafb30?ixlib=rb-1.2.1&ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2370&q=80"},
				{id: 6, title: "'6 item Margot' breathlessly reimagines Anne Fran's sister", date: 1642616107134, comments: 26,  imgURL: "https://images.unsplash.com/photo-1642524859252-448170eb1b11?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2369&q=80"},
			]
		}
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

</style>
