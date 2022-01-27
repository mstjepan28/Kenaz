<template>
<div class="secondaryCard">
    <div class="secondaryCard_description">
        <div class="secondaryCard_description_info">
            <div class="secondaryCard_description_info_comments">
                <img src="@/assets/commentBubble.png" alt="comment bubble"> 5
            </div>
            <div class="secondaryCard_description_info_date">{{formattedDate}}</div>
        </div>

        <h3>Palestinians call off peace talks after clash</h3>
    </div>

    <div class="secondaryCard_imgWrapper">
        <img src="https://images.unsplash.com/photo-1638913974071-ad0045d13691?ixlib=rb-1.2.1&ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2574&q=80" alt="article img">
    </div>
</div>
</template>

<script>
import dayjs from "dayjs";

export default {
    computed:{
        formattedDate(){
            const date = 1642675620987;
            return dayjs(date).format('MMMM DD, YYYY');
        }
    },
}
</script>

<style lang="scss" >
@import "@/styles/main.scss";

.secondaryCard{
    display: flex;

    padding: 22px 32px !important;

    cursor: pointer;
    
    border-bottom: 1px solid rgba(black, 0.2);

    &:hover{
        background-color: rgba(black, 0.1);
    }

    & > .secondaryCard_description{
        & > .secondaryCard_description_info{
            & > .secondaryCard_description_info_comments{
                @include fontStyle($varelaRound, 10px, normal, 12px, $font_color-gray);
    
                display: flex;
                justify-content: flex-end;
    
                margin-right: 28px;
    
                & > img{
                    width: 10px;
                    height: 10px;

                    margin-right: 4px;
                }
            }
            & > .secondaryCard_description_info_date{
                @include fontStyle($varelaRound, 10px, normal, 12px, $font_color-gray);
            }
        }

        & > h3{
            @include fontStyle($bitter, 14px, bold, 16px, white);
            margin: 8px 8px 0 0;
        }
    }

    & > .secondaryCard_imgWrapper{
        max-width: 70px;
        max-height: 70px;

        & > img{
            width: 100%;
            height: 100%;
            border: 2px solid white;
        }
    }
}
</style>