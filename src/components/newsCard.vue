<template>
<router-link :to="`/article/${article.id}`" class="card" :class="{horizontalCard: horizontal}">
    <img class="card_image" :src="article.imgURL" alt="article image">
    
    <div class="card_description">    
        <div class="card_info">
            <span class="card_info_date">{{formattedDate}}</span>
            <span class="card_info_number">{{numOfComments}}</span>
        </div>
        
        <h3 class="card_title">{{article.title}}</h3>
    </div>
</router-link>
</template>

<script>
import dayjs from "dayjs";

export default {
    props:{
        horizontal:{
            type: Boolean,
            required: false,
        },
        article:{
            type: Object,
            required: true,
        }
    },
    computed:{
        formattedDate(){
            const date = this.article.date * 1000;
            return dayjs(date).format('MMMM DD, YYYY');
        },
        numOfComments(){
            return this.article.commentIds.length
        },
    },
}
</script>

<style lang="scss" scoped>
@import "@/styles/main.scss";

a.horizontalCard{
    max-width: 100%;
    min-height: auto;

    display: flex;

    & > .card_image{
        max-width: 100%;
        width: 120px;
        max-height: 90px;

        margin-right: 16px;
    }

    & > .card_description{
        max-width: 130px;

        & > .card_info{
            display: flex;
            justify-content: space-between;
    
            margin: 0 0 8px 0;

            & > .card_info_number{
                display: none;
            }
        }
    }
}
.card{
    max-width: 170px;
    min-height: 220px;

    display: block;

    & > .card_image{
        max-width: 100%;
        max-height: 128px;
    }

    & > .card_description{
        & > .card_info{
            display: flex;
            justify-content: space-between;
    
            margin: 8px 0;
    
            & > *{
                @include fontStyle($varelaRound, 12px, normal, 14px, initial);
            }
        }
    
        & > .card_title{
            @include fontStyle($bitter, 14px, bold, 18px, initial);
        }
    }

}

</style>