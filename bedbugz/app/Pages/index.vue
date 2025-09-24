<template>
    <div class="main-background homepage">
        <div class="homepage-title"> 
            <h1 class="font-semibold font-white font-32"> BedBugZ </h1>
            <h2 class="font-medium font-grad font-20"> bug bites to love bites </h2>
        </div>
        <div class="homepage-buttons">
            <ButtonElement 
                icon="favorite"
                text="find a match"
            />
            <ButtonElement 
                icon="park"
                text="view date spots"
            />
            <ButtonElement 
                icon="pest_control"
                text="scan a suitor"
            />
        </div>
        <PercentBar 
            number=33
        />
    </div>
</template>

<script>
import ButtonElement from '~/components/button.vue';
import PercentBar from '~/components/percent.vue';

export default {
    components: {
        ButtonElement,
        PercentBar
    }
}
</script>

<style lang="scss">
.homepage {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;

    &-title {
        margin-top: 70px;
        text-align: center;
    }

    &-buttons {
        display: flex;
        flex-direction: column;
        gap: 10px;
        width: 75%;
    }
}
</style>