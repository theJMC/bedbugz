<template>
    <button class="button button-stroke">
        <span :class="`material-symbols-outlined font-${isLarge ? '50' : '20'}`">
            {{ icon }}
        </span>
        <span :class="`font-bold font-${isLarge ? '50' : '20'}`">
            {{ text }}
        </span>
    </button>
</template>

<script>
export default {
    name: "ButtonElement",
    props: {
        icon: {
            type: String
        },
        text: {
            type: String, 
            default: ''
        },
        isLarge: {
            type: Boolean,
            default: false
        }
    }
}
</script>

<style lang="scss">
@import '../main.scss';

.button {
    display: flex;
    flex-direction: column;
    width: 100%;
    
    &-stroke {
        position: relative;
        border-radius: 25px;
        padding: 16px;
        background: $main-black;
        color: white;
        
        &::before {
            content: "";
            position: absolute;
            inset: 0;
            padding: 2px;
            border-radius: inherit;
            background: $main-bright-grad;
            -webkit-mask: 
                linear-gradient(white 0 0) content-box, 
                linear-gradient(white 0 0);
            -webkit-mask-composite: xor;
            mask-composite: exclude;
        }

        &:hover {
            background: $main-bright-grad;
            color: $main-black;
        }
    }
}
</style>