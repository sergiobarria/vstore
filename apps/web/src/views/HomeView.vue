<script setup>
import BookCard from '@/components/BookCard.vue';
import { useBookStore } from '@/stores/books.store';
import { onMounted } from 'vue';

const store = useBookStore();

onMounted(() => {
  store.fetchBooks();
});

console.log(store.books);
</script>

<template>
  <section class="my-8">
    <h2>Latest Products</h2>

    <div class="my-6 grid grid-cols-12">
      <div class="col-span-3">Filters</div>
      <div v-if="store.books.length > 0" :class="['col-span-9 my-4 space-y-6']">
        <div v-for="book in store.books" :key="book.id">
          <BookCard :book="book" />
        </div>
      </div>
      <div v-else class="my-4">Loading...</div>
    </div>
  </section>
</template>
