<template>
<router-link :to="`/article/${article.id}`" v-if="article" class="secondaryCard">
    <div class="secondaryCard_description">
        <div class="secondaryCard_description_info" :class="{oneRowInfo: oneRowInfo}">
            <div class="secondaryCard_description_info_comments">
                <img src="@/assets/commentBubble.png" alt="comment bubble"> {{numOfComments}}
            </div>
            <div class="secondaryCard_description_info_date">{{formattedDate}}</div>
        </div>

        <h3>{{shortTitle}}</h3>
    </div>

    <div class="secondaryCard_imgWrapper">
        <img :src="article.imgURL" alt="article img">
    </div>
</router-link>
</template>

<script>
import dayjs from "dayjs";

export default {
    props:{
        oneRowInfo: {
            type: Boolean,
            required: false
        },
        article:{
            type: Object,
            required: false,
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
        shortTitle(){
            const res = this.article.title.slice(0, 40);
            return res.length == this.article.title? res: res + "...";
        }
    },
}
</script>

<style lang="scss" >
@import "@/styles/main.scss";

.oneRowInfo{
    display: flex;
    justify-content: space-between;
    flex-direction: row-reverse;
    
    * {
        color: #666666 !important;
    }
    img{
        display: none;
    }
}

a.secondaryCard{
    display: flex;

    padding: 22px 32px;

    cursor: pointer;
    
    border-bottom: 1px solid rgba(black, 0.2);

    &:hover{
        background-color: rgba(black, 0.1);
    }

    .secondaryCard_description{
        .secondaryCard_description_info_comments{
            @include fontStyle($varelaRound, 10px, normal, 12px, #ADB3BA);

            display: flex;
            justify-content: flex-end;

            margin-right: 28px;

            img{
                width: 10px;
                height: 10px;

                filter: brightness(0) saturate(100%) invert(82%) sepia(4%) saturate(481%) hue-rotate(172deg) brightness(88%) contrast(86%);

                margin-right: 4px;
            }
        }
        .secondaryCard_description_info_date{
            @include fontStyle($varelaRound, 10px, normal, 12px, #ADB3BA);
        }

        h3{
            @include fontStyle($bitter, 14px, bold, 16px, white);
            margin: 8px 8px 0 0;
            word-break: break-all;
        }
    }

    .secondaryCard_imgWrapper > img{
        width: 70px;
        height: 70px;
        border: 2px solid white;
    }
}
</style>