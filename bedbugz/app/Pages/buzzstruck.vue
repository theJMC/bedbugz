<template>
    <div class="main-background subpage">
        <div class="subpage-title"> 
            <h1 class="font-semibold font-white font-32"> BedBugZ </h1>
        </div>
        
        <WinComponent />

        <span class="font-medium font-grad font-20"> 
            new suitor unlocked 
            </br> 
            "<span class="font-white">{{ name }}</span>"
        </span>

        <div class="subpage-buttons">
            <ButtonElement 
                icon="favorite"
                text="return home"
            />
        </div>
    </div>
</template>

<script>
import ButtonElement from '~/components/button.vue';
import WinComponent from '~/components/win.vue';

export default {
    components: {
        ButtonElement,
        WinComponent
    }
    props: {
        name: {
            type: String,
            default: 'Name'
        }
    }
}
</script>

<style lang="scss">
.subpage {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;

    &-title {
        margin-top: 15px;
        margin-left: 15px;
        text-align: left;
        align-self: flex-start;
    }

    &-buttons {
        width: 75%;
        margin-bottom: 35px;
    }
}
</style>