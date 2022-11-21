<template>
  <div class="container">
    <hr>
    {{ questions[index].content }}
    <b-button variant="outline-success"
    v-for="(question, idx) in questions[index]['answers']"
    :key="`question_${idx}`"
    @click="getCount(idx)">{{ question }}</b-button>
    <!-- --- -->
    <div v-if="result">
      <b-carousel
        id="carousel-fade"
        style="text-shadow: 0px 0px 2px #000"
        fade
        indicators
        img-width="1024"
        img-height="480"
      >
        <b-carousel-slide
          v-for="res in result"
          :key="res.id"
          :caption="`${ res.title }는 어떠세요?`"
          :img-src="`https://image.tmdb.org/t/p/original/${ res.backdrop_path }`" 
          style="width: 50rem; height:30rem;"
        ></b-carousel-slide>
      </b-carousel>
    </div>
    <!-- ---- -->
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
      result : [],
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
    getCount(answer) { // count 개수 반환(filter_list와 함께)
      const question = this.questions[this.index]
      console.log(this.questions[this.index].answers)
      // console.log(question)
      let tmp = {
        'answers_option': question.answers_option[answer],
        'field_name': question.field_name,
        'field_value': question.field_value,
      }
      this.filter_list.push(tmp)
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
        // if (this.index == this.questions.length && JSON.parse(res.data).count == 0) {
        //   this.filter_list.pop()
        //   console.log('pop')
        //   console.log(this.filter_list)
        //   this.GetResult()
        // } else if (this.index == this.questions.length) {
        //   this.GetResult()
        // } else if (JSON.parse(res.data).count == 0 ){
        //   this.filter_list.pop()
        //   console.log('pop')
        //   console.log(this.filter_list)
        //   this.index ++
        // } 
        if (JSON.parse(res.data).count > 7) {
          this.index ++
        } else if (JSON.parse(res.data).count == 0) {
          this.filter_list.pop()
          console.log('pop')
          console.log(this.filter_list)
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
          this.result = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    SelectedMovie(movie_id) {
      console.log(movie_id)
      this.$router.push({name: 'detail', params: {movie_id}})
    },
  },
}
</script>

<style>

</style>