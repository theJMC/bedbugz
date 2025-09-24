<template>
  <div class="description">
    <h3>Description</h3>
    <p>{{ text }}</p>
  </div>
</template>

<script>
export default {
  name: 'Description',
  props: {
    text: {
      type: String,
      required: true
    }
  }
}
</script>

<style>
.description {
  width: 100%;
  margin: 12px 0;
  font-size: 1rem;
  color: #eee;
}
</style>