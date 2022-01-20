<template>
<h2 class="title">Social</h2>
<ul class="socialMedia">
    <li>
        <img src="@\assets\svg\facebookIcon.svg" alt="Facebook icon">
        <h4>Like</h4>
        <span> 25041 Fans</span>
    </li>    
    <li>
        <img src="@\assets\svg\twitterIcon.svg" alt="Twitter icon">
        <h4>Follow</h4>
        <span> 25041 Followers</span>
    </li>    
    <li>
        <img src="@\assets\svg\youtubeIcon.svg" alt="Youtube icon">
        <h4>Subscribe</h4>
        <span> 941 Subscribers</span>
    </li>    
</ul>
</template>

<script>

export default {

}
</script>

<style lang="scss" scoped>
@import "@/styles/main.scss";

.title{
    @include fontStyle($bitter, 24px, bold, 29px, initial);
}
.socialMedia{
    display: flex;
    flex-direction: column;
    row-gap: 8px;

    margin-top: 16px;
    list-style: none;

    & > li{
        display: flex;
        align-items: stretch;

        & > h4{
            @include fontStyle($bitter, 18px, bold, 18px, initial);
            width: 40%;

            display: flex;
            align-items: center;

            padding-left: 16px;

            background-color: $background-darker;
        }

        & > span{
            @include fontStyle($varelaRound, 14px, normal, 17px, white);

            display: flex;
            align-items: center;
            flex: 1;

            padding-left: 16px;

            background-color: $primary;
        }
    }
}

</style>