<template>
<article class="categoryNewsCard">
    <h2>{{news.title}}</h2>

    <div class="categoryNewsCard_info">
        <span class="categoryNewsCard_info_date">
            <img src="" alt="">
        </span>
        <span class="categoryNewsCard_info_author">

        </span>
        <span class="categoryNewsCard_info_comments">

        </span>
    </div>
</article>
</template>

<script>

export default {
    props:{
        news:{
            type: Object,
            required: true
        }
    },
    data(){
        return{

        }
    },
    mounted() {
        console.log(this.news)
    },
}
</script>

<style lang="scss" scoped>

.categoryNewsCard{
    width: 100%;
    max-width: 620px;
}
</style>