<template>
    <dialog
        class="main-background modal"
        :open="visible"
        @close="handleClose"
        ref="dialog"
        tabindex="0"
    >
        <div class="modal-header" v-if="title">
            <h3 class="font-white font-32 font-semibold">{{ title }}</h3>
            <button class="modal-close" @click="close">&times;</button>
        </div>
        <div class="modal-body font-white font-medium">
            <slot />
        </div>
        <div class="modal-footer" v-if="$slots.footer">
            <slot name="footer" />
        </div>
    </dialog>
</template>

<script lang="js">
import '../main.scss'
export default {
    name: 'ModalComponent',
    props: {
        visible: {
            type: Boolean,
            default: false
        },
        title: {
            type: String,
            default: ''
        }
    },
    emits: ['update:visible', 'close'],
    watch: {
        visible(val) {
            if (val) {
                this.open();
            } else {
                this.close();
            }
        }
    },
    mounted() {
        if (this.visible) {
            this.open();
        }
    },
    methods: {
        open() {
            if (this.$refs.dialog && !this.$refs.dialog.open) {
                this.$refs.dialog.showModal();
            }
        },
        close() {
            if (this.$refs.dialog && this.$refs.dialog.open) {
                this.$refs.dialog.close();
            }
            this.$emit('update:visible', false);
            this.$emit('close');
        },
        handleClose() {
            this.$emit('update:visible', false);
            this.$emit('close');
        }
    }
}
</script>

<style>
@import '../main.scss';

.modal {
    min-width: 300px;
    max-width: 90vw;
    border-radius: 8px;
    border: none;
    padding: 0;
    box-shadow: 0 2px 16px rgba(0,0,0,0.2);
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    margin-inline: auto;
    height:fit-content !important;
}
.modal-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem;
    border-bottom: 1px solid #eee;
}
.modal-close {
    background: none;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
    color: white;
}
.modal-body {
    padding: 1rem;
}
.modal-footer {
    padding: 1rem;
    border-top: 1px solid #eee;
    text-align: right;
}
</style>