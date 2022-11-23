<template>
  <div class="wrap_Login">
    <div class="Login">
      <h1>Sign Up</h1>
        <form @submit.prevent="SignUp">
          <label for="email">email</label>
        <input class="input" id="email" type="text" v-model="email" placeholder="@example"><br>

        <label for="nickname"> nickname</label>
        <input class="input" type="text" id="nickname" v-model="nickname"><br>

        <label for="password1"> password</label>
        <input class="input" type="password" id="password1" v-model="password1">

        <label for="password2"> password</label>
        <input class="input" type="password" id="password2" v-model="password2">
        <input class="button" type="submit" value="회원가입 완료">
        </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      email: null,
      // profile_image: '',
      nickname: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    SignUp() {
      console.log(this)
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
      this.$store.dispatch('SignUp', payload)
    }
  }
}
</script>
