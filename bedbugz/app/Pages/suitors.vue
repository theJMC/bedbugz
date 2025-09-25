<template>
  <div class="main-background suitor-page">
    <div class="suitor-page-title">
      <h1 class="font-semibold font-white font-32">BedBugZ</h1>
    </div>

    <!-- Scrollable container -->
    <div class="suitor-page-grid-container">
      <div class="suitor-page-grid">
        <ImageButton 
            v-for="(suitor, index) in suitors"
            :key="suitor.id"
            :image="suitor.image"
            :text="suitor.name"
            :locked="suitor.locked"
            :selected="selectedSuitorId === suitor.id"
            @click="selectSuitor(suitor)"
        />
      </div>
    </div>

    <div class="suitor-page__confirm-box">
        <h2 class="font-medium font-grad font-20">Choose your suitor</h2>
        <div class="suitor-page__buttons">
          <button
                  class="suitor-page__play-button active"
                  @click="handleReturn"
              >
              <span class="suitor-page__undo-symbol material-symbols-outlined">undo</span>
          </button>  
          <button
                  class="suitor-page__play-button"
                  :class="selectedSuitorId ? 'active' : 'inactive'"
                  :disabled="!selectedSuitorId"
                  @click="handleSelectSuitor"
              >
              <span class="suitor-page__play-symbol material-symbols-outlined">arrow_right</span>
          </button>
        </div>
    </div>
  </div>
</template>

<script>
import imageButton from '~/components/imageButton.vue'; 

export default {
  components: { imageButton },
  data() {
    return {
      selectedSuitorId: null,
      suitors: Array.from({ length: 16 }, (_, i) => ({
        id: i + 1,
        name: `Suitor ${i + 1}`,
        image: 'https://tse4.mm.bing.net/th/id/OIP.2Yp1BvzHL7251IUYAfkEUgHaEx?rs=1&pid=ImgDetMain&o=7&rm=3',
        locked: (i % 3)-2 === 0,
      })),
    };
  },
  methods: {
    selectSuitor(suitor) {
      if (!suitor.locked) {
        this.selectedSuitorId = suitor.id;
      }
    },
    handleSelectSuitor() {
      this.$router.push('/smashOrSquash');
    },
    handleReturn() {
      this.$router.push('/')
    }
  },
};
</script>

<style lang="scss">
.suitor-page {
  display: flex;
  flex-direction: column;
  align-items: center;

  &-title {
    margin-top: 70px;
    text-align: center;
  }

    &__confirm-box {
        display: flex;
        padding-top: 25px;
        flex-direction: column;
        align-items: center;
        gap: 16px
    }

    &__buttons {
      display: flex;
      flex-direction: row;
      gap: 30px;
    }

    &__play-button {
        border-radius: 50%;
        border: none;
        width: 100px;
        height: 100px; 
        text-align: center;
        text-decoration: none;
        display: inline-block;
        display: flex;
        align-items: center;
        justify-content: center;

        &.inactive {
            background: purple;
            cursor: default;
        }

        &.active {
            background: #E110F2;
            cursor:pointer;

            &:hover {
                background-color: purple;
            }
        }
    }

    &__play-symbol {
        font-size:100px;
    }

    &__undo-symbol {
        font-size:50px;
    }

  &-grid-container {

    padding-top: 30px;
    width: 100%;
    max-width: 350px;
    overflow-y: auto;
    max-height: 400px;

    &::-webkit-scrollbar {
        display: none;
    }

    scrollbar-width: none;
    -ms-overflow-style: none;
  }

  &-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
  }

  &-grid > * {
    aspect-ratio: 1 / 1;
    width: 100%;
  }
}

.suitor-page-grid-container {
  -webkit-mask-image: linear-gradient(to bottom, black 0%, black 90%, transparent 100%);
  mask-image: linear-gradient(to bottom, black 0%, black 90%, transparent 100%);
  -webkit-mask-repeat: no-repeat;
  mask-repeat: no-repeat;
}

</style>
