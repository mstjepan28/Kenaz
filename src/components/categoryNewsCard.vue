<template>
<article class="categoryNewsCard">
    <h2>{{news.title}}</h2>

    <div class="categoryNewsCard_info">
        <span class="categoryNewsCard_info_date">
            <img src="../assets/calendar.png" alt="calendar icon">{{formattedDate}}
        </span>
        <span class="categoryNewsCard_info_author">
            Author: {{author}}
        </span>
        <span class="categoryNewsCard_info_comments">
            {{numOfComments}} comments
        </span>
    </div>

    <div class="categoryNewsCard_content">
        <div class="categoryNewsCard_content_img">
            <img :src="news.imgURL" alt="">
        </div>
        <div class="categoryNewsCard_content_text">
            <p>{{shortContent}}</p>

            <router-link :to="`/article/${news.id}`" class="readArticle">Read article</router-link>
        </div>
    </div>
</article>
</template>

<script>
import dayjs from "dayjs";

export default {
    props:{
        news:{
            type: Object,
            required: true
        }
    },
    data(){
        return{
            author: null
        }
    },
    computed:{
        numOfComments(){
            return this.news.commentIds.length
        },
        formattedDate(){
            const date = this.news.date * 1000;
            return dayjs(date).format('MMMM DD, YYYY');
        },
        shortContent(){
            return this.news.content.slice(0, 500) + "...";
        }
    },
    mounted(){
        if(!this.$store.state.authorList) 
            this.$store.dispatch('fetchAuthorList')
        
        this.author = this.$store.getters.getAuthorById(this.news.authorId).name
    }
}
</script>

<style lang="scss" scoped>
@import "@/styles/main.scss";

.categoryNewsCard{
    width: 100%;
    max-width: 620px;

    padding: 24px 16px 64px 32px;

    border-bottom: 1px solid #DDDDDD;

    & > h2{
        @include fontStyle($bitter, 24px, bold, 24px, #363F48);
    }

    & > .categoryNewsCard_info{
        @include fontStyle($varelaRound, 12px, normal, 14px, #666666);

        display: flex;
        align-items: center;
        column-gap: 32px;

        padding: 16px 0 8px 0;

        & > .categoryNewsCard_info_date{
            display: flex;
            align-items: center;

            img{
                max-width: 16px;
                margin-right: 4px;
            }
        }
    }

    & > .categoryNewsCard_content{
        display: flex;

        & > .categoryNewsCard_content_img{
            width: 170px;
            min-width: 170px;
            max-height: 128px;

            & > img{
                width: 100%;
                height: 100%;
            }
        }

        & > .categoryNewsCard_content_text{
            padding-left: 20px;

            & > p{
                @include fontStyle($bitter, 14px, normal, 22px, #444444);
            }

            & > .readArticle{
                @include fontStyle($varelaRound, 14px, normal, 16px, white);

                display: inline-block;

                padding: 8px 20px;
                margin-top: 24px;


                background-color: $primary;
            }
        }
    }
}
</style>