<template>
  <div class="gift-page">
  <h1 class="font-semibold font-white font-32">BedBugZ</h1>
  <div class="page-content">
  <div class="gift-container">
  <!-- Main gifting content -->
  <svg width="300px" height="35%" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="green-purple-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#18D959"/>
      <stop offset="100%" stop-color="#D80FF2"/>
    </linearGradient>
  </defs>

  <g id="SVGRepo_bgCarrier" stroke-width="0"/>
  <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"/>
  <g id="SVGRepo_iconCarrier">
    <path 
      d="M12 8V21M12 8H7.5C6.83696 8 6.20107 7.73661 5.73223 7.26777C5.26339 6.79893 5 6.16304 5 5.5C5 4.83696 5.26339 4.20107 
      5.73223 3.73223C6.20107 3.26339 6.83696 3 7.5 3C11 3 12 8 12 8ZM12 8H16.5C17.163 8 17.7989 7.73661 18.2678 7.26777C18.7366 6.79893 19 6.16304 19 5.5C19 
      4.83696 18.7366 4.20107 18.2678 3.73223C17.7989 3.26339 17.163 3 16.5 3C13 3 12 8 12 8ZM3 14H21M6.2 21H17.8C18.9201 21 19.4802 21 19.908 20.782C20.2843 
      20.5903 20.5903 20.2843 20.782 19.908C21 19.4802 21 18.9201 21 17.8V11.2C21 10.0799 21 9.51984 20.782 9.09202C20.5903 8.71569 20.2843 8.40973 19.908 8.21799C19.4802 
      8 18.9201 8 17.8 8H6.2C5.0799 8 4.51984 8 4.09202 8.21799C3.71569 8.40973 3.40973 8.71569 3.21799 9.09202C3 9.51984 3 10.0799 3 11.2V17.8C3 18.9201 3 19.4802 3.21799 
      19.908C3.40973 20.2843 3.71569 20.5903 4.09202 20.782C4.51984 21 5.07989 21 6.2 21Z" 
      stroke="url(#green-purple-gradient)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
    />
  </g>
</svg>

  <h2 class="font-semibold font-white font-20">Choose a gift</h2>
  <div class="gift-options">
        <ButtonElement 
          icon="grass"
          class="gift-option"
          :isLarge="true"
          @click="handleGift('grass')"
        />
        <ButtonElement 
          icon="park"
          class="gift-option"
          :isLarge="true"
          @click="handleGift('tree')"
        />
        <ButtonElement 
          icon="local_florist"
          class="gift-option"
          :isLarge="true"
          @click="handleGift('flower')"
        />
        <ButtonElement 
          icon="water_drop"
          class="gift-option"
          :isLarge="true"
          @click="handleGift('water')"
        />
        <ButtonElement 
          icon="hive"
          class="gift-option"
          :isLarge="true"
          @click="handleGift('honey')"
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
  },
  methods: {
    handleGift(giftType) {
      // TODO: add or minus to score based on this and the type of bug
       switch (giftType) {
        case "grass":
            break;
        case "tree":
            break;
        case 'flower':
            break;
        case 'water':
            break;
        case 'honey':
            break;
        default:
            console.error("Unknown response");
        }
      
      // TODO: this should be based on score
      if (true) {
        this.$router.push('/buzzstruck');
      } else {
        this.$router.push('/buzzoff');
      }
    }
  }
  };
  </script>
  
  <style scoped>
  .gift-page {
  display: flex;
  flex-direction: column;
  background: linear-gradient(180deg, #3b006a, #000);
  height: calc(100dvh - 40px);
  padding: 20px;
  color: white;
  }
  
  .page-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  overflow: hidden;
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
  width: 250px;
  height: 250px;
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
  gap: 10px;
  width: 100%;
  }
  
  .gift-option {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  
}

.gift-option .material-symbols-outlined {
  font-size: 200px; /* scales with button */
}
  </style>