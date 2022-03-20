<script setup>
import BookRating from '@/components/BookRating.vue';
import BestsellerBanner from '@/components/BestsellerBanner.vue';

const props = defineProps(['book']);

const { book } = props;
console.log(book);
</script>

<template>
  <article
    :class="[
      'relative flex h-full space-x-4 rounded-md border-[1px] p-4',
      'overflow-hidden',
    ]"
  >
    <router-link :to="{ name: 'BookDetails', params: { bookId: book.id } }">
      <div class="w-36">
        <img :src="book.images[0]?.url" :alt="book.title" class="w-full" />
      </div>
    </router-link>
    <div class="flex w-full flex-col">
      <router-link :to="{ name: 'BookDetails', params: { bookId: book.id } }">
        <h4 class="w-[90%] transition-colors duration-200 hover:text-primary">
          {{ book.title }}
        </h4>
      </router-link>
      <p class="text-sm text-gray-600">
        by
        <span
          v-for="author in book.authors"
          :key="author.id"
          class="text-accent"
        >
          <router-link
            :to="{ name: 'AuthorDetails', params: { authorId: author.id } }"
          >
            {{ author.full_name }}
          </router-link>
          <span class="mx-1 text-gray-700">|</span>
        </span>
        <span>Published on: {{ book.published_year }}</span>
      </p>
      <BookRating :rating="book.rating" />
      <p v-if="book.stock_qty > 0" class="text-green-600">In Stock</p>
      <p v-else class="text-red-600">Out of Stock</p>
      <hr class="my-2" />
      <div v-if="book.hardcover_price">
        <p class="font-semibold text-accent">Hardcover</p>
        <span class="text-xl font-semibold text-gray-700">
          ${{ book.hardcover_price }}
        </span>
      </div>
      <div class="mt-auto">
        <span
          v-for="(genre, i) in book.genres"
          :key="genre.id"
          :class="['text-sm capitalize text-gray-600']"
        >
          {{ genre.name }}
          <!-- prettier-ignore -->
          <span v-if="i + 1 < book.genres.length"> | </span>
        </span>
      </div>
    </div>
    <BestsellerBanner v-if="book.is_bestseller" />
  </article>
</template>
