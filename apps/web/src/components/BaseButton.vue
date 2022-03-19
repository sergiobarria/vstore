<script setup>
const emits = defineEmits(['click']);

function handleClick() {
  emits('click');
}
</script>

<template>
  <button
    type="button"
    @click="handleClick"
    :class="[
      'rounded-lg bg-primary px-4 py-2',
      'transition duration-200 ease-in-out hover:scale-105',
    ]"
  >
    <slot>click me</slot>
  </button>
</template>
