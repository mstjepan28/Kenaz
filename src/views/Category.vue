<template>
<main class="main">

</main>


</template>

<script>
import NewsSection from "@/components/newsSection.vue";
import Banner from "@/components/banner.vue";

export default {
	name: 'Category',
	components: { NewsSection, Banner },
	
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
	},
}
</script>

<style lang="scss" scoped>
@import "@/styles/main.scss";
.main{
	min-width: fit-content;

	& > *{
		margin-bottom: 16px;

		&:last-child{
			margin-bottom: 0px 
		}
	}
}

</style>