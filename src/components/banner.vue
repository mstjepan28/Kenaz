<template>
	<div class="banner">
		<img :src="imgSrc" alt="banner">
	</div>
</template>

<script>

export default {
    props: {
        imgSrc: {
            type: String
        },
    }
}
</script>

<style lang="scss" scoped>
@import "@/styles/main.scss";

.banner{
    width: 100%;
    max-width: $content_width;
    height: 120px;

    margin: 16px 0;

	background: #FFFFFF;
    border: 1px solid #D7D7D7;

    img{
        width: 100%;
        height: 100%;
    }
}
</style>