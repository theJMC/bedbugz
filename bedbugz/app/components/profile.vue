<template>
  <div class="profile-card-wrapper">
    <span class="profile-card-border"></span>
    <div
      class="profile-card"
      :style="profileCardStyle"
    >
      <div class="carousel-wrapper">
        <VerticalProfileCarousel
          :key="profile.name"
          :pages="carouselPages"
          :pageProps="carouselPageProps"
          @pageChange="onCarouselChange"
        />
        <div class="overlay">
          <h2 class="font-semibold font-24 font-transparent">{{ profile?.name }}</h2>
          <p class="font-semibold font-14 font-white"><i>{{ profile?.species }}</i></p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import VerticalProfileCarousel from './vertical-profile-carousel.vue'
import CarouselComponent from './carousel.vue'
import DescriptionComponent from './description.vue'
import PromptsComponent from './prompts.vue'
import { markRaw } from 'vue'

export default {
  name: 'ProfileComponent',
  components: {
    VerticalProfileCarousel
  },
  props: {
    profile: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      currentCarouselIndex: 0
    }
  },
  computed: {
    carouselPages() {
      return [
        markRaw(CarouselComponent),
        markRaw(DescriptionComponent),
        markRaw(PromptsComponent)
      ]
    },
    carouselPageProps() {
      return [
        { images: this.profile?.images || [] },
        { text: this.profile?.description || '' },
        { prompts: this.profile?.prompts || [] }
      ]
    },
    profileCardStyle() {
      return {}
    }
  },
  methods: {
    onCarouselChange(index) {   
      this.currentCarouselIndex = index
    }
  },
  watch: {
    profile: {
      handler() {
        this.currentCarouselIndex = 0;
      },
      immediate: true
    }
  }
}
</script>

<style lang="scss">
.profile-card-wrapper {
  position: relative;
  width: 262px;
  margin: auto;
}

.profile-card-border {
  position: absolute;
  top: -8px;
  left: -8px;
  width: calc(100% - 32px);
  height: calc(100% - 46px);
  border-radius: 24px;
  border: 2px solid #ffffff40;
  pointer-events: none;
}

.profile-card {
  height: 420px;
  border-radius: 20px;
  color: white;
  padding: 12px;
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  overflow-y: auto;
  padding-bottom: 24px;
  background: inherit;
  z-index: 1;
}

.header {
  text-align: left;
  width: 100%;
  font-weight: bold;
  margin-bottom: 8px;
}

.carousel-wrapper {
  position: relative;
  width: 100%;
  border-radius: 20px;
  overflow: hidden;
}

.overlay {
  position: absolute;
  top: 8px;
  right: 12px;
  color: white;
  text-shadow: 0 2px 4px rgba(0,0,0,0.6);
  z-index: 2;
}

.footer {
  display: flex;
  justify-content: space-around;
  width: 100%;
  margin-top: 12px;
}

.footer button {
  flex: 1;
  margin: 0 4px;
  border: none;
  padding: 10px;
  border-radius: 12px;
  font-weight: bold;
  cursor: pointer;
}

.smash {
  background: #ff3d3d;
  color: white;
}

.squash {
  background: #4caf50;
  color: white;
}
</style>
