<template>
<section class="newsSelection" :class="{oneByOne: contentPlacement == '1x1'}">
    <div class="newsSelection_sidebar" :style="`background-color: ${newsCategory.color}`"></div>

    <div v-if="articleList" class="newsSelection_main">
        <div class="newsSelection_main_heading">
            <h2 class="category_title">{{newsCategory.category}}</h2>

            <div class="carouse_controls">
                <button type="button" @click="moveCarousel(-1)">
                    <img src="@/assets/svg/chevronLeft.svg" alt="left arrow" :class="{yellowSvg: newsCategory.category == 'News Carousel'}">
                </button>

                <button type="button" @click="moveCarousel(1)">
                    <img src="@/assets/svg/chevronRight.svg" alt="right arrow" :class="{yellowSvg: newsCategory.category == 'News Carousel'}">
                </button>
            </div>
        </div>

        <div v-if="carouselContent" :id="id" class="newsSelection_content">
            <NewsCard :key="article.id + Math.random()" :article="article" v-for="article in carouselContent"/>
        </div>
    </div>
</section>
</template>

<script>
import NewsCard from "@/components/cards/primaryCard.vue";
export default {
    props: {
        id:{
            type: String,
            required: true,
        },
        newsCategory:{
            type: Object,
            required: true
        },
        articleList: {
            type: Array,
            required: true
        },
        contentPlacement:{
            type: String,
            required: false
        }
    },
    components: { NewsCard },
    data(){
        return{
            isTransitioning: false,
            selectedIndex: 0,

            carouselOffset: 0,
            carouselContent: null,

            offsetWidth: null, 
            animationSpeed: 600 //ms
        }
    },
    methods: {
        moveCarousel(direction, disableAnimation=false){
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
            }, this.animationSpeed)
        },

        // On button click, change move the carousel
        moveImages(disableAnimation){
            const carousel = document.getElementById(this.id);
            
            this.carouselOffset = this.selectedIndex * -this.offsetWidth;
            
            carousel.style.transition = disableAnimation? "none": `${this.animationSpeed}ms ease-in-out`;
            carousel.style.transform = `translateX(${this.carouselOffset}px)`;

            setTimeout(() => {
                this.checkForReset(carousel)
            }, this.animationSpeed)
        },

        // Check if the last/first slide is reached, if it is, turn off the transition and reset the slide
        checkForReset(carousel){
            const maxOffset = (carousel.children.length - 2) * this.offsetWidth
            
            if(Math.abs(this.carouselOffset) == maxOffset){
                this.selectedIndex = 1;
                this.resetCarousel(carousel);
            }
            else if(this.carouselOffset == 0){
                this.selectedIndex = carousel.children.length - 3;
                this.resetCarousel(carousel);
            }
        },
        resetCarousel(carousel){
            this.carouselOffset = this.selectedIndex * -this.offsetWidth;

            carousel.style.transition = "none";
            carousel.style.transform = `translateX(${this.carouselOffset}px)`;
        },
        // Clones the first and last element to the opposite place in the list so 
        // we can create the infinite effect
        cloneElements(){
            const firstElem = this.articleList[0];
            const secondElem = this.articleList[1];
            const lastElem = this.articleList[this.articleList.length - 1];

            this.carouselContent = [lastElem, ...this.articleList, firstElem, secondElem];
        },

        initCarousel(){
            this.cloneElements();
            this.$nextTick(() => this.moveCarousel(1, true))
        }
    },
    mounted(){
        this.offsetWidth = this.contentPlacement? 260: 290; // card width + col gap
        this.initCarousel();
    },
}
</script>

<style lang="scss" scoped>
@import "@/styles/main.scss";

.yellowSvg{
    filter: brightness(0) saturate(100%) invert(88%) sepia(30%) saturate(1147%) hue-rotate(327deg) brightness(103%) contrast(98%);
}

section.oneByOne{
    max-width: 300px !important;

    div.newsSelection_content > a{
        min-width: 230px !important;
    }
}

.newsSelection{
    max-width: 620px;
    max-height: 325px;

    display: flex;

    background-color: white;

    .newsSelection_sidebar{
        min-width: 12px;
    }

    .newsSelection_main{
        display: flex;
        flex-direction: column;

        overflow: hidden;

        .newsSelection_main_heading{
            display: flex;
            justify-content: space-between;

            padding: 16px 32px 0 32px;

            .category_title{
                @include fontStyle($bitter, 24px, bold, 29px, initial);
            }

            .carouse_controls{
                display: flex;
                align-items: center;
                column-gap: 12px;

                padding-top: 12px;

                button {
                    cursor: pointer;

                    border: none;
                    background: none;

                    img {
                        width: 16px;
                        height: 22px;
                    }
                }

            }
        }

        .newsSelection_content{
            width: 100%;
            display: flex;
            column-gap: 30px;
            margin: 32px 28px;

            a{
                min-width: 260px;
            }
        }
    }
}
</style>