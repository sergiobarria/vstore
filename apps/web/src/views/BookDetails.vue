<script setup>
import { useRoute } from 'vue-router';

const route = useRoute();
console.log(route.params);
</script>

<template>
  <div>hello from the book details page: {{ route.params?.bookId }}</div>
</template>
