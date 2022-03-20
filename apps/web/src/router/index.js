import { createRouter, createWebHistory } from 'vue-router';

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: () => import('@/views/HomeView.vue'),
  },
  {
    path: '/cart',
    name: 'CartView',
    component: () => import('@/views/CartView.vue'),
  },
  {
    path: '/books/:bookId',
    name: 'BookDetails',
    component: () => import('@/views/BookDetails.vue'),
  },
  {
    path: '/authors/:authorId',
    name: 'AuthorDetails',
    component: () => import('@/views/AuthorDetails.vue'),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
