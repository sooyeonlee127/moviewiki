<template>
  <div id="app" > 
    <b-navbar-nav>
      <b-nav>
        <b-nav-item to="/" active>홈</b-nav-item>
        <b-nav-item to="/choice" active>스무고개</b-nav-item>
        <b-nav-item to="/profile" active>내 프로필</b-nav-item>
      </b-nav>
    </b-navbar-nav>
    <router-view/>
  </div>
</template>


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
</style>
