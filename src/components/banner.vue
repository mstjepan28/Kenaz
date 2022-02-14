<template>
<div class="banner">
    <span v-if="imgSrc">
        <img :src="imgSrc" alt="banner">
    </span>
    <span v-else>
        Banner goes here
    </span>
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
    height: 123px;

    display: flex;
    justify-content: center;
    align-items: center;

    margin: 16px 0;

	background: #FFFFFF;
    border: 1px solid #D7D7D7;

    img{
        width: 100%;
        height: 100%;
    }

    span{
        text-align: center;
    }
}
</style>