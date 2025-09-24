<template>
  <div class="meetup-page">
  <h1 class="font-semibold font-white font-32">BedBugZ</h1>
  
  <div class="scanner">
    <div class="image-container">
      <img
        class="scan-image"
        src="/images/flowers.jpg"
        alt="flowers"
      />
    </div>
    <ButtonElement 
      icon="camera"
      class="camera-button-style"
    />
  
    <div class="hint-content">
      <h2 class="font-medium text-white font-20">Hint</h2>
      <p class="hint-text">
        <span class="font-medium font-grad font-20">Bumblebees can’t resist <br></span>
        <span class="font-medium font-grad font-20">lavender blooms</span>
      </p>
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
  }
  </script>
  
  <style scoped>
  .meetup-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  background: linear-gradient(180deg, #3b006a, #000);
  min-height: 100vh;
  padding: 20px;
  color: white;
  }
  
  .scanner {
  background: rgba(255, 255, 255, 0.05);
  border-radius: 20px;
  padding: 16px;
  width: 450px;
  text-align: center;
  position: relative;
  }
  
  .image-container {
  width: 100%;
  padding: 2px;
  border-radius: 16px;
  background-image: linear-gradient(135deg, #18D959, #D80FF2,#18D959, #D80FF2);
  margin-bottom: 50px;
  }
  
  .scan-image {
  width: 100%;
  border-radius: 16px;
  object-fit: cover;
  display: block;
  }
  
  .camera-button-style {
    position: absolute;
bottom: 16%;
left: 50%;
transform: translateX(-50%);
}
  
  .hint-content {
  font-weight: bold;
  }
  
  .hint-text {
  margin-top: 8px;
  font-size: 14px;
  line-height: 1.4;
  }
  
  </style>