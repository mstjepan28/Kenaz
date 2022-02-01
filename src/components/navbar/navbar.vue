<template>
    <nav class="navbar">

        <div class="navbar_top_wrapper">
            <ul class="navbar_top_content">
                <li>
                    <router-link to="/" class="container_logo">
                        <span class="logo">
                            <img src="@\assets\logo_white.png" alt="Kenaz logo">
                        </span>
                        <span class="title">Kenaz</span> 
                    </router-link>
                </li>

                <li class="break_element">Media</li> 
                <li>Marketing</li> 
                <li>Contact</li>

                <li class="search">
                    <img src="@\assets\search.png" alt="search icon">
                </li>
            </ul>
        </div>

        <div class="navbar_bottom_wrapper">
            <ul class="navbar_bottom_content">
                <NavbarCategory :key="category.category" :category="category" v-for="category in categoryList" />
            </ul>
        </div>

    </nav>
</template>

<script>
import NavbarCategory from "@/components/navbar/navbarCategory.vue";

export default {
    props: {
        categoryList: {
            type: Object,
            required: true
        },
    },
    components: { NavbarCategory }
}
</script>

<style lang="scss" scoped>
@import "@/styles/main.scss";

.navbar{
    width: 100%;
}

.navbar_top_wrapper,
.navbar_bottom_wrapper{
    display: flex;
    justify-content: center;
}

.navbar_top_content,
.navbar_bottom_content{
    max-width: $content_width;
    width: 100%;

    list-style-type: none;

    display: flex;
}

.navbar_top_wrapper{
    background-color: $secondary;
    
    & > .navbar_top_content{
        display: flex;

        & > li{
            @include fontStyle($varelaRound, 14px, normal, 27px, $font_color);

            display: flex;
            align-items: center;
    
            padding: 12px 8px;

            &:first-child{
                padding: 0;
            }
        }

        & .container_logo{
            display: flex;
            align-self: stretch;
            align-items: center;
            
            & > .logo{
                display: flex;
                align-self: stretch;
                align-items: center;

                padding: 0 24px;

                background-color: $secondary-light; 
    
                & > img{
                    width: 14px;
                    height: 21px;
                }
            }
    
            & > .title{
                @include fontStyle($bitter, 24px, normal, 27px, $font_color);
                align-self: flex-start;
                padding: 16px 0 0 8px;
            }
        }


        & > .break_element{
            margin-left: auto;
        }

        & > .search{
            max-height: 56px;

            padding: 20px 24px;
            background-color: $secondary-light; 
            
            img{
                width: 16px;
                height: 16px;
            }
        }
    }

}

.navbar_bottom_wrapper{
    background-color: $primary;
}



</style>