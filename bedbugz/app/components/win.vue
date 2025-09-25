<template>
    <div class="win">
        <div class="win-profile win-profile-one"></div>

        <span class="win-heart material-symbols-outlined"> favorite </span>
        <span class="win-heart win-heart--med material-symbols-outlined"> favorite </span>
        <span class="win-heart win-heart--sml material-symbols-outlined"> favorite </span>

        <div class="win-title-pos-one">
            <h2 class="win-title font-semibold" data-text="Catch">
                Buzz
            </h2>
        </div>
        <div class="win-title-pos-two">
            <h2 class="win-title font-semibold" data-text="Catch">
                Struck
            </h2>
        </div>
    </div>
</template>

<script>
export default {
    name: "WinComponent"
}
</script>

<style lang="scss">
@import '../main.scss';

.win {
    position: relative;
    height: 300px;
    width: 320px;

    &-heart {
        color: white;
        font-size: 50px;
        transform: rotate(45deg);
        position: absolute;
        top: 20px;
        left: calc(25px + 140px);

        &--med {
            font-size: 40px;
            transform: rotate(15deg);
            top: -20px;
            left: calc(45px + 140px);
        }
        &--sml {
            font-size: 30px;
            transform: rotate(-20deg);
            top: -30px;
            left: calc(15px + 140px);
        }
    }

    &-profile {
        position: absolute;
        background-color: $main-green;
        box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.25);
        border-radius: 25px;
        height: 150px;
        width: 150px;

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
            &-one {
                position: absolute;
                bottom: 78px;
                right: -15px;
            }
            &-two {
                position: absolute;
                bottom: 0;
                left: -5px;
            }
        }
    }
}
</style>