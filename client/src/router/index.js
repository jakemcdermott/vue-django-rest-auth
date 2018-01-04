import Vue from 'vue';
import Router from 'vue-router';

import About from '../views/About';
import Home from '../views/Home';
import Login from '../views/Login';
import Lost from '../views/Lost';
import PasswordReset from '../views/PasswordReset';
import PasswordResetConfirm from '../views/PasswordResetConfirm';
import Register from '../views/Register';
import VerifyEmail from '../views/VerifyEmail';

import store from '../store';

const redirectUnauthorizedToLogin = (to, from, next) => {
  if (!store.getters['auth/isAuthenticated']) {
    next('/login');
  } else {
    next();
  }
};

const redirectAuthorizedToHome = (to, from, next) => {
  if (store.getters['auth/isAuthenticated']) {
    next('/home');
  } else {
    next();
  }
};

const redirectLogout = (to, from, next) => {
  store.dispatch('auth/logout')
    .then(() => next('/login'));
};

Vue.use(Router);

export default new Router({
  saveScrollPosition: true,
  routes: [
    {
      path: '/about',
      component: About,
      beforeEnter: redirectUnauthorizedToLogin,
    },
    {
      path: '/',
      redirect: '/home',
    },
    {
      path: '/home',
      component: Home,
      beforeEnter: redirectUnauthorizedToLogin,
    },
    {
      path: '/password_reset',
      component: PasswordReset,
    },
    {
      path: '/password_reset/:uid/:token',
      component: PasswordResetConfirm,
    },
    {
      path: '/register',
      component: Register,
    },
    {
      path: '/register/:key',
      component: VerifyEmail,
    },
    {
      path: '/login',
      component: Login,
      beforeEnter: redirectAuthorizedToHome,
    },
    {
      path: '/logout',
      beforeEnter: redirectLogout,
    },
    {
      path: '*',
      component: Lost,
    },
  ],
});
