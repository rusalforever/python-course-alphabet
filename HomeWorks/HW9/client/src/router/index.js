import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/components/Home';
import Vegetables from '@/components/Vegetables';
import Fruits from '@/components/Fruits';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/Vegetables',
      name: 'Vegetables',
      component: Vegetables,
    },
    {
      path: '/fruits',
      name: 'Fruits',
      component: Fruits,
    },
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
  ],
  mode: 'history',
});
