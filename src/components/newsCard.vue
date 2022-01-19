<template>
<div class="card">
    <img class="card_image" src="https://images.unsplash.com/photo-1593642632559-0c6d3fc62b89?ixlib=rb-1.2.1&ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1769&q=80" alt="">
    
    <div class="card_info">
        <span class="card_info_date">August 26, 2013</span>
        <span class="card_info_number">14</span>
    </div>
    
    <h3 class="card_title">
        For Obama, MLK's shadow looms large ahead of speech
    </h3>
</div>
</template>

<script>

export default {

}
</script>

<style lang="scss" scoped>

.card{
    max-width: 170px;
    min-height: 220px;

    & > .card_image{
        max-width: 100%;
        max-height: 128px;
    }

    & > .card_info{
        display: flex;
        justify-content: space-between;

        margin: 8px 0;

        & > *{
            font-family: "Varela Round";
            font-size: 12px;
            font-weight: 400;
            line-height: 14px;
        }
    }

    & > .card_title{
        font-family: Bitter;
        font-size: 14px;
        font-weight: 700;
        line-height: 18px;
    }
}

</style>