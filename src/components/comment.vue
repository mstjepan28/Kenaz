<template>
<div v-if="commentData" class="comment" :class="{reply: replyId}">
    <div class="user_img">
        <img v-if="commentData.imgURL" :src="commentData.imgURL" alt="user profile picture">
        <img v-else src="../assets/defaultUserImg.png" alt="default user image">
    </div>

    <div class="comment_main">
        <div class="comment_info">
            <span class="comment_info_user">{{commentData.user}}</span>
            <span class="comment_info_date">{{formattedDate}}</span>
            <button v-if="!replyId" class="comment_info_replyButton" @click="replyToComment()">Reply</button>
        </div>
        <p class="comment_text">{{commentData.text}}</p>
    </div>
</div>
</template>

<script>
import dayjs from "dayjs"

export default {
    props: {
        comment:{
            type: Object,
            required: false
        },
        replyId:{
            type: String,
            required: false
        }
    },
    data(){
        return{
            commentData: null
        }
    },
    computed:{
        formattedDate(){
            const advancedFormat = require('dayjs/plugin/advancedFormat')
            dayjs.extend(advancedFormat)

            const date = this.commentData.date * 1000;
            return dayjs(date).format('MMM Do, YYYY h:mm a');
        },
    },
    methods:{
        replyToComment(){
            this.$emit("reply", this.commentData.id)
        }
    },
    mounted() {
        if(this.replyId)
            this.commentData = this.$store.getters.getReplyById(this.replyId)    
        else if(this.comment)
            this.commentData = this.comment
    },

}
</script>

<style lang="scss" scoped>
@import "@/styles/main.scss";

div.reply{
    width: 90%;
    margin-left: auto;
    padding: 0 0 24px 0;
}
.comment{
    width: 100%;

    display: flex;
    padding: 24px 0;

    .user_img{
        max-width: 60px;
        height: 60px;

        margin-right: 16px;

        img{
            max-width: 60px;
            aspect-ratio: 1/1;
        }
    }

    p{
        @include fontStyle($varelaRound, 13px, normal, 20px, #444444);
    }

    .comment_main{
        width: 100%;
    }
    .comment_info{
        display: flex;

        .comment_info_user{
            @include fontStyle($bitter, 18px, normal, 20px, $primary);
            margin-right: 8px;
        }
        .comment_info_date{
            @include fontStyle($varelaRound, 11px, normal, initial, #666666);
            
            display: flex;
            align-items: flex-end
        }

        .comment_info_replyButton{
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