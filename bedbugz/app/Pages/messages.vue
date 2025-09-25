<template>
    <div class="main-background subpage">
        <div class="subpage-title"> 
            <h1 class="font-semibold font-white font-32"> BedBugZ </h1>
        </div>

        <MessageChain 
            :messageChain="messageChain"
            ref="messageChainContainer"
        />

        <div class="messages-choice">
            <MessageChoices 
                :A="messageIndex == null ? null : optionA.text"
                :B="optionB.text"
                :C="optionC.text"
                @choiceA="checkChoice(optionA.type, $event)"
                @choiceB="checkChoice(optionB.type, $event)"
                @choiceC="checkChoice(optionC.type, $event)"
            />
        </div>
    </div>
</template>

<script>
import MessageChoices from '~/components/messageChoices.vue';
import MessageChain from '~/components/messageChain.vue';
import gsap from 'gsap';

const MIN_USER_SCORE = 40;
export default {
  components: {
    MessageChoices,
    MessageChain
  },
  data() {
    return {
      name: '',
      messages: [],
      messageIndex: null,
      messageChain: [],
      userScore: 0,
      optionA: '',
      optionB: '',
      optionC: '',
    }
  },
  mounted() {
    this.name = localStorage.getItem("suitorName");
    this.getMessages()
  },
  methods: {
    async getMessages() {
        try {
            const response = await fetch(`https://api.bedbugz.uk/chat/sexyeducational${this.name}whodoesntintro`)
            const data = await response.json()
            this.messages = data
            this.chooseResponseOrder(0)
        } catch(error) {
            console.error('Unexpected Error getting messages')
        }
    },
    scrollToBottom() {
        this.$nextTick(() => {
            const container = this.$refs.messageChainContainer?.$el || this.$refs.messageChainContainer;
            if (container) {
                container.scrollTop = container.scrollHeight;
            }
        });
    },
    chooseResponseOrder(index) {
        this.messageChain.push({
            isUser: false,
            message: this.messages[index].bugMsg
        })
        this.scrollToBottom();
        this.messageIndex = index;

        const responses = [
        { type: "good", text: this.messages[index].responses.good },
        { type: "medium", text: this.messages[index].responses.medium },
        { type: "bad", text: this.messages[index].responses.bad }
        ];

        // Shuffle array
        for (let i = responses.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [responses[i], responses[j]] = [responses[j], responses[i]];
        }

        [this.optionA, this.optionB, this.optionC] = responses;
    },
    checkChoice(type, event) {
        switch (type) {
        case "good":
            this.messageChain.push({
                isUser: true,
                message: this.messages[this.messageIndex].responses.good
            })
            this.userScore += 20
            this.explodeEmojis("good", event);
            break;

        case "medium":
            this.messageChain.push({
                isUser: true,
                message: this.messages[this.messageIndex].responses.medium
            })
            this.userScore += 10
            this.explodeEmojis("medium", event);
            break;

        case "bad":
            this.messageChain.push({
                isUser: true,
                message: this.messages[this.messageIndex].responses.bad
            })
            this.explodeEmojis("bad", event);
            break;

        default:
            console.error("Unknown response");
        }

        this.scrollToBottom();

        // 2 second pause before next message
        const currentIndex = this.messageIndex;
        this.messageIndex = null;
        setTimeout(() => {
            this.messageIndex = currentIndex + 1;
            if (this.messageIndex < this.messages.length) {
                this.chooseResponseOrder(this.messageIndex);
            } else {
                this.scoreAndRedirect()
            }
        }, 2000);
    },
    scoreAndRedirect() {
        if (this.userScore >= MIN_USER_SCORE) {
            this.$router.push('/meetup');
        } else {
            this.$router.push('/buzzoff');
        }
    },
    explodeEmojis(type, event) {
    let emojiChars = [];
    if (type === "good") {
        emojiChars = ["❤️", "💕", "💖"];
    } else if (type === "medium") {
        emojiChars = ["🫤", "👌", "🙌"];
    } else if (type === "bad") {
        emojiChars = ["😢", "😒", "😭"];
    }

    const container = this.$refs.messageChainContainer?.$el || this.$refs.messageChainContainer;
    if (!container) return;

    const button = event.currentTarget;
    const rect = button.getBoundingClientRect();
    const centerX = rect.left + rect.width / 2;
    const centerY = rect.top + rect.height - 60; // near bottom of messages

    for (let i = 0; i < 30; i++) {
        const emoji = document.createElement("span");
        emoji.textContent = emojiChars[Math.floor(Math.random() * emojiChars.length)];
        emoji.style.position = "fixed";
        emoji.style.left = centerX + "px";
        emoji.style.top = centerY + "px";
        emoji.style.fontSize = "${500 + Math.random() * 30}px";
        emoji.style.pointerEvents = "none";
        document.body.appendChild(emoji);

        // random trajectory
        const angle = Math.random() * Math.PI * 2;
        const distance = 100 + Math.random() * 80;
        const x = Math.cos(angle) * distance;
        const y = Math.sin(angle) * distance;

        gsap.to(emoji, {
            x,
            y,
            scale: 0,
            opacity: 0,
            rotation: Math.random() * 360,
            duration: 5 + Math.random() * 0.5,
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