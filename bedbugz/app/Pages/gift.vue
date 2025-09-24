<template>
  <div class="gift-page">
  <h1 class="font-semibold font-white font-32">BedBugZ</h1>
  <div class="page-content">
  <div class="gift-container">
  <!-- Main gifting content -->
  <svg class="gift-icon" viewBox="0 0 24 24">
  <path fill="url(#gift-gradient)" d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm-2-9h4v2h-4v-2zm-2 2c0 2.21 1.79 4 4 4s4-1.79 4-4H8c0 1.1-.9 2-2 2zm1-5c0 1.1-.9 2-2 2s-2-.9-2-2 .9-2 2-2 2 .9 2 2z"></path>
  <path fill="url(#gift-gradient)" d="M12 11c1.1 0 2 .9 2 2s-.9 2-2 2-2-.9-2-2 .9-2 2-2zm0-5c1.1 0 2 .9 2 2s-.9 2-2 2-2-.9-2-2 .9-2 2-2z"></path>
  <linearGradient id="gift-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
  <stop offset="0%" style="stop-color:rgb(24,217,89);stop-opacity:1" />
  <stop offset="100%" style="stop-color:rgb(216,15,242);stop-opacity:1" />
  </linearGradient>
  </svg>
  
      <h2 class="font-medium font-grad font-20">Choose a gift</h2>
  
      <div class="gift-options">
        <ButtonElement 
          icon="grass"
          class="gift-option"
        />
        <ButtonElement 
          icon="park"
          class="gift-option"
        />
        <ButtonElement 
          icon="forest"
          class="gift-option"
        />
        <ButtonElement 
          icon="water_drop"
          class="gift-option"
        />
        <ButtonElement 
          icon="hive"
          class="gift-option"
        />
      </div>
    </div>
  </div>
  
  </div>
  </template>
  
  <script>
  import ButtonElement from '~/components/button.vue';
  
  export default {
  components: {
  ButtonElement,
  }
  };
  </script>
  
  <style scoped>
  .gift-page {
  display: flex;
  flex-direction: column;
  background: linear-gradient(180deg, #3b006a, #000);
  min-height: 100vh;
  padding: 20px;
  color: white;
  }
  
  .page-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  }
  
  .gift-container {
  background: rgba(255, 255, 255, 0.05);
  border-radius: 20px;
  padding: 16px;
  width: 450px;
  text-align: center;
  position: relative;
  
  /* Flexbox for vertical layout */
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  }
  
  .gift-icon {
  width: 150px;
  height: 150px;
  }
  
  .font-grad {
  background: linear-gradient(135deg, #18D959, #D80FF2);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  color: #18D959; /* Fallback for older browsers */
  }
  
  .gift-options {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 40px;
  width: 100%;
  }
  
  .gift-option {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid transparent;
  background-image: linear-gradient(135deg, #18D959, #D80FF2);
  background-clip: padding-box, border-box;
  background-origin: padding-box, border-box;
  }
  
  .gift-option .material-icons {
font-size: 50px;
color: white;
}
  </style>