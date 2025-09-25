<template>
  <button
    :class="['image-button', { locked, selected }]"
    @click="$emit('click')"
    :disabled="locked"
  >
    <img :src="image" alt="" class="image-button__img" />
    <span class="image-button__text">{{ text }}</span>

    <!-- Lock overlay -->
    <div v-if="locked" class="image-button__overlay">
      <span class="material-symbols-outlined lock-icon">lock</span>
    </div>
  </button>
</template>

<script>
export default {
  name: "ImageButton",
  props: {
    image: { type: String, required: true },
    text: { type: String, default: "" },
    locked: { type: Boolean, default: false },
    selected: { type: Boolean, default: false },
  },
};
</script>

<style lang="scss">
.image-button {
  position: relative; 
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  border: none;
  border-radius: 25px;
  background-color: black;
  color: white;
  padding: 0;
  cursor: pointer;
  width: 100%;
  aspect-ratio: 1 / 1;
  overflow: hidden;

  &__img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  &__text {
    position: absolute;
    bottom: 8px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 16px;
    font-weight: bold;
    text-align: center;
    color: white;
    text-shadow: 0 0 5px rgba(0, 0, 0, 0.7);
    pointer-events: none;
  }

  &.locked {
    cursor: not-allowed;

    &::after {
      content: "";
      position: absolute;
      inset: 0;
      background-color: rgba(23, 218, 88, 0.5);
    }

    .image-button__overlay {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      color: #17DA58;
      font-size: 32px;
      pointer-events: none;
    }
  }

  &.selected {
    position: relative;
    border-radius: 25px;
    &::before{
        content: "";
        position: absolute;
        inset: 0;
        padding: 7px;
        border-radius: inherit;
        background: linear-gradient(90deg, rgb(19, 223, 85) 0%, rgb(242, 0, 255) 50%, rgb(19, 223, 85) 100%);
        -webkit-mask: linear-gradient(white 0 0) content-box, linear-gradient(white 0 0);
        -webkit-mask-composite: xor;
        mask-composite: exclude;
    }
  }

  &:hover:not(.locked) {
    opacity: 0.9;
  }
}
</style>
