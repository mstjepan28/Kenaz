<template>
<div>
    <div class="title">
        <h2>Kenaz TV</h2>
    </div>
    <iframe 
        width="300" height="150" 
        :src="videoLink" 
        title="Kenaz TV" 
        frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen
    ></iframe>
    <div class="video_description">
        <div class="video_date">{{formattedDate}}</div>
        <h3 class="video_title">
            NASA releases portrait of a planet waving at Saturn
        </h3>
    </div>
</div>
</template>

<script>
import dayjs from "dayjs";

export default {
    props:{
        videoLink: {
            type: String,
            required: true,
        }
    },
    computed:{
        formattedDate(){
            const date = 1642675620987
            return dayjs(date).format('MMMM DD, YYYY');
        }
    },
}
</script>

<style lang="scss" scoped>
@import "@/styles/main.scss";

.title{
    padding: 16px 32px 32px 32px;
    margin-top: 20px;

    background-color: white;

    & > h2{
        @include fontStyle($bitter, 24px, bold, 29px, #363F48);
    }
}

.video_description{
    padding: 16px 32px 24px 32px;
    background-color: white;
    & > .video_date{
        @include fontStyle($varelaRound, 12px, normal, 14px, #666666);

    }

    & > .video_title{
        @include fontStyle($bitter, 14px, bold, 18px, #363F48);
    }

}
</style>