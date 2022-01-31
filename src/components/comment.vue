<template>
<div class="comment">
    <div class="user_img">
        <img :src="comment.imgURL" alt="">
    </div>

    <div class="comment_main">
        <div class="comment_info">
            <span class="comment_info_user">{{comment.user}}</span>
            <span class="comment_info_date">{{formattedDate}}</span>
            <button class="comment_info_replyButton">Reply</button>
        </div>
        <p class="comment_text">{{comment.text}}</p>
    </div>
</div>
</template>

<script>
import dayjs from "dayjs"

export default {
    props: {
        comment:{
            type: Object,
            required: true
        }
    },
    computed:{
        formattedDate(){
            const advancedFormat = require('dayjs/plugin/advancedFormat')
            dayjs.extend(advancedFormat)

            const date = this.comment.date * 1000;
            return dayjs(date).format('MMM Do, YYYY h:mm a');
        },
    }

}
</script>

<style lang="scss" scoped>
@import "@/styles/main.scss";

.comment{
    display: flex;
    margin-bottom: 48px;

    & > .user_img{
        max-width: 60px;
        height: 60px;

        margin-right: 16px;

        background-color: red;

        & > img{
            max-width: 60px;
            aspect-ratio: 1/1;
        }
    }

    & .comment_main{
        //background-color: blue
    }

    & p{
        @include fontStyle($varelaRound, 13px, normal, 20px, #444444);

    }

    & .comment_info{
        display: flex;

        & > .comment_info_user{
            @include fontStyle($bitter, 18px, normal, 20px, $primary);
            margin-right: 8px;
        }
        & > .comment_info_date{
            @include fontStyle($varelaRound, 11px, normal, initial, #666666);
            
            display: flex;
            align-items: flex-end
        }

        & > .comment_info_replyButton{
            @include fontStyle($varelaRound, 14px, normal, 16px, $primary);
            margin-left: auto;
            
            cursor: pointer;

            border: none;
            background: none;

            &:hover, &:focus{
                text-decoration: underline;
            }
        }
    }
}

</style>