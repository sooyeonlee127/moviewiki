<template>
  <div>
    <hr>
    {{ questions[index][0] }}
    <b-button variant="outline-success" @click="Answer">{{ questions[index][1][0] }}</b-button>
    <b-button variant="outline-success" @click="Answer">{{ questions[index][1][1] }}</b-button>
    {{ index }}
    <p>선택 끝났을 때 출력할 영상</p>
    
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = "http://127.0.0.1:8000" // django 서버

export default {
  name: 'ChoiceView',
  components: {
  },
  data() {
    return {
      filter_list : [],
      index: 0,
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    questions() {
      return this.$store.state.questions
    }
  },
  created(){
    if (!this.isLogin) { // 로그인 여부 확인
      alert('로그인이 필요한 서비스입니다')
      this.$router.push({ name: 'login' })
    } 
  },


  methods: {
    getCount() { // count 개수 반환(filter_list와 함께)
      axios({
        method: 'POST',
        url: `${API_URL}/api/v1/count/`,
        header: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data: {
          filter_list: this.filter_list,
        },
      })
      .then((res) => {
        console.log(JSON.parse(res.data).count)
        if (JSON.parse(res.data).count > 5) {
          this.index ++
        } else {
          this.GetResult()
        }
        })
        .catch((err) => {
          console.log(err)
          this.index ++
        })
    },
    GetResult() { // 추천 영화 반환
      console.log(this.filter_list)
      axios({
        method: 'POST',
        url: `${API_URL}/api/v1/result/`,
        header: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data: {
          filter_list: this.filter_list,
        },
      })
        .then((res) => {
          console.log(res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style>

</style>