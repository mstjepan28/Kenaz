<template>
	<main class="main">
		<NewsSection :newsCategory="categoryList[0]"/>
	</main>
</template>

<script>
import NewsSection from "@/components/newsSection.vue"

export default {
	name: 'Home',
	components: { NewsSection },
	
	data(){
		return{
			categoryList: [
                { category: "NEWS", color: "#299EC3", newsList: [] },
                { category: "BUSINESS", color: "#EE6151", newsList: [] },
                { category: "SPORT", color: "#84C14F", newsList: [] },
                { category: "LIFE", color: "#5DCFF3", newsList: [] },
                { category: "TECH", color: "#FCC44D", newsList: [] },
                { category: "TRAVEL", color: "#A99765", newsList: [] },
            ]
		}
	}
}
</script>

<style lang="scss" scoped>
@import "@/styles/main.scss";
.main{
	max-width: $content_width;
}

</style>