<template>
  <div class="main-background date-spots-page">
    <div class="date-spots-page-title">
      <h1 class="font-semibold font-white font-32">BedBugZ</h1>
    </div>

    <!-- Scrollable container -->
    <div class="date-spots-page-grid-container">
      <div class="date-spots-page-grid">
        <ImageButton 
            v-for="(dateSpot, index) in dateSpots"
            :key="dateSpot.id"
            :image="dateSpot.image"
            :text="dateSpot.name"
        />
      </div>
    </div>

    <div class="date-spots-page__confirm-box">
        <h2 class="font-medium font-grad font-20">view your date spots</h2>
            <button
                class="date-spots-page__play-button active"
                @click="handleReturn"
            >
            <span class="date-spots-page__play-symbol material-symbols-outlined">undo</span>
        </button>
    </div>
  </div>
</template>

<script>
import imageButton from '~/components/imageButton.vue'; 

export default {
  components: { imageButton },
  data() {
    return {
      selecteddateSpotId: null,
      dateSpots: Array.from({ length: 16 }, (_, i) => ({
        id: i + 1,
        name: `Plant`,
        image: 'https://watchandlearn.scholastic.com/content/dam/classroom-magazines/watchandlearn/videos/animals-and-plants/plants/what-are-plants-/What-Are-Plants.jpg',
        locked: (i % 3)-2 === 0,
      })),
    };
  },
  methods: {
    selectdateSpot(dateSpot) {
      if (!dateSpot.locked) {
        this.selecteddateSpotId = dateSpot.id;
      }
    },
    handleReturn() {
      this.$router.push('/');
    }
  },
};
</script>

<style lang="scss">
.date-spots-page {
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

.date-spots-page-grid-container {
  -webkit-mask-image: linear-gradient(to bottom, black 0%, black 90%, transparent 100%);
  mask-image: linear-gradient(to bottom, black 0%, black 90%, transparent 100%);
  -webkit-mask-repeat: no-repeat;
  mask-repeat: no-repeat;
}

</style>
