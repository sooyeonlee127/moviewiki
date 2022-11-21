<template>
  <div id="app" > 
    <b-navbar-nav>
      <b-nav>
        <b-nav-item to="/" active>홈</b-nav-item>
        <b-nav-item to="/choice" active>스무고개</b-nav-item>
        <div class="accounts">
          <b-button v-if="isLogin" variant="primary" class="accounts_btn" to="/profile">My page</b-button>
          <b-button v-else variant="primary" class="accounts_btn" to="/login">Login</b-button>
          <b-button v-if="isLogin" variant="primary" class="accounts_btn" @click="logOut">Logout</b-button>
          <b-button v-else variant="primary" class="accounts_btn" to="/signup">SignUp</b-button>
        </div>
      </b-nav>
    </b-navbar-nav>
    <router-view/>
  </div>
</template>
<script>
export default {
  name: 'App',
  data() {
    return {

    }
  },
  methods:{
    logOut() {
      this.$store.state.token = null
      this.$router.push({ name: 'movie'})
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #dee2e6;
  background-color: #000;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

.accounts {
  position: absolute;
  right: 0;
}
.accounts .accounts_btn {
  margin: 0 5px;
}
</style>
