<template>
  <div>
    <h1>Modal Test Page</h1>
    <ButtonElement icon="open_in_new" text="Open Modal" @click="showModal" />
    <ModalComponent
      :visible="isModalVisible"
      title="Test Modal"
      @update:visible="isModalVisible = $event"
      @close="handleClose"
    >
      <p>This is a test modal body.</p>
      <template #footer>
        <ButtonElement icon="close" text="Close" @click="handleClose" class="modal-button" />
      </template>
    </ModalComponent>
  </div>
</template>

<script>
import ModalComponent from '../Components/modal.vue';
import ButtonElement from '../Components/button.vue';

export default {
  name: 'ModalTestPage',
  components: {
    ModalComponent,
    ButtonElement
  },
  data() {
    return {
      isModalVisible: false
    };
  },
  methods: {
    showModal() {
      this.isModalVisible = true;
    },
    handleClose() {
      this.isModalVisible = false;
    }
  }
}
</script>

<style>
h1 {
  margin-bottom: 1rem;
}

.modal-button{
    font-size:12px;
}
</style>    