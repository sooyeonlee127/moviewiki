<template>
  <div class="wrap_container">
    <div id="app" class="container"> 
      <header>
        <div class="menus">
          <!-- <img src="" alt="Logo"> -->
          <span id="logo" style="font-size: 30px;">LOGO</span>
          <router-link class="menu" to="/">Home</router-link>
          <router-link class="menu" to="/choice">Explore</router-link>
          <form @submit.prevent="" style="display: inline-block">
            <input class="searchBar" type="text" placeholder="search" @keyup.enter="searchMovie">
          </form>
        </div>
        <div class="accounts">
          <button v-if="isLogin" @click="logOut" class="accounts_btn">Logout</button>
          <router-link v-else to="/signup"><button class="accounts_btn">SignUp</button></router-link>
          <router-link v-if="isLogin" to="/profile"><button class="accounts_btn">My page</button></router-link>
          <router-link v-else to="/login"><button class="accounts_btn">Login</button></router-link>
        </div>
        
      </header>
      <hr>
      <article>
      <router-view/>
      </article>
    </div>
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
    },
    searchMovie() {
      console.log("dd")
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
/* @import "https://fonts.googleapis.com";
@import "https://fonts.gstatic.com"; */
@import "https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,300;1,400;1,500;1,600;1,700;1,800&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap";
body {
  margin: 0;
}
.wrap_container {
  background: black;
  margin: 0;
  height: 100%;
  min-height: 100vh;
  box-sizing: content-box;
}

#app {
  min-height: 100vh;
  font-family: 'Open Sans', sans-serif;
  font-family: 'Poppins', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #dee2e6;
  /* background: red; */
}

.container article {
  padding: 50px 0;
}

header {
  display: flex;
  flex-direction:row;
  justify-content: space-between;
  padding-top: 50px;
}

#logo {
  top: 0;
  margin-right: 30px;
}

.menus {
  display: flex;
  flex-direction: row;
  align-items: center;
}

.menus .menu {
  margin: 0 10px;
  color: white;
  text-decoration: none;
}

.menus .menu:hover {
  color: rgb(137, 255, 68);
}

.menus .menu:active {
  color: rgb(75, 199, 3);
}

.menus .searchBar{  
  transition: 0.2s;
  border: 1px solid rgba(255, 255, 255, 0.6);
  padding: 0 10px;
  margin: 10px 0;
  margin-left: 30px !important;
  color: rgba(255, 255, 255, 0.6);
  font-weight: 300;
  background: transparent;
  width: 150px;
  border-radius: 0px;
}


.menus .searchBar:focus {
  margin: 0;
  padding: 9px 20px;
  font-weight: 600;
  border: 2px solid rgba(255, 255, 255, 1);
  color: rgba(255, 255, 255, 1);
  width: 200px;
}

.accounts {
  right: 0;
  display: flex;
  flex-direction: row-reverse;
  align-items: center;
}
.accounts .accounts_btn {
  margin: 0 7px;
  color: black;
  padding: 3px 10px;
  font-weight: bold;
  background-color: rgb(137, 255, 68);
  transition: 0.2s;
}

.accounts .accounts_btn:hover {
  background-color: rgb(255, 255, 255);
}
.accounts .accounts_btn:active {
  background-color: rgb(103, 192, 51);
}
</style>
