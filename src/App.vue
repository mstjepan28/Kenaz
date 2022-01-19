<template>
	<div class="app">
		<Navbar :categoryList="categoryList"/>

		<Banner :imgSrc="''"/>

		<router-view/>
	</div>
</template>

<script>
import Navbar from "@/components/navbar.vue";
import Banner from "./components/banner.vue";

export default {
	components: { Navbar, Banner },
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

<style lang="scss">
@import "@/styles/main.scss";

.app{
	width: 100%;

	display: flex;
	flex-direction: column;
	align-items: center;

	background-color: $background;
}

</style>
