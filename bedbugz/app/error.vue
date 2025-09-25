<template>
    <div class="main-background subpage errorpage">
        <div class="subpage-title"> 
            <h1 class="font-semibold font-white font-32"> BedBugZ </h1>
        </div>

            <div class="error">
        <span class="error-subtitle font-semibold font-white font-32">
            {{ error.statusCode || 500 }}
        </span>
        <div class="error-title-pos">
            <h2 class="error-title font-semibold" data-text="Catch">
                Splat!
            </h2>
        </div>
    </div>

    <div class="errorpage__text">
        <h3 class="font-medium font-grad font-24">
            {{ error.message || 'Something went wrong.' }}
        </h3>
        <h3 class="errorpage__bottom font-medium font-white font-20">
            <NuxtLink to="/">Go back home</NuxtLink>
        </h3>
    </div>
    </div>
</template>

<script>
export default {
    name: "errorComponent",
    props: {
    }
}
</script>

<script setup>
defineProps({
  error: Object
})
</script>

<style lang="scss">
@import '~/main.scss';
.errorpage {
    height: 100dvh;

    &__text {
        display: flex;
        flex-direction: column;
        text-align: center;
        align-items: center;
        gap: 5px;
        margin-bottom: 100px;
    }
}
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
.error {
    position: relative;
    height: 160px;
    width: 320px;

    &-subtitle {
        position: absolute;
        bottom: 110px;
        left: 35px;
    }

    &-title {
        font-size: 96px;
        font-weight: bold;
        position: relative;
        -webkit-text-stroke: 15px transparent;
        background: $main-bright-grad;
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: white;
        padding: 0 20px;

        &-pos {
            position: absolute;
            bottom: 0;
            left: -5px;
        }
    }
}
</style>