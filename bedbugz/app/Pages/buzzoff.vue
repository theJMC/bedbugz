<template>
    <div class="main-background subpage">
        <div class="subpage-title"> 
            <h1 class="font-semibold font-white font-32"> BedBugZ </h1>
        </div>
        
        <LooseComponent />

        <span class="font-medium font-grad font-20"> 
            They’re not crawling back to you
        </span>

        <div class="subpage-buttons">
            <ButtonElement 
                icon="heart_broken"
                text="return home"
                @click="handleReturnHome"
            />
        </div>
    </div>
</template>

<script>
import ButtonElement from '~/components/button.vue';
import LooseComponent from '~/components/loose.vue';

export default {
    components: {
        ButtonElement,
        LooseComponent
    },
    props: {
        name: {
            type: String,
            default: 'Name'
        }
    },
    methods: {
        handleReturnHome() {
            this.$router.push('/');
        },
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