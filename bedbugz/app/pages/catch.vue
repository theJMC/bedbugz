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
import gsap from 'gsap';

export default {
    components: {
        ButtonElement,
        MatchComponent
    },
    mounted() {
        const centerX = window.innerWidth / 2.3;
        const centerY = window.innerHeight / 2.7;
        this.explodeEmojis("good", centerX, centerY);
        this.name = localStorage.getItem("suitorName");
    },
    methods: {
        handleGetChatting() {
            this.$router.push('/messages');
        },
        explodeEmojis(type, x, y) {
            let emojiChars = [];
            if (type === "good") {
                emojiChars = ["❤️", "🐞","🐜","🐝"];
            }

            for (let i = 0; i < 40; i++) {
                const emoji = document.createElement("span");
                emoji.textContent =
                emojiChars[Math.floor(Math.random() * emojiChars.length)];
                emoji.style.position = "fixed";
                emoji.style.left = x + "px";
                emoji.style.top = y + "px";
                emoji.style.fontSize = `${32 + Math.random() * 20}px`;
                emoji.style.pointerEvents = "none";
                document.body.appendChild(emoji);

                const angle = Math.random() * Math.PI * 2;
                const distance = 150 + Math.random() * 150;
                const dx = Math.cos(angle) * distance;
                const dy = Math.sin(angle) * distance;

                gsap.to(emoji, {
                x: dx,
                y: dy,
                scale: 0.6,
                opacity: 0,
                rotation: Math.random() * 720,
                duration: 3 + Math.random() * 1,
                ease: "power2.out",
                onComplete: () => emoji.remove()
                });
            }
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