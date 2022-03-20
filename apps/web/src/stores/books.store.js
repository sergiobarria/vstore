import { defineStore } from 'pinia';
// import { useAxios } from '@/composables/useAxios';
import { useAxios } from '@vueuse/integrations/useAxios';
import { axiosInstance } from '@/lib/axiosInstance';

export const useBookStore = defineStore('books', {
  state: () => {
    return {
      books: [],
      isLoading: false,
      error: '',
    };
  },
  getters: {},
  actions: {
    async fetchBooks() {
      try {
        this.isLoading = true;
        const { data } = await useAxios('/books/', axiosInstance);
        // console.log(data.value);

        if (data.value.status === 'success') {
          // console.log(data.value.data);
          this.books = data.value.data;
        }
      } catch (error) {
        console.error(error.message);
      } finally {
        this.isLoading = false;
      }
    },
  },
});
