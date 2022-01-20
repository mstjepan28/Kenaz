<template>
<div class="home">
	<main class="home_content">
		<NewsSection :newsCategory="categoryList[0]" :contentPlacement="'1x3'"/>
		<NewsSection :newsCategory="categoryList[2]" :contentPlacement="'1x3'"/>

		<Banner />

		<NewsSection :newsCategory="categoryList[1]" :contentPlacement="'2x2'"/>
		
		<Banner />
	</main>
	
	<aside class="home_sidebar">
		<SidebarContent/>
		<SocialMediaSection/>
	</aside>

</div>

<Banner />
</template>

<script>
import NewsSection from "@/components/newsSection.vue";
import Banner from "@/components/banner.vue";
import SocialMediaSection from "@/components/socialMediaSection.vue";
import SidebarContent from "@/components/sidebarContent.vue";

export default {
	name: 'Home',
	components: { NewsSection, Banner, SocialMediaSection, SidebarContent },
	
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
.home{
	width: 100%;
	max-width: $content_width;
	
	display: flex;
	column-gap: 16px;


	& > .home_content{
		min-width: fit-content;

		& > *{
			margin-bottom: 16px;

			&:last-child{
				margin-bottom: 0px 
			}
		}
	}
	& > .home_sidebar{
		width: 100%;
	}
}

</style>