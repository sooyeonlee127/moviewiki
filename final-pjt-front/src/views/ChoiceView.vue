<template>
  <div class="container">
    <hr>
    <!-- --- -->
    <div v-if="view_step == 1">
      {{ questions[index].content }}
      <b-button variant="outline-success"
      v-for="(question, idx) in questions[index]['answers']"
      :key="`question_${idx}`"
      @click="getCount(idx)">{{ question }}</b-button>
    </div>
    <div v-else-if="view_step == 2">
      <h1>{{ result[idx].title }}는 어떠세요?</h1>
      <img class="poster" :src="`https://image.tmdb.org/t/p/original/${ result[idx].backdrop_path }`" :alt="`${ result[idx].title }`">
      <b-button @click="SelectMovie(true, result[idx])">좋아요!</b-button>
      <b-button @click="SelectMovie(false, result[idx])">싫어요</b-button>
    </div>
    <div v-else>
      <div 
      v-for="(movie, idx) in result"
      :key="`movie_${idx}`"
      >
        <h1>{{ movie.title }}</h1>
        <img :src="`https://image.tmdb.org/t/p/original/${movie.backdrop_path}`" alt="">
      </div>
    </div>
    <!-- ---- -->
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ChoiceView',
  components: {
  },
  data() {
    return {
      filter_list : [],
      idx: 0,
      index: 0,
      view_step: 1,
      result : [],
      API_URL: this.$store.state.API_URL,
      del_gerne_cnt: 0,
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    questions() {
      return this.$store.state.questions
    },
  },
  created(){
    if (!this.isLogin) { // 로그인 여부 확인
      alert('로그인이 필요한 서비스입니다')
      this.$router.push({ name: 'login' })
    } 
  },
  methods: {
    getCount(answer) { // count 개수 반환(filter_list와 함께)
      const question = this.questions[this.index]
      // console.log(this.questions[this.index].answers)
      let tmp = {
        'answers_option': question.answers_option[answer],
        'field_name': question.field_name,
        'field_value': question.field_value,
      }
      
      this.filter_list.push(tmp)
      axios({
        method: 'POST',
        url: `${this.API_URL}/api/v1/count/`,
        header: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data: {
          filter_list: this.filter_list,
        },
      })
      .then((res) => {
        const count = JSON.parse(res.data).count
        console.log(`count : ${count}`)
        console.log(this.result)
        if (tmp['field_name'] == 'genre_ids') { // 장르로 필터를 거는 경우
        this.del_gerne_cnt += tmp['field_value'].length
          if (this.del_gerne_cnt >= 5 && this.index < 10) { // 소거한 장르의 개수가 5 이상이고, 현재 질문의 인덱스가 10 미만
            this.index = 11
          } else {
            this.index ++
          }
        } else if (count > 5) { 
          console.log(this.index)
          this.index ++
        } else if (count == 0) {
          this.filter_list.pop()
          this.index ++
        } else {
          this.view_step = 2
          console.log('count')
          console.log(count)
          // getResult 동기 처리
          axios({
            method: 'POST',
            url: `${this.API_URL}/api/v1/result/`,
            header: {
              Authorization: `Token ${this.$store.state.token}`
            },
            data: {
              filter_list: this.filter_list,
            },
          })
          .then((res) => {
            this.result = res.data
            this.view_step = 2
          })
          .catch((err) => {
            console.log(err)
          })
        } 
      })

      .catch((err) => {
        console.log(err)
      })
    },
    GetResult() { // 추천 영화 반환
      console.log(this.filter_list)
      axios({
        method: 'POST',
        url: `${this.API_URL}/api/v1/result/`,
        header: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data: {
          filter_list: this.filter_list,
        },
      })
        .then((res) => {
          // console.log(res.data)
          this.result = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    DetailMovie(movie_id) { // 마지막 추천 영화 클릭시 디테일 페이지로 연결
      // console.log(movie_id)
      this.$router.push({name: 'detail', params: {movie_id}})
    },
    FindSimilar(movie_id) {  // 비슷한 영화 추천
      const API_URL = `https://api.themoviedb.org/3/movie/${movie_id}/similar`
      const API_KEY = '53b8d4bdf76930f30d64c0bcd333285a'
      axios.get(API_URL, {
        params: {
            api_key: API_KEY,
            language: 'ko',
            page: 1,
        }
      }).then((res) => {
        // 비슷한영화 가져옴
        console.log(res.data.results)
        this.result = res.data.results
      }).catch((error) => {
          console.error(error)
      })
    },
    SelectMovie(answer, movie) {
      if (answer == true) {
        // console.log("selectmvie")
        this.view_step = 3
        this.FindSimilar(movie.id)
      } else {
        let tmp = {
          'answers_option': 0,
          'field_name': "title",
          'field_value': [movie.title],
        }
        console.log('selectmovie')
        this.filter_list.push(tmp)
        console.log(tmp)
        if (this.idx > 2) {
          console.log('여기')
          this.result = []
          this.GetResult()
          this.idx = 0
        } else {
          console.log('실패')
          this.idx++
        }
      }
      // console.log(this.idx)
      // console.log(this.filter_list)
      
    }
  }
}
</script>

<style>
.poster {
  width: 1200px;
  height: 480px;
}
</style>