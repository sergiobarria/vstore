<script setup>
import AppLogo from '@/components/AppLogo.vue';
import BaseButton from '@/components/BaseButton.vue';

function handleSignUp() {
  console.log('sign up clicked!');
}

const links = [
  {
    id: 1,
    route: '/',
    text: 'home',
    routeName: 'HomeView',
  },
  {
    id: 2,
    route: '/cart',
    text: 'cart',
    routeName: 'CartView',
  },
];
</script>

<template>
  <header class="bg-gray-700 px-4 text-white xl:px-0">
    <div class="container mx-auto max-w-screen-xl">
      <nav class="flex items-center justify-between py-4">
        <app-logo />
        <div class="flex items-center space-x-6">
          <ul class="flex items-center space-x-4">
            <li
              v-for="link in links"
              :key="link.id"
              :class="['duration-150 ease-in-out hover:scale-105']"
            >
              <router-link :to="{ name: link.routeName }" class="capitalize">
                {{ link.text }}
              </router-link>
            </li>
          </ul>
          <base-button @click="handleSignUp">Sign Up</base-button>
        </div>
      </nav>
    </div>
  </header>
</template>
