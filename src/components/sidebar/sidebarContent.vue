<template>
<div class="sidebar">
    <div class="sidebar_controls">
        <label for="popular" :class="{activeType: activeSelection == 'popular'}"> 
            Popular <input type="radio" id="popular" name="contentSelection" value="popular" v-model="activeSelection">
        </label>
        <label for="topRated" :class="{activeType: activeSelection == 'topRated'}"> 
            Top Rated <input type="radio" id="topRated" name="contentSelection" value="topRated" v-model="activeSelection">
        </label>
        <label for="comments" :class="{activeType: activeSelection == 'comments'}"> 
            Comments <input type="radio" id="comments" name="contentSelection" value="comments" v-model="activeSelection">
        </label>
    </div>
    <div v-if="articleList" class="sidebar_content">
        <SecondaryCard 
            :key="article.id" 
            :article="article" 
            v-for="article in articleList.slice(0, 5)"
        />
    </div>
</div>
</template>

<script>
import SecondaryCard from "@/components/cards/secondaryCard.vue";

export default {
    components: { SecondaryCard },
    data(){
        return{
            activeSelection: "popular",
            articleList: null,
        }
    },
    mounted(){
        this.articleList = this.$store.getters.getArticles(6);

        if(!this.articleList){
            this.$store.dispatch("fetchArticleList")
            this.articleList = this.$store.getters.getArticles(6);	
        }    
    }
}
</script>

<style lang="scss" scoped>
@import "@/styles/main.scss";

label.activeType{
    color: $highlight-yellow !important;
    border-bottom: 1px solid rgba($highlight-yellow, 0.3) !important;
}
.sidebar{
    width: 100%;
    //min-height: 675px;

    display: flex;
    flex-direction: column;

    padding-bottom: 43px;
    margin-bottom: 28px;

    background: $primary;
    
    .sidebar_controls{
        width: 100%;
        min-height: 53px;

        display: flex;
        justify-content: space-between;

        padding: 16px 32px;

        background-color: $primary-darker;

        label{
            @include fontStyle($varelaRound, 14px, normal, 17px, white);

            cursor: pointer;

            display: flex;
            justify-content: center;
            align-items: center;

            border-bottom: 1px solid rgba(#ACB3BA, 0.3);

            &>input{
                display: none !important;
            }
        }
    }

    .sidebar_content{
        & a {
            max-height: 114px
        }
    }
}
</style>