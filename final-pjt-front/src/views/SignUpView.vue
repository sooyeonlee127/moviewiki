<template>
  <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="email">email : </label>
      <input type="text" id="email" v-model="email"><br>

      <!-- <label for="profile_image"> profile_image : </label>
      <input type="file" id="profile_image" @change="{}"><br> -->

      <label for="nickname"> nickname : </label>
      <input type="text" id="nickname" v-model="nickname"><br>

      <label for="password1"> password : </label>
      <input type="password" id="password1" v-model="password1">

      <label for="password2"> password : </label>
      <input type="password" id="password2" v-model="password2">
      
      <input type="submit" value="SignUp">
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      email: null,
      profile_image: '',
      nickname: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    UploadImage() {

    },
    SignUp() {
      const email = this.email
      const nickname = this.nickname
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        email: email,
        // profile_image: profile_image,
        nickname: nickname,
        password1: password1,
        password2: password2,
      }

      this.$store.dispath('signUp', payload)
    }
  }
}
</script>
