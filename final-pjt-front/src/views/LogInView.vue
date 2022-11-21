<template>
  <div>
    <h1>LogIn Page</h1>
    <form @submit.prevent="logIn">
      <label for="email">email : </label>
      <input type="text" id="email" v-model="email"><br>

      <label for="password"> password : </label>
      <input type="password" id="password" v-model="password"><br>

      <input type="submit" value="logIn">
    </form>
  </div>
</template>

<script>
// 회원가입(signUp)과 다른점 password1 password2가 password로 바뀐 것뿐
// 요청을 보내고 응답을 받은 Token을 state에 저장하는 것도 동일 ( == mutations가 처리 해야 하는 업무가 동일)
// SIGN_UP mutations를 SAVE_TOKEN mutations으로 대체 가능
// 이전에 작성되어있던 SIGN_UP mutation을 지우고 하나로 활용
export default {
  name: 'LogInView',
  data() {
    return {
      email: null,
      password: null
    }
  },
  methods: {
    logIn() {
      const email = this.email
      const password = this.password

      const payload = {
        email: email,
        password: password
      }
      this.$store.dispatch('logIn', payload)
    }
  }
}
</script>
