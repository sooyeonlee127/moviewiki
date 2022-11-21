<template>
  <div id="app" > 
    <b-navbar-nav>
      <b-nav>
        <img src="" alt="Logo">
        <b-nav-item class="menu" to="/" active>Home</b-nav-item>
        <b-nav-item class="menu" to="/choice" active>Explore</b-nav-item>
        <div class="accounts">
          <router-link v-if="isLogin" to="/profile"><button class="accounts_btn">My page</button></router-link>
          <router-link v-else to="/login"><button class="accounts_btn">Login</button></router-link>
          <button v-if="isLogin" @click="logOut" class="accounts_btn">Logout</button>
          <router-link v-else to="/signup"><button class="accounts_btn">SignUp</button></router-link>
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

.navbar-nav {
  padding: 30px 0;
}

nav {
  padding: 30px;
  margin-top: 30px;
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
  margin-top: 5px;
}
.accounts .accounts_btn {
  margin: 0 5px;
  color: black;
  border-radius: 10px;
  padding: 3px 10px;
  background-color: rgb(137, 255, 68);
  border: 1px solid rgb(137, 255, 68);
  transition: 0.3s;
}

.accounts .accounts_btn:hover {
  background-color: rgb(117, 218, 58);
  border: 1px solid rgb(117, 218, 58);
}
.accounts .accounts_btn:active {
  background-color: rgb(103, 192, 51);
  border: 1px solid rgb(103, 192, 51);
}
</style>
