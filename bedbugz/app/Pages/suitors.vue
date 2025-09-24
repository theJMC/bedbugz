<template>
  <div class="main-background suitor-page">
    <div class="suitor-page-title">
      <h1 class="font-semibold font-white font-32">BedBugZ</h1>
    </div>

    <h2 class="font-medium font-grad font-20">Choose your suitor</h2>

    <!-- Scrollable container -->
    <div class="suitor-page-grid-container">
      <div class="suitor-page-grid">
        <ButtonElement
          v-for="n in 16"
          :key="n"
          :image="'https://lipsum.app/640x640/'"
          :text="`Suitor ${n}`"
        />
      </div>
    </div>
  </div>
</template>

<script>
import ButtonElement from '~/components/button.vue';

export default {
  components: {
    ButtonElement,
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

  /* Container limits the height and makes grid scrollable */
  &-grid-container {
    width: 100%;
    max-width: 350px;
    overflow-y: auto;

    /* Show exactly 3 rows of squares + gaps */
    //max-height: calc(3 * ((350px / 3)) + 2 * 12px); 
    max-height: 400px;
    /* 350px = max container width, 12px = gap */

    &::-webkit-scrollbar {
        display: none;
    }

    scrollbar-width: none;

    /* Hide scrollbar (IE 10+) */
    -ms-overflow-style: none;
  }

  /* Actual grid */
  &-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px; /* same horizontal & vertical */
  }

  /* Grid items are squares */
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
