<template>
  <div class="percent">
    <b class="percent-number font-bold">
      {{ clampedNumber }}%
    </b>
    <div class="percent-bar">
      <div 
        class="percent-bar__highlight"
        :style="{ width: clampedNumber + '%' }"
      ></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "PercentBar",
  props: {
    number: {
      type: Number,
      default: 0,
    },
  },
  computed: {
    clampedNumber() {
      return Math.min(100, Math.max(0, this.number));
    },
  },
};
</script>

<style lang="scss" scoped>
@import '../main.scss';

.percent {
  display: flex;
  flex-direction: column;
  margin-bottom: 50px;
  width: 90%;

  &-number {
    color: $main-purple;
    text-align: center;
  }

  &-bar {
    width: 100%;
    height: 25px;
    background-color: transparent;
    border-radius: 50px;
    border: 2px solid rgba(255, 255, 255, 0.25);
    box-sizing: border-box;
    box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.25);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    overflow: hidden;

    &__highlight {
        height: 100%;
        border-radius: 25px;
        background-color: $main-purple;
        box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.25);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        transition: width 0.3s ease-in-out;
    }
  }
}
</style>
