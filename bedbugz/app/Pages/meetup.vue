<template>
  <div class="meetup-page">
    <div class="logo">
      <h1 class="font-semibold font-white font-32">BedBugZ</h1>
    </div>

    <div class="scanner">
      <div class="image-container">
        <video
          v-if="!capturedImage"
          ref="video"
          autoplay
          playsinline
          class="scan-image"
        ></video>
        <img
          v-else
          :src="capturedImage"
          alt="Captured"
          class="scan-image"
        />
      </div>

      <ButtonElement 
        icon="camera"
        class="camera-button-style"
        @click="handleCameraClick"
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
  components: { ButtonElement },
  data() {
    return {
      capturedImage: null,
      stream: null,
    };
  },
  mounted() {
    this.startCamera();
  },
  beforeUnmount() {
    this.stopCamera();
  },
  methods: {
    async startCamera() {
      try {
        this.stream = await navigator.mediaDevices.getUserMedia({ video: true });
        this.$refs.video.srcObject = this.stream;
      } catch (err) {
        console.error('Error accessing camera:', err);
      }
    },
    stopCamera() {
      if (this.stream) {
        this.stream.getTracks().forEach(track => track.stop());
      }
    },
    handleCameraClick() {
      if (!this.capturedImage) {
        // Capture current video frame
        const video = this.$refs.video;
        const canvas = document.createElement('canvas');
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
        this.capturedImage = canvas.toDataURL('image/png');

        // Pause the video
        video.pause();
        this.stopCamera();
      } else {
        // Optional: navigate to gift page if already captured
        this.$router.push('/gift');
      }
    }
  }
};
</script>

  
  <style scoped>
  .meetup-page {
    display: flex;
    flex-direction: column;
    align-items: center;
    background: linear-gradient(180deg, #3b006a, #000);
    height: calc(100dvh - 40px);
    padding: 20px;
    color: white;
  }
  .logo {
  align-self: flex-start;
  display: flex;
  justify-content: flex-start;
}
  .scanner {
    background: rgba(255, 255, 255, 0.05);
    border-radius: 20px;
    padding: 16px;
    width: 75%;
    text-align: center;
    position: relative;
  }
  
  .image-container {
    max-height: calc(100dvh - 250px);
    overflow: hidden;
    margin: auto;
  padding: 2px;
  border-radius: 16px;
  background-image: linear-gradient(135deg, #18D959, #D80FF2,#18D959, #D80FF2);
  margin-bottom: 50px;
  }
  
  .scan-image {
  width: 100%;
  height: calc(100dvh - 250px);
  border-radius: 16px;
  object-fit: cover;
  display: block;
  }
  
  .camera-button-style {
    position: absolute;
    bottom: 18%;
    left: 50%;
    transform: translateX(-50%);
    width: fit-content;
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