<template>
  <div class="description-card">
    <h3>Description</h3>
    <p class="desc-text">{{ text }}</p>
    <div class="info-row">
      <span class="info-label">Age:</span>
      <span class="info-value">{{ age }}</span>
    </div>
    <div class="info-row">
      <span class="info-label">Looking for:</span>
      <span class="info-value">{{ lookingFor }}</span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DescriptionComponent',
  props: {
    text: {
      type: String,
      required: true
    },
    age: {
      type: [String, Number],
      required: true
    },
    lookingFor: {
      type: String,
      required: true
    }
  }
}
</script>

<style>
.description-card {
  width: 100%;
  margin: 16px 0;
  padding: 18px 24px;
  background: rgba(35, 39, 47, 0.45);
  border-radius: 16px;
  box-shadow: 0 4px 24px rgba(0,0,0,0.18);
  color: #eee;
}

.desc-text {
  margin-bottom: 14px;
  font-size: 1.05rem;
}

.info-row {
  display: flex;
  align-items: center;
  margin-bottom: 6px;
}

.info-label {
  font-weight: 600;
  margin-right: 8px;
  color: #eee;
}

.info-value {
  color: #fff;
}
</style>