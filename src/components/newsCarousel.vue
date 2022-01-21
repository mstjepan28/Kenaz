<template>
<header class="carousel" v-if="carouselContent">
    <div class="carousel_controls">
        <button class="carousel_controls_left" type="button" @click="changeSlide(-1)">
            <img src="@/assets/svg/largeChevronLeft.svg" alt="left arrow">
        </button>
        <button class="carousel_controls_right" type="button" @click="changeSlide(1)">
            <img src="@/assets/svg/largeChevronRight.svg" alt="right arrow">
        </button>
    </div>

    <div class="carousel_description">
        <div class="carousel_description_info">
            <span class="carousel_description_info_date">{{formattedDate}}</span>
            <span class="carousel_description_info_comments"> <img src="@/assets/commentBubble.png" alt="comment bubble">{{carouselContent[selectedIndex].comments}} Comments</span>
        </div>

        <h1 class="carousel_description_title">{{carouselContent[selectedIndex].title}}</h1>

        <button class="carousel_description_gotoArticle">Read article</button>
    </div>

    <div class="carousel_background">
        <img :key="slide.id" :src="slide.imgURL" v-for="slide in carouselContent">
    </div>
</header>
</template>

<script>
import dayjs from 'dayjs';

export default {
    props:{
        newsList:{
            type: Array,
            required: true
        }
    },
    data(){
        return{
            selectedIndex: 0,
            carouselContent: null,

            carouselOffset: 0,
            isTransitioning: false,
        }
    },
    computed:{
        formattedDate(){
            const date = this.carouselContent[this.selectedIndex].date
            return dayjs(date).format('MMMM DD, YYYY');
        }
    },
    methods: {
        // Adds/subtracts from the current index and makes sure the index stays in bounds 
        changeSlide(direction){
            if(this.isTransitioning) return;
            this.isTransitioning = true

            this.selectedIndex += direction;

            if(this.selectedIndex >= this.carouselContent.length)
                this.selectedIndex = 0;
            else if(this.selectedIndex < 0)
                this.selectedIndex = this.carouselContent.length - 1

            this.moveImages();

            setTimeout(() => {
                this.isTransitioning = false
            }, 750)
        },

        // On button click, change move the carousel
        moveImages(){
            const carousel = document.querySelector("div.carousel_background");
            
            this.carouselOffset = this.selectedIndex * -carousel.offsetWidth;
            
            carousel.style.transition = "0.75s ease-in-out";
            carousel.style.transform = `translateX(${this.carouselOffset}px)`;

            setTimeout(() => {
                this.checkForReset(carousel)
            }, 750)
        },

        // Check if the last/first slide is reached, if it is, turn off the transition and reset the slide
        checkForReset(carousel){
            const maxOffset = (carousel.children.length - 1) * carousel.offsetWidth
            
            if(Math.abs(this.carouselOffset) == maxOffset){
                this.selectedIndex = 1;
                this.resetCarousel(carousel);
            }
            else if(this.carouselOffset == 0){
                this.selectedIndex = carousel.children.length - 2;
                this.resetCarousel(carousel);
            }
        },
        resetCarousel(carousel){
            this.carouselOffset = this.selectedIndex * -carousel.offsetWidth;

            carousel.style.transition = "none";
            carousel.style.transform = `translateX(${this.carouselOffset}px)`;
        },

        // Clones the first and last element to the opposite place in the list so 
        // we can create the infinite effect
        cloneElements(){
            const firstElem = this.newsList[0];
            const lastElem = this.newsList[this.newsList.length - 1];

            this.carouselContent = [lastElem, ...this.newsList, firstElem];
        }
    },
    mounted(){
        this.cloneElements();

        setInterval(() => {
            this.changeSlide(1);
        }, 4750);
    },
}
</script>

<style lang="scss" scoped>
@import "@/styles/main.scss";

.carousel{
    width: 100%;
    max-width: $content_width;
    height: 425px;

    margin-bottom: 20px;

    position: relative;
    overflow: hidden;

    & > .carousel_controls{
        width: 100%;

        display: flex;
        justify-content: space-between;
        align-items: center;

        position: absolute;
        top: 0;
        bottom: 0;
        z-index: 2;

        padding: 0 28px;

        & > button{
            cursor: pointer;
            border: none;
            background-color: transparent;
        }
    }

    & > .carousel_description{
        display: flex;
        flex-direction: column;

        margin: 28px;

        position: absolute;
        bottom: 0;
        z-index: 2;

        & > .carousel_description_info{
            display: flex;
            column-gap: 24px;

            & > span{
                @include fontStyle($varelaRound, 12px, normal, 14px, $font_color-gray);

                display: flex;
                align-items: center;
            }

            & img{
                width: 16px;
                height: 14px;

                margin-right: 8px;
            }
        }

        & > .carousel_description_title{
            @include fontStyle($bitter, 34px, bold, 41px, $font_color-gray);
            max-width: 65%;

            margin: 12px 0;
        }

        & > .carousel_description_gotoArticle{
            @include fontStyle($varelaRound, 14px, normal, 17px, $font_color-gray);

            align-self: flex-start;

            padding: 8px 22px;

            cursor: pointer;

            border: 1px solid #FFFFFF;
            background-color: transparent;
        }
    }

    & > .carousel_background{
        min-width: 100%;
        height: 100%;

        display: flex;

        & > img{
            min-width: 100%;
            height: 100%;
        }
    }
}
</style>