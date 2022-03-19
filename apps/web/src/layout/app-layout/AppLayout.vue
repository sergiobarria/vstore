<script setup>
import TheNavbar from './TheNavbar.vue';
import TheFooter from './TheFooter.vue';
</script>

<template>
  <the-navbar />
  <main class="mx-auto w-full max-w-screen-xl">
    <router-view />
  </main>
  <the-footer />
</template>
