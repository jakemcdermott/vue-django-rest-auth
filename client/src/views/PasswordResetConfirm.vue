<template>
  <div id="password-reset-confirm-view">
    <h1>Reset Password Confirm</h1>
    <template v-if="resetLoading">
      loading...
    </template>
    <template v-else-if="!resetCompleted">
      <form @submit.prevent="submit">
        <input v-model="inputs.password1" type="password" id="password1" placeholder="password">
        <input v-model="inputs.password2" type="password" id="password2"
          placeholder="confirm password">
      </form>
      <button @click="resetPassword(inputs)">
        reset password
      </button>
      <span class="error" v-show="resetError">
        A error occured while processing your request.
      </span>
    </template>
    <template v-else>
      Your password has been reset.
      <router-link to="/login">return to login page</router-link>
    </template>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex';

export default {
  data() {
    return {
      inputs: {
        password1: '',
        password2: '',
        uid: this.$route.params.uid,
        token: this.$route.params.token,
      },
    };
  },
  computed: mapState('password', [
    'resetCompleted',
    'resetError',
    'resetLoading',
  ]),
  methods: mapActions('password', [
    'resetPassword',
    'clearResetStatus',
  ]),
};
</script>

<style>
form input {
  display: block
}
</style>
