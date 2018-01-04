<template>
  <div id="password-reset-view">
    <h1>Reset Password</h1>
    <template v-if="emailLoading">
      loading...
    </template>
    <template v-else-if="!emailCompleted">
      <form @submit.prevent="submit">
        <input v-model="inputs.email" type="text" id="email" placeholder="email">
      </form>
      <button @click="sendResetEmail(inputs)">
        send email
      </button>
      <span class="error" v-show="emailError">
        A error occured while processing your request.
      </span>
    </template>
    <template v-else>
      <div>
        Check your inbox for a link to reset your password. If an email doesn't appear within a few
        minutes, check your spam folder.
      </div>
      <router-link to="/login">
        return to login page
      </router-link>
    </template>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex';

export default {
  data() {
    return { inputs: { email: '' } };
  },
  computed: mapState('password', [
    'emailCompleted',
    'emailError',
    'emailLoading',
  ]),
  methods: mapActions('password', [
    'sendResetEmail',
    'clearEmailStatus',
  ]),
  beforeRouteLeave(to, from, next) {
    this.clearEmailStatus();
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
