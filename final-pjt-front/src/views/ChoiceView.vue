<template>
  <div class="container">
    <hr>
    <!-- --- -->
    <div v-if="len_result > 0">
      <h1>{{ result[idx].title }}는 어떠세요?</h1>
      <img class="poster" :src="`https://image.tmdb.org/t/p/original/${ result[idx].backdrop_path }`" :alt="`${ result[idx].title }`">
      <b-button @click="SelectMovie(true, result[idx])">좋아요!</b-button>
      <b-button @click="SelectMovie(false, result[idx])">싫어요</b-button>
    </div>
    <div v-else>
      {{ questions[index].content }}
      <b-button variant="outline-success"
      v-for="(question, idx) in questions[index]['answers']"
      :key="`question_${idx}`"
      @click="getCount(idx)">{{ question }}</b-button>
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
      result : [],
      API_URL: this.$store.state.API_URL,
      gerne_cnt: 0,
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    questions() {
      return this.$store.state.questions
    },
    len_result() {
      return this.result.length
    }
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
      console.log(this.questions[this.index].answers)
      // console.log(question)
      let tmp = {
        'answers_option': question.answers_option[answer],
        'field_name': question.field_name,
        'field_value': question.field_value,
      }
      if (tmp['field_name'] == 'genre_ids') {
        this.gerne_cnt += tmp['field_value'].length
        if (this.gerne_cnt >= 10 && this.index < 10 ) {
          this.index = 11
        }
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
        console.log(JSON.parse(res.data).count)
        if (JSON.parse(res.data).count > 30) {
          this.GetResult()
          this.index ++
        } else if (JSON.parse(res.data).count == 0) {
          this.filter_list.pop()
          // console.log('pop')
          // console.log(this.filter_list)
          this.index ++
        } else if (JSON.parse(res.data).count <= 5) {
          this.GetResult()
        } else {
          // console.log(this.result[0].id)
          // console.log(this.result[0])
          this.FindSimilar(this.result[0].id)
        // if (JSON.parse(res.data).count > 10) {
        //   this.index ++
        // } else if (JSON.parse(res.data).count == 0) {
        //   this.filter_list.pop()
        //   console.log('pop')
        //   console.log(this.filter_list)
        //   this.index ++
        // } else {
        //   console.log(this.result[0].id)
        //   console.log(this.result[0])
        //   this.FindSimilar(this.result[0].id)
        // }
        // if (this.gerne_cnt >= 10 && this.index == 11) {
        //   console.log('인덱스 이동')
        // } else {
        // this.index ++
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
          console.log(res.data)
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
      // console.log('findsimilar')
      // console.log(movie_id)
      const API_URL = `https://api.themoviedb.org/3/movie/${movie_id}/similar`
      const API_KEY = '53b8d4bdf76930f30d64c0bcd333285a'
      axios.get(API_URL, {
        params: {
            api_key: API_KEY,
            language: 'ko',
            page: 1,
        }
      }).then((res) => {
        
        console.log(res.data.results)
      }).catch((error) => {
          console.error(error)
      })
    },
    SelectMovie(answer, movie) {
      if (answer == true) {
        this.FindSimilar(movie.id)
      } else {
        
        let tmp = {
        'answers_option': 0,
        'field_name': "title",
        'field_value': [movie.title],
        }
        this.filter_list.push(tmp)
        if (this.idx > 2) {
          this.result = []
          this.GetResult()
          this.idx = 0
        } else {
          this.idx++
        }
      }
      console.log(this.idx)
      console.log(this.filter_list)
      
    }
  },
}
</script>

<style>
.poster {
  width: 1200px;
  height: 480px;
}
</style>