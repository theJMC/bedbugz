<template>
  <div class="prompts">
    <h3>Prompts</h3>
    <ul>
      <li v-for="(prompt, idx) in prompts" :key="idx">{{ prompt }}</li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'Prompts',
  props: {
    prompts: {
      type: Array,
      required: true
    }
  }
}
</script>

<style >
.prompts {
  width: 100%;
  margin: 12px 0;
  font-size: 1rem;
  color: #eee;
}
.prompts ul {
  padding-left: 18px;
}
</style>