<template>
    <li 
        class="category" 
        :class="{active: isCurCategory}"
        :style="`border-bottom: 3px solid ${category.color}`" 
        role="button" 
        @click="gotoCategory(category.category)"
        
    >
        <span class="category_title">{{upperCaseCategory}}</span>
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
    },
    computed:{
        isCurCategory(){
            const categoryId = this.$route.params.id;
            const curCategory = this.category.category.toLowerCase();

            return categoryId == curCategory
        },
        upperCaseCategory(){
            return this.category.category.toUpperCase();
        }
    },
    methods: {
        gotoCategory(categoryId){
            this.$router.push({ name: 'Category', params: { id: categoryId.toLowerCase() } })
        }
    },
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

    .category_title{
        @include fontStyle($bitter, 18px, bold, 21px, $font_color);

        position: relative;
        transition: 0.4s;

        z-index: 2;
    }

    .category_background{
        width: 100%;
        height: 100px;

        position: absolute;
        top: 97px;
        left: 0;
        right: 0;

        z-index: 1;
    }

    &.active{
        border-bottom-width: 0;
        .category_background{
            top: 0px;
        }
        .category_title{
            top: 3px;
        }
    }

    &:not(.active):hover{
        animation: removeBorder 0.4s forwards;

        .category_background{
            animation: moveUp 0.4s forwards;
        }

        .category_title{
            animation: moveTextDown 0.4s forwards;
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
    @keyframes moveTextDown {
        from{
            top: 0;
        }
        to{
            top: 3px;
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