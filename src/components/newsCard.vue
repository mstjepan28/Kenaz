<template>
<div class="card" :class="{horizontalCard: horizontal}">
    <img class="card_image" src="https://images.unsplash.com/photo-1593642632559-0c6d3fc62b89?ixlib=rb-1.2.1&ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1769&q=80" alt="">
    
    <div class="card_description">    
        <div class="card_info">
            <span class="card_info_date">{{formattedDate}}</span>
            <span class="card_info_number">14</span>
        </div>
        
        <h3 class="card_title">
            For Obama, MLK's shadow looms large ahead of speech
        </h3>
    </div>
</div>
</template>

<script>
import dayjs from "dayjs";

export default {
    props:{
        horizontal:{
            type: Boolean,
            required: false,
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

div.horizontalCard{
    max-width: 100%;
    min-height: auto;

    display: flex;

    & > .card_image{
        max-width: 100%;
        max-height: 90px;

        margin-right: 16px;
    }

    & > .card_description{
        max-width: 130px;

        & > .card_info{
            display: flex;
            justify-content: space-between;
    
            margin: 0 0 8px 0;

            & > .card_info_number{
                display: none;
            }
        }
    }
}
.card{
    max-width: 170px;
    min-height: 220px;

    & > .card_image{
        max-width: 100%;
        max-height: 128px;
    }

    & > .card_description{
        & > .card_info{
            display: flex;
            justify-content: space-between;
    
            margin: 8px 0;
    
            & > *{
                @include fontStyle($varelaRound, 12px, normal, 14px, initial);
            }
        }
    
        & > .card_title{
            @include fontStyle($bitter, 14px, bold, 18px, initial);
        }
    }

}

</style>