<template>
  <div class="wrap_Login">
    <div class="Login">
      <h1>LOGIN</h1>
        <form @submit.prevent="logIn">
          <label for="email">이메일</label>
          <input class="input" id="email" type="text" v-model="email">
          <label for="password">닉네임</label>
          <input class="input" type="password" id="password" v-model="password">
          <input class="button" type="submit" value="logIn">
        </form>
    </div>
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
<style>
.wrap_Login {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: left;
}
.Login {
  padding: 30px;
  color: rgb(53, 53, 53);
  width: 100%;
  max-width: 700px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  background: rgb(244 245 243);
  border: 1px solid rgb(202, 202, 202);
  box-sizing: border-box;
  box-shadow: 0 0 5px rgba(137, 255, 68, 0.3),
              0 0 15px rgba(137, 255, 68, 0.3),
              0 0 30px rgba(137, 255, 68, 0.3),
              0 0 100px rgba(137, 255, 68, 0.3);
}
.Login form {
  width: 100%;
}
.Login form label {
  width: 100%;
  margin: 15px 0 3px 0;
}

.Login .input {
  width: 100%;
  padding: 5px;
  color: inherit;
  background: white;
  border: 1px solid rgb(214, 214, 214);
}

.Login .button {
  width: 100%;
  background: rgb(199, 199, 199);
  border: none;
  color: rgb(255, 255, 255);
  font-size: 20px;
  font-weight: 600;
  padding: 7px 10px;
  margin-top: 30px;
}

.Login .button:hover {
  color: black;
  background: rgb(137, 255, 68);
}
</style>