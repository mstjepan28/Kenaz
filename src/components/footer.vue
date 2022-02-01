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

        <div class="footer_content_news">
            <div class="featured">
                <h2>Featured</h2>
                <div v-if="articleList">
                    <SecondaryCard 
                        :key="article.id" 
                        :article="article" 
                        v-for="article in articleList.slice(0, 3)"
                    />
                </div>
            </div>
            <div class="randomPost">
                <h2>Random Posts</h2>
                <div v-if="articleList" class="randomPost_container">
                    <SecondaryCard 
                        :key="article.id" 
                        :article="article" 
                        v-for="article in articleList.slice(3, 6)"
                    />
                </div>
            </div>
            <div class="twitterFeed">
                <h2>Twitter Feed</h2>
                <div>

                    <div class="tweet">
                        <div class="user">
                            <img src="@/assets/svg/twitterLogo.svg" alt="Twitter logo">
                            <span class="user_name">Envato</span>
                            <span class="user_userName">@envato</span>
                        </div>
                        <p>
                            Is this your typical million dollar day in the park? http://enva.to/150vxFC  Happy @TrueThemes Day! #ThemeForest pic.twitter.com/EHz7awxOXy
                        </p>
                    </div>
                    <div class="tweet">
                        <div class="user">
                            <img src="@/assets/svg/twitterLogo.svg" alt="Twitter logo">
                            <span class="user_name">Envato</span>
                            <span class="user_userName">@envato</span>
                        </div>
                        <p>
                            Happy TrueThemes Day http://enva.to/1dRzgLD 
                        </p>
                    </div>
                    <div class="tweet">
                        <div class="user">
                            <img src="@/assets/svg/twitterLogo.svg" alt="Twitter logo">
                            <span class="user_name">Envato</span>
                            <span class="user_userName">@envato</span>
                        </div>
                        <p>
                            @robscri I would really want to look into what's taking so long. Thank you ever so much! ^TC
                        </p>
                    </div>

                </div>
            </div>
        </div>

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
import SecondaryCard from "@/components/cards/secondaryCard.vue";

export default {
    components: { SecondaryCard },
    data(){
        return{
            tagList: ["Lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipisicing", "elit", "Voluptatum", "dolor", "voluptatibus", "beatae", "error"],
            articleList: null,
        }
    },
    mounted(){
        this.articleList = this.$store.getters.getArticles(6);
    
        if(!this.articleList){
            this.$store.dispatch("fetchArticleList")
            this.articleList = this.$store.getters.getArticles(6);	
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
        flex-direction: column;

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
                min-height: 52px;

                display: flex;
                align-items: center
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
                & > .tags_container{
                    display: flex;
                    flex-wrap: wrap;

                    padding-top: 24px;
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

        & > .footer_content_news{
            width: 100%;

            display: flex;
            column-gap: 20px;

            margin-top: 68px;
            
            & > *{
                width: 33%;
            }

            h2{
                @include fontStyle($bitter, 24px, bold, 29px, white);
            }

            & .secondaryCard{
                border-bottom: 1px solid #666666;
            }

            & > .twitterFeed{
                & .tweet{
                    padding: 20px 0;

                    p{
                        @include fontStyle($varelaRound, 13px, normal, 18px, #CCCCCC);
                    }

                    & > .user{
                        display: flex;
                        align-items: center;

                        margin-bottom: 12px;

                        .user_name{
                            @include fontStyle($bitter, 14px, normal, 16px, #666666);
                            margin: 0 4px;
                        }
                        .user_userName{
                            @include fontStyle($varelaRound, 14px, normal, 16px, #666666);
                        }
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