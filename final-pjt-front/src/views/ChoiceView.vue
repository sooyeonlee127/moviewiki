<template>
  <div class="container">
    <div class="inner_container">
      <div v-if="view_step == 1">
        <p class="question">{{ questions[index].content }}</p>
        <button variant="outline-success"
        v-for="(question, idx) in questions[index]['answers']"
        :key="`question_${idx}`"
        @click="getCount(idx)">{{ question }}</button>
      </div>
      <div v-else-if="view_step == 2">
        <div v-if="result.length > 0">
          <p class="question">{{ result[idx].title }}는 어떠세요?</p>
          <img class="poster" :src="`https://image.tmdb.org/t/p/original/${ result[idx].poster_path }`" :alt="`${ result[idx].title }`">
          <div>
            <button @click="SelectMovie(true, result[idx])">좋아요!</button>
            <button @click="SelectMovie(false, result[idx])">싫어요</button>
          </div>
        </div>
        <div v-else>
          <h1>영화를 별로 안 좋아하시나봐요..</h1>
          <h1>어쩌면 음악과 더 맞을지도?!</h1>
          <a href="https://www.melon.com"><button >Melon</button></a>
          <a href="https://vibe.naver.com/"><button >Vibe</button></a>
          <a href="https://www.spotify.com"><button >Spotify</button></a>
        </div>
      </div>
      <div v-else class="results row">
        <div class="wrap_movie col-2"
        v-for="(movie, idx) in result"
        :key="`movie_${idx}`"
        >
          <a @click="DetailMovie(movie.id)">
            <div class="movie">
              <img :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`" alt="">
              <div class="desc">{{ movie.title }}</div>
            </div>
          </a>
      </div>
      </div>
    </div>
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
      // movie: {
      //   title: null,
      // },
      result: [
        {
          title: null,
          poster_path: null,
        }
      ],
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
            this.index = 10
          } else {
            this.index ++
          }
        } else if(this.index == 14) { // 1) 모든 질문이 소진 되었을 때,

          if( count == 0 ) {
            this.filter_list.pop() 
          } // (1) 만약 남은 영화가 없다면,
            // 마지막 필터 제거하고 다음단계로 진행(결과 받아오기)
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
              console.log(res.data)
              this.result = res.data
              this.view_step = 2
            })
            .catch((err) => {
              console.log(err)
            })
        } else if (count > 10) { // 2) 남은 영화가 10개 이상이면 진행 
          this.index ++
        } else if (count < 3) { // 3) 남은 영화가 없으면 마지막 필터를 제거하고 진행
          this.filter_list.pop()
          this.index ++
        } else { // 
          this.view_step = 2 // 4) 남은 영화가 10개 미만일 때 다음단계로 진행(결과 받아오기)
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
            // console.log(res.data)
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
    // GetResult() { // 추천 영화 반환
    //   console.log(this.filter_list)
    //   axios({
    //     method: 'POST',
    //     url: `${this.API_URL}/api/v1/result/`,
    //     header: {
    //       Authorization: `Token ${this.$store.state.token}`
    //     },
    //     data: {
    //       filter_list: this.filter_list,
    //     },
    //   })
    //     .then((res) => {
    //       this.idx = 0
    //       console.log(res.data)
    //       this.result = res.data
    //     })
    //     .catch((err) => {
    //       console.log(err)
    //     })
    // },
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
        this.idx++
        console.log('selectmovie')
        this.filter_list.push(tmp)
        console.log(tmp)
        if (this.idx > 2) {
          this.result = []
        } 
      }   
    }
  }
}
</script>

<style>
.inner_container {
  padding-top: 50px;
}

.inner_container .poster{
  height: 50vh;
}

.inner_container button{
  min-width: 100px;
  color: white;
  background-color: transparent;
  border: 1px solid white;
  padding: 5px 10px;
  margin: 30px 10px;
  transition: 0.1s;
}

.inner_container button:hover{
  background-color: white;
  color: black;
}

.inner_container button:active{
  background-color: rgb(167, 167, 167);
  border: 1px solid rgb(167, 167, 167);
  color: black;
}

.inner_container .results {
  width: 100%;
}

.inner_container .results .wrap_movie{
  padding: 10px;
  display: flex;
  justify-content: column;
}

.inner_container .results .movie {
  color: rgb(211, 211, 211);
  height: 100%;
  box-sizing: border-box;
  background: rgba(255, 255, 255, 0.1);
}
.inner_container .results .movie:hover {
  
}

.inner_container .results .movie img {
  width: 100%;
  height: 250px;
  overflow: hidden;
}

.inner_container .results .movie .desc {
  padding: 10px;
  text-align: left;
}

.question {
  font-size: 35px;
}
</style>