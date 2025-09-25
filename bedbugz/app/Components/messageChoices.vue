<template>
    <div 
        v-if="A == null || B == null || C == null" 
        class="choice-container"
    >
        <div 
            class="choice typing-bubble"
        >
            <span></span><span></span><span></span>
        </div>

        <div 
            class="choice typing-bubble"
        >
            <span></span><span></span><span></span>
        </div>

        <div 
            class="choice typing-bubble"
        >
            <span></span><span></span><span></span>
        </div>
    </div>

    <div 
        class="choice-container"
        v-else
    >
        <button 
            class="choice font-medium"
            @click="$emit('choiceA', $event)"
        >
            {{ A }}
        </button>

        <button 
            class="choice font-medium"
            @click="$emit('choiceB', $event)"
        >
            {{ B }}
        </button>

        <button 
            class="choice font-medium"
            @click="$emit('choiceC', $event)"
        >
            {{ C }}
        </button>
    </div>
</template>

<script>
export default {
    name: "MessageChoices",
    props: {
        A: {
            type: String
        },
        B: {
            type: String
        },
        C: {
            type: String
        }
    }
}
</script>

<style lang="scss">
@import '../main.scss';

.choice {
    position: relative;
    background: $main-green;
    background: $green-grad;
    color: white;
    padding: 30px 5px;
    border-radius: 10px;
    margin-bottom: 50px;
    text-align: center;
    width: 100%;

    &:hover {
        opacity: 0.8;
    }

    &::after {
        content: "";
        position: absolute;
        bottom: -18px;
        left: 50%;
        transform: translateX(-50%);
        border-width: 10px;
        border-style: solid;
        border-color: $main-green transparent transparent transparent;
    }

    &-container {
        display: flex;
        gap: 5px;
        width: 95vw;
    }
}

</style>