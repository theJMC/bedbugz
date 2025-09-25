<template>
  <div class="carousel" @click="handleClick">
    <img :src="images[currentIndex]" alt="profile image" class="pointer-events-none"/>
    <!-- progress dots -->
    <div class="dots">
      <span
        v-for="(img, index) in images"
        :key="index"
        :class="{ active: index === currentIndex }"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: 'CarouselComponent',
  props: {
    images: {
      type: Array,
      required: true
    }
  },
emits: ['active-image'],
  data() {
    return {
      currentIndex: 0
    }
  },
  watch: {
    currentIndex(newIdx) {
      this.$emit('active-image', this.images[newIdx])
    }
  },
  mounted() {
    this.$emit('active-image', this.images[this.currentIndex])
  },
  methods: {
    handleClick(event) {
      const { offsetX, target } = event
      const midPoint = target.clientWidth / 2

      if (offsetX < midPoint) {
        // tap left → previous image
        this.prev()
      } else {
        // tap right → next image
        this.next()
      }
    },
    next() {
      if (this.currentIndex < this.images.length - 1) {
        this.currentIndex++
      } else {
        this.currentIndex = 0 // loop
      }
    },
    prev() {
      if (this.currentIndex > 0) {
        this.currentIndex--
      } else {
        this.currentIndex = this.images.length - 1 // loop
      }
    }
  }
}
</script>

<style lang="scss">
.carousel {
  position: relative;
  width: 100%;
  height: 420px;
  border-radius: 16px;
  overflow: hidden;
  cursor: pointer;

}

.carousel img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.dots {
  position: absolute;
  bottom: 10px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 6px;
}

.dots span {
  width: 8px;
  height: 8px;
  background: rgba(255, 255, 255, 0.5);
  border-radius: 50%;
}

.dots span.active {
  background: white;
}
</style>
