<template>
<router-link :to="`/article/${article.id}`" class="primaryCard" :class="{horizontalCard: horizontal}">
    <img class="primaryCard_image" :src="article.imgURL" alt="article image">
    
    <div class="primaryCard_description">    
        <div class="primaryCard_info">
            <span class="primaryCard_info_date">{{formattedDate}}</span>
            <span class="primaryCard_info_number">{{numOfComments}}</span>
        </div>
        
        <h3 class="primaryCard_title">{{article.title}}</h3>
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

    & > .primaryCard_image{
        max-width: 100%;
        width: 120px;
        max-height: 90px;

        margin-right: 16px;
    }

    & > .primaryCard_description{
        max-width: 130px;

        & > .primaryCard_info{
            display: flex;
            justify-content: space-between;
    
            margin: 0 0 8px 0;

            & > .primaryCard_info_number{
                display: none;
            }
        }
    }
}
.primaryCard{
    max-width: 170px;
    min-height: 220px;

    display: block;

    & > .primaryCard_image{
        max-width: 100%;
        max-height: 128px;
    }

    & > .primaryCard_description{
        & > .primaryCard_info{
            display: flex;
            justify-content: space-between;
    
            margin: 8px 0;
    
            & > *{
                @include fontStyle($varelaRound, 12px, normal, 14px, initial);
            }
        }
    
        & > .primaryCard_title{
            @include fontStyle($bitter, 14px, bold, 18px, initial);
        }
    }

}

</style>