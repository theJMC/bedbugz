<template>
  <div class="message-container font-20 font-medium">
    <div
      v-for="(message, index) in messageChain"
      :key="index"
      :class="`message-row ${message.isUser ? 'row-user' : 'row-bug'}`"
    >
      <img 
        v-if="!message.isUser" 
        :src="bugImage" 
        alt="Bug profile" 
        class="profile-photo"
      />

      <div :class="`message message-${message.isUser ? 'user' : 'bug'}`">
        {{ message.message }}
      </div>

      <img 
        v-if="message.isUser" 
        :src="userImage" 
        alt="User profile" 
        class="profile-photo"
      />
    </div>
    <div v-if="messageChain.length == 0 || messageChain.length && messageChain[messageChain.length-1].isUser" class="message-row row-bug">
      <img 
        :src="bugImage" 
        alt="Bug profile" 
        class="profile-photo"
      />
      <div class="message message-bug typing-bubble">
        <span></span><span></span><span></span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MessageChoices",
  props: {
    messageChain: {
      type: Array,
      default: () => ([])
    },
    userImage: {
      type: String,
      default: '/images/user.png'
    },
    bugImage: {
      type: String,
      default: '/images/bug.png'
    }
  }
}
</script>

<style lang="scss">
@import '../main.scss';

.message-container {
  display: flex;
  flex-direction: column;
  gap: 15px;
  width: 95vw;
  height: 50vh;
  overflow-y: scroll;

  scrollbar-width: none;
  ::-webkit-scrollbar { display: none; }
}

.message-row {
  display: flex;
  align-items: flex-end;
  gap: 10px;

  &.row-user {
    justify-content: flex-end;
  }

  &.row-bug {
    justify-content: flex-start;
  }
}

.profile-photo {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  object-fit: cover;
}

.message {
  position: relative;
  max-width: 60%;
  color: white;
  padding: 12px 16px;
  border-radius: 18px;
  text-align: left;
  font-size: 0.95rem;
  line-height: 1.3;

  &-bug {
    background: $main-purple;
    background: $purple-grad;
    border-bottom-left-radius: 4px;
  }
  &-user {
    background: $main-green;
    background: $green-grad;
    border-bottom-right-radius: 4px;
  }
}
</style>
