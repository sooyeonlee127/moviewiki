<template>
  <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password1"> password : </label>
      <input type="password" id="password1" v-model="password1"><br>

      <label for="password2"> password confirmation : </label>
      <input type="password" id="password2" v-model="password2">
      
      <input type="submit" value="SignUp">
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  // data() {
  //   return {
  //     username: null,
  //     password1: null,
  //     password2: null,
  //   }
  // },
  // 회원가입 완료시 응답받을 정보 token을 store에서 관리할 수 있도록
  // actions를 활용하여 요청 후, state에 저장할 로직 작성
  // 다양한 컴포넌트에서 쉽게 접근할 수 있도록 중앙 상태 저장소인
  // vuex에서 관리
  // methods: {
  //   SignUp() {
  //     const username = this.username
  //     const password1 = this.password1
  //     const password2 = this.password2

  //     const payload = {
  //       username: username,
  //       password1: password1,
  //       password2: password2
  //     }

  //     this.$store.dispath('signUp', payload)
  //   }
  // }
}
</script>
