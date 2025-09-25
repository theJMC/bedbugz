<template>
    <div class="main-background subpage">
        <div class="subpage-title"> 
            <h1 class="font-semibold font-white font-32"> BedBugZ </h1>
        </div>
        
        <MatchComponent />

        <div class="subpage-buttons">
            <ButtonElement 
                icon="favorite"
                text="get chatting"
                @click="handleGetChatting"
            />
        </div>
    </div>
</template>

<script>
import ButtonElement from '~/components/button.vue';
import MatchComponent from '~/components/match.vue';

export default {
    components: {
        ButtonElement,
        MatchComponent
    },
    methods: {
        handleGetChatting() {
            this.$router.push('/messages');
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