<template>
  <div id="register-view">
    <h1>Create Account</h1>
    <template v-if="registrationLoading">
      loading...
    </template>
    <template v-else-if="!registrationCompleted">
      <form @submit.prevent="submit">
        <input v-model="inputs.username" type="text" id="username" placeholder="username">
        <input v-model="inputs.password1" type="password" id="password1" placeholder="password">
        <input v-model="inputs.password2" type="password" id="password2"
          placeholder="confirm password">
        <input v-model="inputs.email" type="email" id="email" placeholder="email">
      </form>
      <button @click="createAccount(inputs)">
        create account
      </button>
      <span class="error" v-show="registrationError">
        An error occured while processing your request.
      </span>
      <div>
        Already have an account?
        <router-link to="/login">login</router-link> |
        <router-link to="/password_reset">reset password</router-link>
      </div>
    </template>
    <template v-else>
      <div>
        Registration complete. You should receive an email shortly with instructions on how to
        activate your account.
      </div>
      <div>
        <router-link to="/login">return to login page</router-link>
      </div>
    </template>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex';

export default {
  data() {
    return {
      inputs: {
        username: '',
        password1: '',
        password2: '',
        email: '',
      },
    };
  },
  computed: mapState('signup', [
    'registrationCompleted',
    'registrationError',
    'registrationLoading',
  ]),
  methods: mapActions('signup', [
    'createAccount',
    'clearRegistrationStatus',
  ]),
  beforeRouteLeave(to, from, next) {
    this.clearRegistrationStatus();
    next();
  },
};
</script>

<style>
form input {
  display: block
}

.error {
  color: crimson;
  font-size: 12px;
}
</style>
