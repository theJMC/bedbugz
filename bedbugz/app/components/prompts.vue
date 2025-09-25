<template>
  <div class="prompts-card">
    <div class="scroll-container">
      <ul>
        <li v-for="(prompt, idx) in prompts" :key="idx" class="prompt-item">
          <div class="prompt-question">{{ prompt.question }}</div>
          <div class="prompt-answer">{{ prompt.answer }}</div>
        </li>
      </ul>
    </div>
  </div>
</template>


<script>
export default {
  name: 'PromptsComponent',
  props: {
    prompts: {
      type: Array,
      required: true
      // Each item: { question: String, answer: String }
    }
  }
}
</script>

<style>
.prompts-card {
  width: 100%;
  margin-top: 32px;
  padding: 18px 24px;
  background: rgba(35, 39, 47, 0.45);
  border-radius: 16px;
  box-shadow: 0 4px 24px rgba(0,0,0,0.18);
  color: #eee;
  backdrop-filter: blur(12px);
  max-height: 400px; /* optional: limit height to trigger scrolling */
}

.scroll-container {
  overflow-y: auto;
  max-height: 340px; /* adjust based on design needs */
  padding-right: 4px; /* prevents content from hiding under scrollbar */
}

/* Scrollbar styles for WebKit browsers */
.scroll-container::-webkit-scrollbar {
  width: 6px;
}

.scroll-container::-webkit-scrollbar-thumb {
  background-color: rgba(255, 255, 255, 0.2);
  border-radius: 3px;
}

.scroll-container::-webkit-scrollbar-track {
  background: transparent;
}

/* Firefox scrollbar */
.scroll-container {
  scrollbar-width: thin;
  scrollbar-color: rgba(255,255,255,0.2) transparent;
}

.prompts-card ul {
  padding-left: 0;
  list-style: none;
  margin: 0;
}

.prompt-item {
  margin-bottom: 18px;
  padding-bottom: 10px;
  border-bottom: 1px solid rgba(255,255,255,0.08);
}

.prompt-question {
  font-weight: 600;
  color: #b3b3b3;
  margin-bottom: 4px;
  font-size: 1.05rem;
}

.prompt-answer {
  color: #fff;
  font-size: 1.08rem;
  margin-left: 20px;
}

</style>