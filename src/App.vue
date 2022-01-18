<template>
	<Navbar/>

	<router-view/>
</template>

<script>
import Navbar from "@/components/navbar.vue";

export default {
	components: { Navbar }
}

</script>

<style lang="scss">
@import "@/styles/main.scss";


</style>
