<script setup></script>

<template>
  <footer
    :class="[
      'mt-auto flex flex-col items-center justify-center',
      'h-32 w-full',
    ]"
  >
    <p class="text-sm text-gray-600">
      VStore &copy; Copyright {{ new Date().getFullYear() }}
    </p>
  </footer>
</template>
