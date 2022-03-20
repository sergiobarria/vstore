<script setup>
import { useRoute } from 'vue-router';

const route = useRoute();
console.log(route.params);
</script>

<template>
  <div>hello from the author details page: {{ route.params?.authorId }}</div>
</template>
