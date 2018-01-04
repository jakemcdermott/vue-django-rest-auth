<template>
  <div id="login-view">
    <h1>Login</h1>
    <form @submit.prevent="submit">
      <input v-model="inputs.username" type="text" id="username" placeholder="username">
      <input v-model="inputs.password" type="password" id="password" placeholder="password">
    </form>
    <button @click="login(inputs)" id="login-button">
      login
    </button>
    <div>
      <router-link to="/register">create account</router-link> |
      <router-link to="/password_reset">reset password</router-link>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      inputs: {
        username: '',
        password: '',
      },
    };
  },
  methods: {
    login({ username, password }) {
      this.$store.dispatch('auth/login', { username, password })
        .then(() => this.$router.push('/'));
    },
  },
};
</script>

<style>
form input {
  display: block
}
</style>
