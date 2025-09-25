<template>
    <div class="match">
        <div class="match-profile match-profile-one">
            <img :src="suitorImg" alt="profile image" class="pointer-events-none"/>
        </div>
        <div class="match-profile match-profile-two">
            <img :src="userImage" alt="profile image" class="pointer-events-none"/>
        </div>

        <span class="match-heart material-symbols-outlined"> favorite </span>

        <span class="match-subtitle font-semibold font-white font-32">
            IT'S A
        </span>
        <div class="match-title-pos">
            <h2 class="match-title font-semibold" data-text="Catch">
                Catch
            </h2>
        </div>
    </div>
</template>

<script>
export default {
    name: "MatchComponent",
    data() {
        return {
            suitorImg: '',
            userImage: '',
        }
    },
    mounted() {
        this.suitorImg = localStorage.getItem("suitorImg");
        this.userImage = localStorage.getItem("userImg");
    }
}
</script>

<style lang="scss">
@import '../main.scss';

.match {
    position: relative;
    height: 340px;
    width: 320px;

    &-heart {
        color: white;
        font-size: 50px;
        transform: rotate(45deg);
        position: absolute;
        top: 20px;
        left: calc(25px + 140px);
    }

    &-profile {
        position: absolute;
        overflow: hidden;
        background-color: $main-green;
        box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.25);
        border-radius: 25px;
        height: 150px;
        width: 150px;

        img {
            object-fit: cover;
            display: block;
            width: 100%;
            height: 100%;
        }

        &-one {
            top: 0;
            left: 15px;
        }

        &-two {
            top: 70px;
            left: calc(15px + 140px);
        }
    }

    &-subtitle {
        position: absolute;
        bottom: 96px;
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