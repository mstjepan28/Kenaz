<template>
<footer class="footer">
    <div class="footer_topStrip"></div>

    <div class="footer_content">
        <div class="footer_content_about">
            <div class="aboutUs">
                <span class="title">
                    <img src="@/assets/logo.png" alt="logo">
                    <h2>Kenaz</h2>
                </span>

                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus leo ante.</p>

                <div class="socialMediaIcons">
                    <img src="@/assets/svg/rssIcon.svg" alt="Rss logo">
                    <img src="@/assets/svg/facebookIcon.svg" alt="Facebook logo">
                    <img src="@/assets/svg/twitterIcon.svg" alt="Twitter logo">
                    <img src="@/assets/svg/dribbleIcon.svg" alt="Dribble logo">
                    <img src="@/assets/svg/linkedinIcon.svg" alt="Linkedin logo">
                    <img src="@/assets/svg/youtubeIcon.svg" alt="Youtube logo">
                    <img src="@/assets/svg/skypeIcon.svg" alt="Skype logo">
                </div>
            </div>

            <div class="newsLetterSignup">
                <h2>Newsletter</h2>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus leo ante...</p>

                <form @submit.prevent>
                    <input type="email" placeholder="Your mail">
                    <button type="submit"> Subscribe </button>
                </form>
            </div>

            <div class="tags">
                <h2>Tags Widget</h2>

                <div class="tags_container">
                    <span class="tag" :key="tag" v-for="tag in tagList">{{tag}}</span>
                </div>
            </div>
        </div>
        <div class="footer_content_news"></div>
    </div>
    
    <div class="footer_misc">
        <div>        
            <span>© 2013 - Kenaz Template - Proudly made at Plava tvornica Croatia</span>
            <span>
                <span>Typography</span> - <span>Templates</span> - <span>Contact Form</span> - <span>404 Page</span>
            </span>
        </div>
        
    </div>
</footer>
</template>

<script>

export default {
    data(){
        return{
            tagList: ["Lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipisicing", "elit", "Voluptatum", "dolor", "voluptatibus", "beatae", "error"]
        }
    }

}

</script>

<style lang="scss" scoped>
@import "@/styles/main.scss";

.footer{
    width: 100%;

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

    background-color: $secondary;

    & > .footer_topStrip{
        width: 100%;
        height: 24px;

        background-color: $primary;
    }

    & > .footer_content{
        width: 100%;
        max-width: $content_width;

        display: flex;
        justify-content: center;

        padding: 56px 0 68px 0;

        & > .footer_content_about{
            width: 100%;

            display: flex;
            column-gap: 10px;
            
            & > *{
                width: 33%;
            }

            & h2{
                @include fontStyle($bitter, 24px, bold, 29px, #CCCCCC);
            }
            & p{
                @include fontStyle($bitter, 14px, normal, 20px, #666666);
                padding: 24px 0;
            }

            & > .aboutUs{

                & > .title{
                    display: flex;

                    & > img{
                        width: 28px;
                    }

                    & > h2{
                        @include fontStyle($bitter, 30px, normal, 52px, #45B0E3);
                        margin-left: 16px;
                    }
                }
                & > .socialMediaIcons{
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                    

                    & > img{
                        width: 38px;
                        height: 38px;
                    }
                }
            }

            & > .newsLetterSignup > form{
                display: flex;

                & > input{
                    @include fontStyle($varelaRound, 16px, normal, 19px, #999999);
                    max-width: 192px;

                    padding: 16px 20px;
                    border: none;
                    background-color: #333333;
                }

                & > button{
                    @include fontStyle($varelaRound, 16px, normal, 19px, #999999);

                    padding: 16px 20px;
                    border: none;
                    background-color: $primary;

                    cursor: pointer;
                }
            }

            & > .tags{

                h2{
                    margin-bottom: 36px;
                }

                & > .tags_container{
                    display: flex;
                    flex-wrap: wrap
                }

                & .tag{
                    @include fontStyle($varelaRound, 12, normal, 20px, #666666);
                    max-width: fit-content;

                    padding: 4px 12px;
                    margin: 0 4px 4px 0;

                    background-color: #333333;

                    &:hover{
                        color: #CCCCCC;
                        cursor: pointer;
                        background-color: $primary;
                    }
                }
            }
        }
    }

    & > .footer_misc{
        width: 100%;

        display: flex;
        justify-content: center;

        padding: 20px 0 120px 0;
    
        border-top: 1px solid #333333;

        & > div{
            width: 100%;
            max-width: $content_width;

            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        & span{
            @include fontStyle($varelaRound, 12px, normal, 14.5px, #999999);
        }
    }
}
</style>