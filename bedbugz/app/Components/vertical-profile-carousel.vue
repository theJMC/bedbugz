<template>
  <div
    class="vertical-profile-carousel"
    :class="{ 'has-bg': !!activeImage }"
  >
    <div class="slide">
      <div class="nav-btn-group">
        <button
          class="nav-btn up"
          :disabled="currentIndex === 0"
          aria-label="Previous page"
          @click="prevPage"
        >▲</button>
        <button
          class="nav-btn down"
          :disabled="currentIndex === pages.length - 1"
          aria-label="Next page"
          @click="nextPage"
        >▼</button>
      </div>
      <div class="page-content">
        <component
          :is="pages[currentIndex]"
          v-bind="pageProps[currentIndex]"
          @active-image="handleActiveImage"
        />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'VerticalProfileCarousel',
  props: {
    pages: { type: Array, required: true },
    pageProps: { type: Array, default: () => [] }
  },
  data() {
    return {
      currentIndex: 0,
      activeImage: null
    }
  },
  watch: {
    activeImage() {
      this.updateBgImage()
    }
  },
  mounted() {
    this.updateBgImage()
  },
  methods: {
    prevPage() {
      if (this.currentIndex > 0) this.currentIndex--
    },
    nextPage() {
      if (this.currentIndex < this.pages.length - 1) this.currentIndex++
    },
    handleActiveImage(url) {
      this.activeImage = url
      this.updateBgImage()
    },
    updateBgImage() {
      const el = this.$el
      if (el) {
        el.style.setProperty('--carousel-bg', this.activeImage ? `url(${this.activeImage})` : '')
      }
    }
  }
}
</script>

<style lang="scss">
.vertical-profile-carousel {
  position: relative;
  overflow: hidden;
  height: 420px;
  width: 100%;
}
.vertical-profile-carousel.has-bg::before {
  content: '';
  position: absolute;
  inset: 0;
  z-index: 0;
  background-image: var(--carousel-bg);
  background-size: cover;
  background-position: center;
  filter: blur(16px) brightness(0.7);
  transition: background-image 0.3s;
}
.slide, .page-content, .nav-btn-group {
  position: relative;
  z-index: 1;
}
.slide {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: stretch;
  justify-content: stretch;
  height: 100%;
  width: 100%;
  position: relative;
}
.page-content {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
}
.nav-btn-group {
  position: absolute;
  left: 16px;
  bottom: 16px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  z-index: 2;
}
.nav-btn {
  background: rgba(0,0,0,0.4);
  color: white;
  border: none;
  border-radius: 50%;
  width: 32px;
  height: 32px;
  font-size: 1.2em;
  cursor: pointer;
  transition: background 0.2s;
  display: block;
}
.nav-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
</style>