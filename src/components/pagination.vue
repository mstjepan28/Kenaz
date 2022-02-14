<template>
<div class="pagination">
    <button 
        class="pagination_pageNum" 
        :class="{active: pageNum == curPage}"
        
        type="button" 
        @click="setPage(pageNum)"
        
        :key="pageNum"
        v-for="pageNum in totalPagesList"
    >
        {{pageNum}}
    </button>
</div>
</template>

<script>

export default {
    props:{
        totalPages:{
            type: Number,
            required: true
        }
    },
    data(){
        return{
            curPage: 1,
        }
    },
    computed:{
        // create an array from 1 to this.totalPages.length => [1,2,3,4,5,...]
        totalPagesList(){
            return Array.from({length: this.totalPages}, (_, i) => i + 1)
        }
    },
    methods:{
        setPage(page){
            this.curPage = page;
            this.$emit("changePage", page)
        }
    }
}
</script>

<style lang="scss" scoped>
@import "@/styles/main.scss";
.pagination{
    width: 100%;

    display: flex;
    align-items: center;

    column-gap: 4px;

    padding: 32px;
    margin-top: auto;

    .pagination_pageNum{
        @include fontStyle($varelaRound, 14px, normal, 17px, $primary);

        padding: 8px 12px;

        cursor: pointer;

        border: none;
        background-color: #DDDDDD;

        &:hover, &.active{
            color: white;
            background-color: $primary;
        }
    }

}
</style>