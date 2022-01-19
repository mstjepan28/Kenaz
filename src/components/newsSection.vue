<template>
<div class="newsSelection">
    <div class="newsSelection_sidebar" :style="`background-color: ${newsCategory.color}`"></div>

    <div class="newsSelection_main">
        <div class="newsSelection_main_heading">
            <span class="category_title">{{newsCategory.category}}</span>
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
                font-family: Bitter;
                font-size: 24px;
                font-weight: 700;
                line-height: 29px;
            }

            & > .seeAll_link{
                font-family: "Varela Round";
                font-size: 14px;
                font-weight: 400;
                line-height: 17px;
                text-align: right;

                color: $font_color-blue;
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