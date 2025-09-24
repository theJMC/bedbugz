<template>
  <div class="profile-card-wrapper">
    <span class="profile-card-border"></span>
    <div class="profile-card">
      <div class="carousel-wrapper">
        <VerticalProfileCarousel
          :pages="carouselPages"
          :pageProps="carouselPageProps"
        />
        <div class="overlay">
          <h2>Bumblebee</h2>
          <p><i>Bombus terrestris</i></p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import VerticalProfileCarousel from './vertical-profile-carousel.vue'
import Carousel from './carousel.vue'
import Description from './description.vue'
import Prompts from './prompts.vue'

export default {
  name: 'Profile',
  components: {
    VerticalProfileCarousel,
    Carousel,
    Description,
    Prompts
  },
  data() {
    return {
      images: [
        'https://picsum.photos/id/1011/600/400',
        'https://picsum.photos/id/1015/600/400',
        'https://picsum.photos/id/1020/600/400'
      ],
      carouselPages: [
        Carousel,      // Use the imported component
        Description,   // Use the imported component
        Prompts        // Use the imported component
      ],
      carouselPageProps: [
        { images: [
            'https://picsum.photos/id/1011/600/400',
            'https://picsum.photos/id/1015/600/400',
            'https://picsum.photos/id/1020/600/400'
          ]
        },
        { text: "The bumblebee is a large, fuzzy insect known for its important role in pollination." },
        { prompts: ['What flowers do bumblebees prefer?', 'How do bumblebees communicate?'] }
      ]
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
  border: 2px solid white;
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
