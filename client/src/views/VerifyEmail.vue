<template>
  <div id="activate-account-view">
    <h1>Verify Email</h1>
    <template v-if="activationLoading">loading...</template>
    <template v-else-if="activationError">An error occured.</template>
    <template v-else-if="activationCompleted">
      Account activation successful.
      <router-link v-if="!isAuthenticated" to="/login">
        Click here to sign in.
      </router-link>
    </template>
  </div>
</template>

<script>
import {
  mapActions,
  mapGetters,
  mapState,
} from 'vuex';

export default {
  computed: {
    ...mapGetters('auth', ['isAuthenticated']),
    ...mapState('signup', [
      'activationCompleted',
      'activationError',
      'activationLoading',
    ]),
  },
  methods: mapActions('signup', [
    'activateAccount',
    'clearActivationStatus',
  ]),
  created() {
    this.activateAccount(this.$route.params);
  },
  beforeRouteLeave(to, from, next) {
    this.clearActivationStatus();
    next();
  },
};
</script>
