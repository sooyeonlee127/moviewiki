<template>
  <div>
    <ChoiceList/>
    <button @click="Question">테스트</button>
    <hr>
    <h3>선택 끝났을 때 출력할 영상</h3>
    <TrailerPlay/>
  </div>
</template>

<script>
import axios from 'axios'
import TrailerPlay from '@/components/TrailerPlay.vue'
import ChoiceList from '@/components/ChoiceList.vue'

const API_URL = "http://127.0.0.1:8000" // django 서버

export default {
  name: 'ChoiceView',
  components: {
    TrailerPlay,
    ChoiceList
  },
  data() {
    return {
      filter_list : [['title', '블랙 팬서', 0], ['title', '아바타', 0]],
    }
  },
  created(){
    if (this.isLogin) { // 로그인 여부 확인
      this.Question()
    } else {
      alert('로그인이 필요한 서비스입니다')
      this.$router.push({ name: 'login' })
    }
  },
  methods: {
    Question() { // 질문 요청(filter_list와 함께) 메서드 => 질문만 반환
      // [{question: "", keyword: "", isContain: 0}, 
      //  {question: "", keyword: "", isContain: 1}]
      axios({
        method: 'POST',
        url: `${API_URL}/api/v1/question/`,
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
    Answer() { // count 개수 반환(filter_list와 함께)
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
          console.log(res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    GetResult() { // 추천 영화 반환
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
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
}
</script>

<style>

</style>