<template>
<section class="carousel" v-if="carouselContent">
    <div class="carousel_controls">
        <button class="carousel_controls_left" type="button" @click="changeSlide(-1)">
            <img src="@/assets/svg/largeChevronLeft.svg" alt="left arrow">
        </button>

        <button v-if="imagesOnly" class="carousel_controls_open" type="button" @click="openImage()">
            <img src="@/assets/search.png" alt="open image">
        </button>

        <button class="carousel_controls_right" type="button" @click="changeSlide(1)">
            <img src="@/assets/svg/largeChevronRight.svg" alt="right arrow">
        </button>
    </div>

    <div v-if="imagesOnly" class="carousel_preview">
        <img 
            class="carousel_preview_img" role="button" 
            :key="slide.id" :src="slide.imgURL" v-for="slide in carouselContent.slice(0, 7)"
            @click="openImage(slide.imgURL)"
        >
    </div>

    <div v-else class="carousel_description">
        <div class="carousel_description_info">
            <span class="carousel_description_info_date">{{formattedDate}}</span>
            <span class="carousel_description_info_comments"> <img src="@/assets/commentBubble.png" alt="comment bubble">{{carouselContent[selectedIndex].comments}} Comments</span>
        </div>

        <h1 class="carousel_description_title">{{carouselContent[selectedIndex].title}}</h1>

        <router-link :to="`/article/${carouselContent[selectedIndex].id}`" class="carousel_description_gotoArticle">Read article</router-link>
    </div>

    <div :id="id" class="carousel_background">
        <img :key="slide.id" :src="slide.imgURL" v-for="slide in carouselContent">
    </div>
</section>
</template>

<script>
import dayjs from 'dayjs';

export default {
    props:{
        id: {
            type: String,
            required: true,
        },
        imagesOnly: {
            type: Boolean,
            required: false
        },
        autoplay: {
            type: Boolean,
            required: false
        },
        articleList:{
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
        openImage(imgURL=null){
            if(imgURL) this.moveToImage(imgURL);

            imgURL = imgURL? imgURL: this.carouselContent[this.selectedIndex].imgURL;
            this.$emit("openImgModal", imgURL)
        },

        moveToImage(imgUrl){
            this.selectedIndex = this.carouselContent.findIndex(item => item.imgURL == imgUrl);
            this.moveImages();
        },

        // Adds/subtracts from the current index and makes sure the index stays in bounds 
        changeSlide(direction, disableAnimation=false){
            if(this.isTransitioning) return;
            this.isTransitioning = true

            this.selectedIndex += direction;

            if(this.selectedIndex >= this.carouselContent.length)
                this.selectedIndex = 0;
            else if(this.selectedIndex < 0)
                this.selectedIndex = this.carouselContent.length - 1

            this.moveImages(disableAnimation);

            setTimeout(() => {
                this.isTransitioning = false
            }, 750)
        },

        // On button click, change move the carousel
        moveImages(disableAnimation){
            const carousel = document.getElementById(this.id);
            
            this.carouselOffset = this.selectedIndex * -carousel.offsetWidth;
            
            carousel.style.transition = disableAnimation? "none": "0.75s ease-in-out";
            carousel.style.transform = `translateX(${this.carouselOffset}px)`;

            setTimeout(() => {
                this.checkForReset(carousel)
            }, 750)
        },

        // Check if the last/first slide is reached, if it is, turn off the transition and reset the slide
        checkForReset(carousel){
            const maxOffset = (carousel.children.length - 1) * carousel.offsetWidth
            console.log(maxOffset, Math.abs(this.carouselOffset), this.selectedIndex)
            
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
            const firstElem = this.articleList[0];
            const lastElem = this.articleList[this.articleList.length - 1];

            this.carouselContent = [lastElem, ...this.articleList, firstElem];
            
        },
    },
    mounted(){
        this.cloneElements();
        this.$nextTick(() => this.changeSlide(1, true))
        //setTimeout(() => , 50); // to set the carousel to a non-cloned slide
        
        if(this.autoplay){
            setInterval(() => this.changeSlide(1), 4750);
        }
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

        & > .carousel_controls_open > img{
            max-width: 80px;
            max-height: 80px;
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

    & > .carousel_preview{
        display: flex;
        flex-direction: row;
        column-gap: 10px;

        margin: 20px;

        position: absolute;
        bottom: 0;
        z-index: 2;

        & > .carousel_preview_img{
            $previewImg-size: 120px;
            width: $previewImg-size;
            height: $previewImg-size;

            cursor: pointer;
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