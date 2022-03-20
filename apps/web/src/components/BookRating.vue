<script setup>
import { StarIcon as StarSolid } from '@heroicons/vue/solid';
import { StarIcon as StarOutline } from '@heroicons/vue/outline';

const props = defineProps(['rating']);

const stars = Math.round(props.rating);
</script>

<template>
  <div class="flex items-center space-x-2 text-gray-700">
    <p class="flex items-center text-yellow-400">
      <span v-for="_ in stars">
        <StarSolid class="h-5 w-5" />
      </span>
      <span v-for="_ in 5 - stars">
        <StarOutline class="h-5 w-5" />
      </span>
    </p>
    <p>{{ rating }} out of 5.0</p>
  </div>
</template>
