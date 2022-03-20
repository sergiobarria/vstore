<script setup>
import AppNavbar from './AppNavbar.vue';
import AppFooter from './AppFooter.vue';
</script>

<template>
  <AppNavbar />
  <main class="mx-auto w-full max-w-screen-xl">
    <router-view />
  </main>
  <AppFooter />
</template>
