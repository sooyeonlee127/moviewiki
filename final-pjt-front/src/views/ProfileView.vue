<template>
  <div class="wrap_myPage">
    <div class="myPage">
      <h1>{{user.nickname}}님의 페이지</h1>
      
      <section>
        <div>
          <label for="nickname">닉네임</label>
          <input id="nickname" class="inputgroup" type="text" disabled="true" v-model="user.nickname" >
        </div>
        <div>
          <label for="email">이메일</label>
          <input id="email" class="inputgroup" type="text" disabled="true" :value="email">
        </div>
      </section>
      <button v-if="!change_profile" @click="AbleProfileInput">회원정보 수정</button>
      <button v-else @click="changeProfile">수정 완료</button>
      <button v-if="!change_password" @click="AblePasswordInput">비밀번호 변경</button>
      <section>
        <h3>내가 좋아하는 콘텐츠</h3>
        
      </section>
      <section>
        <h3>내가 쓴 리뷰</h3>

      </section>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ProfileView',
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
  },
  created() {
    this.getUser()
  },
  data() {
    return {
      email: null,
      user: {
        email: null,
        nickname: null,
        profile_image: '',
      },
      API_URL: this.$store.state.API_URL,
      change_profile: false,
      change_password: false,
    }
  },
  methods: {
    getReviews() {
      if (this.isLogin) {
        this.$store.dispatch('getReviews')
      } else {
        alert('로그인이 필요한 서비스입니다')
        this.$router.push({ name: 'login' })
      }
    },
    getUser() {
      axios({
        method: 'get',
        url: `${this.API_URL}/accounts/user/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
      .then((res) => {
        console.log(res)
        this.email = res.data.email
        this.user = res.data
      })
      .catch((error) => {
        console.log(error)
      })
    },
    AbleProfileInput() {
      const input1 = document.querySelector('#nickname')
      input1.classList.toggle('active')
      input1.disabled = false
      this.change_profile = true
    },
    AblePasswordInput() {
      const input1 = document.querySelector('#nickname')
      const input2 = document.querySelector('#email')
      input1.classList.toggle('active')
      input2.classList.toggle('active')
      input1.disabled = false
      input2.disabled = false
      this.change_password = true
    },
    changeProfile() {
      console.log(this.user.nickname)
      axios({
        method: 'PUT',
        url: `${this.API_URL}/accounts/user/update/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data: {
          email: this.email,
          nickname: this.user.nickname,
          profile_image: this.user.profile_image,
        }
      })
      .then((res) => {
        console.log(res)
        this.change_profile = false
      })
      .catch((error) => {
        console.log(error)
      })
    },
    changePassword() {
      axios({
        method: 'put',
        url: `${this.API_URL}/accounts/user/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
      .then((res) => {
        console.log(res)
        this.change_password = false
      })
      .catch((error) => {
        console.log(error)
      })
    }

  }

}
</script>

<style>
.wrap_myPage {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.myPage {
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

.myPage section {
  width: 100%;
  text-align: left;
}

.myPage section label {
  width: 100%;
  margin: 15px 0 3px 0;
}

.myPage input {
  width: 100%;
  height: 35px;
  padding: 5px;
  color: inherit;
  background: white;
  border: 1px solid rgb(214, 214, 214);
  box-sizing: border-box;
}

.myPage .active {
  border: 2px solid black;
  background: rgb(240, 248, 255);
  color: black;
}
</style>