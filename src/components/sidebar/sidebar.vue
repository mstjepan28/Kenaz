<template>
<aside class="content_sidebar">
    <SidebarContent/>
    <SocialMediaSection/>
    <VideoPlayer :videoLink="'https://www.youtube.com/embed/QhqGCPMfkNM'"/> 

    <div class="bannerContainer">
        <Banner/>
        <Banner/>
    </div>

    <div class="facebookFeed">
        <img src="@/assets/facebookFeedPlaceholder.png" alt="facebook feed placeholder">
    </div>
</aside>
</template>

<script>
import SidebarContent from "@/components/sidebar/sidebarContent.vue";
import SocialMediaSection from "@/components/sidebar/socialMediaSection.vue";
import VideoPlayer from "@/components/sidebar/videoPlayer.vue";
import Banner from "@/components/banner.vue";

export default {
    components: { SidebarContent, SocialMediaSection, VideoPlayer, Banner }
}
</script>

<style lang="scss">
@import "@/styles/main.scss";

.content_sidebar{
    width: 100%;
    max-width: 300px;
    
    & > .bannerContainer{
        display: flex;
        justify-content: space-between;

        padding: 20px;
        margin-top: 16px;

        background-color: $background-darker;

        & > .banner{
            width: 128px;
            height: 128px;

            margin: 0;
        }
    }

    & > .facebookFeed{
        padding: 16px;
        margin-top: 16px;

        background-color: white;

        & > img{
            max-width: 270px;
        }
    }
}
</style>