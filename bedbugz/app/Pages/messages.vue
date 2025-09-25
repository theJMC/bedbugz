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
                @choiceA="checkChoice(optionA.type)"
                @choiceB="checkChoice(optionB.type)"
                @choiceC="checkChoice(optionC.type)"
            />
        </div>
    </div>
</template>

<script>
import MessageChoices from '~/components/messageChoices.vue';
import MessageChain from '~/components/messageChain.vue';

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
            const response = await fetch(`https://api.bedbugz.uk/educational${this.name}`)
            const data = await response.json()
            this.messages = data
            this.chooseResponseOrder(0)
        } catch(error) {
            console.error('Unexpected Error')
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
    checkChoice(type) {
        switch (type) {
        case "good":
            this.messageChain.push({
                isUser: true,
                message: this.messages[this.messageIndex].responses.good
            })
            this.userScore += 20
            break;

        case "medium":
            this.messageChain.push({
                isUser: true,
                message: this.messages[this.messageIndex].responses.medium
            })
            this.userScore += 10
            break;

        case "bad":
            this.messageChain.push({
                isUser: true,
                message: this.messages[this.messageIndex].responses.bad
            })
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
            console.log('find a location')
        } else {
            this.$router.push('/buzzoff');
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