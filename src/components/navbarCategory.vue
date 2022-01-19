<template>
    <li class="category" :style="`border-bottom: 3px solid ${category.color}`">
        <span class="category_title">{{category.category}}</span>
        <div 
            class="category_background" 
            :style="`background-color: ${category.color}`"
        ></div>
    </li>
</template>

<script>

export default {
    props:{
        category: Object
    }
}
</script>

<style lang="scss" scoped>
@import "@/styles/main.scss";

.category{
    padding: 16px 20px;

    cursor: pointer;

    position: relative;
    overflow: hidden;

    border-bottom: 3px solid red;

    & > .category_title{
        font-family: Bitter, sans-serif;
        font-weight: 700;
        font-size: 18px;
        line-height: 21.6px;
    
        color: $font_color;

        position: relative;

        z-index: 2;
    }

    & > .category_background{
        width: 100%;
        height: 100px;

        position: absolute;
        top: 97px;
        left: 0;
        right: 0;

        z-index: 1;
    }

    &:hover{
        animation: removeBorder 0.4s forwards;

        & > .category_background{
            animation: moveUp 0.4s forwards;
        }
    }

    @keyframes removeBorder {
        from{
            border-bottom-width: 3px;
        }
        to{
            border-bottom-width: 0;
        }
    }
    @keyframes moveUp {
        from{
            top: 97px;
        }
        to{
            top: 0px;
        }
    }
}
</style>