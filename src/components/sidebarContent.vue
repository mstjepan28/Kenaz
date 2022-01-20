<template>
<div class="container">
    <div class="controls">
        <label for="popular" :class="{activeType: activeSelection == 'popular'}"> 
            Popular <input type="radio" id="popular" name="contentSelection" value="popular" v-model="activeSelection">
        </label>
        <label for="topRated" :class="{activeType: activeSelection == 'topRated'}"> 
            Top Rated <input type="radio" id="topRated" name="contentSelection" value="topRated" v-model="activeSelection">
        </label>
        <label for="comments" :class="{activeType: activeSelection == 'comments'}"> 
            Comments <input type="radio" id="comments" name="contentSelection" value="comments" v-model="activeSelection">
        </label>
    </div>
    <div class="content">
        <SidebarContentCard />
        <SidebarContentCard />
        <SidebarContentCard />
        <SidebarContentCard />
        <SidebarContentCard />
    </div>
</div>
</template>

<script>
import SidebarContentCard from "./sidebarContentCard.vue";

export default {
    components: { SidebarContentCard },
    data(){
        return{
            activeSelection: "popular",
        }
    }
}
</script>

<style lang="scss" scoped>
@import "@/styles/main.scss";

.activeType{
    color: $highlight-yellow !important;
}
.container{
    width: 100%;

    display: flex;
    flex-direction: column;

    padding-bottom: 40px;
    margin-bottom: 28px;

    background: $primary;

    & > .controls{
        width: 100%;

        display: flex;
        justify-content: space-between;

        padding: 16px 32px;

        background-color: $primary-darker;

        & > label{
            @include fontStyle($varelaRound, 14px, normal, 17px, white);

            cursor: pointer;

            display: flex;
            justify-content: center;
            align-items: center;

            text-decoration: underline;

            &>input{
                display: none !important;
            }
        }
    }
}
</style>