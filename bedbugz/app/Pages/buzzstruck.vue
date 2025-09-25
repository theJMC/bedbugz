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
                @click="handleReturnHome"
            />
        </div>
    </div>
</template>

<script>
import ButtonElement from '~/components/button.vue';
import WinComponent from '~/components/win.vue';
import gsap from 'gsap';

export default {
    components: {
        ButtonElement,
        WinComponent
    },
    data() {
        return {
            name: ''
        }
    },
    mounted() {
        const centerX = window.innerWidth / 2;
        const centerY = window.innerHeight / 2.3;
        this.explodeEmojis("good", centerX, centerY);
        this.name = localStorage.getItem("suitorName");
    },
    methods: {
        handleReturnHome() {
            this.$router.push('/');
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