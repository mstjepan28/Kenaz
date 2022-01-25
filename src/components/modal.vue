<template>
  	<div :id="id" class="modal_background" @click="closeModal()">
        <div class="modal" @click.stop>
            <div class="modal_body"></div>
        </div>
    </div>
</template>

<script>

export default {
    props:{
        id: {
            type: String,
            required: true,
        }
    },
    methods:{
        openWithImg(imgURL){
            let imgElement = document.getElementById(`${this.id}Image`)

            if(!imgElement){
                imgElement = document.createElement("img");
                imgElement.id = `${this.id}Image`

                imgElement.style.maxWidth = "100%";
                imgElement.style.maxHeight = "100%";

                imgElement.classList.add("modal_showImg")

                document.querySelector(`#${this.id} .modal_body`).appendChild(imgElement)
            }

            imgElement.src = imgURL;
            

            this.openModal();
        },
        openModal(){
            const modal = document.getElementById(this.id);
            modal.style.display = "flex";

            document.body.style.overflow = "hidden";
        },
        closeModal(){
            const modal = document.getElementById(this.id);
            modal.style.display = "none";

            document.body.style.overflow = "";
        },
    }
}
</script>

<style lang="scss" scoped>
$modal_animation-speed: 0.4s;

.modal_background{
    width: 100vw;
    height: 100vh;

    display: none;
    align-items: center;
    justify-content: center;

    position: fixed;
    z-index: 9999;

    background-color: rgba(128,128,128,0.75);
    
    animation: fadeIn $modal_animation-speed linear;
}

.modal{
    max-width: 1140px;
    max-height: 600px;
    min-height: 350px;

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

    background: white;

    animation: scaleUp $modal_animation-speed linear;

    .modal_showImg{
        max-width: 1040px;
        max-height: 500px;
    }
}



@keyframes fadeIn{
	from {
        opacity: 0
    } 
	to {
        opacity: 1
    }
}

@keyframes scaleUp{
    0%{
        transform:scale(.5);
    }
    100%{
        transform:scale(1);
    }
}
</style>
