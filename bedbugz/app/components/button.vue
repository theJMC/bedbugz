<template>
  <button
    class="button"
    :class="image ? 'button-image' : 'button-stroke'"
  >
    <template v-if="image">
      <img :src="image" alt="" class="button-image-content" />
      <span v-if="text" class="button-image-label">{{ text }}</span>
    </template>

    <template v-else>
      <span class="material-symbols-outlined">
        {{ icon }}
      </span>
      <span class="font-bold font-20">
        {{ text }}
      </span>
    </template>
  </button>
</template>

<script>
export default {
  name: "ButtonElement",
  props: {
    icon: {
      type: String,
      default: "",
    },
    text: {
      type: String,
      default: "",
    },
    image: {
      type: String,
      default: null,
    },
  },
};
</script>

<style lang="scss">
@import "../main.scss";

.button {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;

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
      -webkit-mask: linear-gradient(white 0 0) content-box,
        linear-gradient(white 0 0);
      -webkit-mask-composite: xor;
      mask-composite: exclude;
    }

    &:hover {
      background: $main-bright-grad;
      color: $main-black;
    }
  }

  &-image {
    aspect-ratio: 1 / 1;
    width: 100%;
    border-radius: 16px;
    overflow: hidden;
    position: relative;
    background: $main-black;

    .button-image-content {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }

    .button-image-label {
      position: absolute;
      bottom: 8px;
      left: 50%;
      transform: translateX(-50%);
      background: rgba(0, 0, 0, 0.6);
      color: white;
      font-size: 14px;
      padding: 2px 6px;
      border-radius: 6px;
      white-space: nowrap;
    }
  }
}
</style>