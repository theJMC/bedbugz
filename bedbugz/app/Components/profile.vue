<template>
  <div class="profile-card-wrapper">
    <span class="profile-card-border"></span>
    <div
      class="profile-card"
      :style="profileCardStyle"
    >
      <div class="carousel-wrapper">
        <VerticalProfileCarousel
          :pages="carouselPages"
          :pageProps="carouselPageProps"
          @pageChange="onCarouselChange"
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
import CarouselComponent from './carousel.vue'
import DescriptionComponent from './description.vue'
import PromptsComponent from './prompts.vue'

export default {
  name: 'ProfileComponent',
  components: {
    VerticalProfileCarousel
  },
  data() {
    return {
      images: [
        'https://picsum.photos/id/1011/600/400',
        'https://picsum.photos/id/1015/600/400',
        'https://picsum.photos/id/1020/600/400'
      ],
      carouselPages: [
        markRaw(CarouselComponent),
        markRaw(DescriptionComponent),
        markRaw(PromptsComponent)
      ],
      carouselPageProps: [
        { images: [
            'https://picsum.photos/id/1011/600/400',
            'https://picsum.photos/id/1015/600/400',
            'https://picsum.photos/id/1020/600/400'
          ]
        },
        { text: "The bumblebee is a large, fuzzy insect known for its important role in pollination." },
        { prompts: [
                    {
                      "question": "What flowers do bumblebees prefer?",
                      "answer": "Bumblebees love big, easy-to-land-on flowers like lavender and sunflowers. Basically, they’re into the ‘bold and beautiful’ vibe."
                    },
                    {
                      "question": "How do bumblebees communicate?",
                      "answer": "They do the waggle dance! It’s like a bee rave, telling the crew where the best nectar spots are."
                    }
                  ]
        }
      ],
      currentCarouselIndex: 0
    }
  },  
  computed: {
    profileCardStyle() {
      return {} // Remove dynamic background style
    }
  },
  methods: {
    onCarouselChange(index) {
      this.currentCarouselIndex = index
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
