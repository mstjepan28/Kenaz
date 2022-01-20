<template>
<div class="newsSelection">
    <div class="newsSelection_sidebar" :style="`background-color: ${newsCategory.color}`"></div>

    <div class="newsSelection_main">
        <div class="newsSelection_main_heading">
            <h2 class="category_title">{{newsCategory.category}}</h2>
            <router-link to="/" class="seeAll_link">See all</router-link>
        </div>

        <div class="newsSelection_content">
            <NewsCard/>
            <NewsCard/>
            <NewsCard/>
        </div>
    </div>

</div>
</template>

<script>
import NewsCard from "./newsCard.vue";
export default {
    props: {
        newsCategory:{
            type: Object,
            required: true
        }
    },
    components: { NewsCard }
}
</script>

<style lang="scss" scoped>
@import "@/styles/main.scss";

.newsSelection{
    display: flex;

    background-color: white;

    & > .newsSelection_sidebar{
        width: 12px;
    }

    & > .newsSelection_main{
        display: flex;
        flex-direction: column;

        & > .newsSelection_main_heading{
            display: flex;
            justify-content: space-between;

            padding: 16px 32px 0 32px;

            & > .category_title{
                @include fontStyle($bitter, 24px, bold, 29px, initial);
            }

            & > .seeAll_link{
                @include fontStyle($varelaRound, 14px, normal, 17px, $font_color-blue);
                text-align: right;
            }
        }

        & > .newsSelection_content{
            display: flex;
            column-gap: 20px;
            margin: 32px 28px;
        }
    }
}
</style>