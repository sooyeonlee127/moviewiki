<template>
  <div class="wrap_myPage">
    <div class="myPage">
      <h1>{{user.nickname}}님의 페이지</h1>
      
      <form @submit.prevent="changeProfile">
        <div>
          {{ userReview}}

          <label for="nickname">닉네임</label>
          <input id="nickname" class="inputgroup" type="text" disabled="true" v-model="user.nickname" >
        </div>
        <div>
          <label for="email">이메일</label>
          <input id="email" class="inputgroup" type="text" disabled="true" v-model="user.email">
        </div>
        <input type="submit" v-if="change_profile" value="수정 완료">
        <button v-if="change_profile" >취소</button>
        <button v-else @click="ProfileInputToggle">회원정보 수정</button>
      </form>

      <button v-if="!change_password" @click="PasswordInputToggle">비밀번호 변경</button>
      <form v-if='change_password' @submit.prevent="changePassword">
        <input id="pw_input1" class="inputgroup" type="password" v-model="new_password1">
        <input id="pw_input2" class="inputgroup" type="password" v-model="new_password2">
        <input type="submit" value="비밀번호 변경 제출">
        <button @click="PasswordInputToggle">취소</button>
      </form>
      <section>
        <h3>내가 좋아하는 콘텐츠</h3>
      </section>
      <section>
        <h3>내가 쓴 리뷰</h3>
          <div 
            v-for="review in userReview"
            :key="review.id"
            >
            <div v-if="review.user == user.email">
              {{ review.movie}}
              {{ review.content }}
            </div>
          </div>

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
    userReview() {
      return this.$store.state.review
    }
  },
  created() {
    this.getUser()
    this.getReview()
  },
  data() {
    return {
      user: {
        email: null,
        nickname: null,
        profile_image: null,
      },
      new_password1: null,
      new_password2: null,
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
          'Authorization': `Token ${this.$store.state.token}`
        },
      })
      .then((res) => {
        console.log(res)
        this.email = res.data.email
        this.user = res.data
        console.log(res.data)
        console.log('회원정보')
      })
      .catch((error) => {
        console.log('회원정보 실패')
        console.log(error)
      })
    },
    ProfileInputToggle() {
      const input1 = document.querySelector('#nickname')
      input1.classList.toggle('active')
      input1.disabled = false
      if (this.change_profile) {
        this.change_profile = false
      } else {
        this.change_profile = true
      }
    },
    PasswordInputToggle() {
      if (this.change_password) {
        this.change_password = false
      } else {
        this.change_password = true
      }
    },
    changeProfile() {
      axios({
        method: 'put',
        url: `${this.API_URL}/accounts/user/`,
        headers: {
          'Authorization': `Token ${this.$store.state.token}`,
        },
        data: {
          'nickname': this.user.nickname,
          'profile_image': this.user.profile_image,
        },
      })
      .then((res) => {
        console.log(res)
        this.ProfileInputToggle()
      })
      .catch((error) => {
        console.log(error)
      })
    },
    changePassword() {
      axios({
        method: 'post',
        url: `${this.API_URL}/accounts/password/change/`,
        headers: {
          'Authorization': `Token ${this.$store.state.token}`
        },
        data: {
          'new_password1': this.new_password1,
          'new_password2': this.new_password2,
        }
      })
      .then((res) => {
        console.log(res)
        this.PasswordInputToggle()
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

.myPage form {
  width: 100%;
  text-align: left;
}

.myPage form label {
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