import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
// import createPersistedstate from 'vuex-persistedstate'



Vue.use(Vuex)

const API_URL = "http://127.0.0.1:8000" // django 서버

export default new Vuex.Store({
  // Plugins : [
  //   createPersistedstate()
  // ],
  state: {
    token: null,
    review: [],
    movies: [],
    filter_list: [],
    questions: [ // index - 1: 질문, 2: 대답, 3: key, 4: value, 5: 소거(0) / 포함(1)
      ["가족과 함께 보시나요?", ["Yes", "No"], "adult", true, 0],
      ["겁이 많으신가요?", ["Yes", "No"], "genre_ids", 27, 0],
      ["음악 영화 좋아하세요?", ["Yes", "No"], "genre_ids", 10402, 1],
      ["연인과 함께 보시나요?", ["Yes", "No"], "genre_ids", 10749, 1],
    ]
  },
  getters: {
  },
  mutations: {
    GET_MOVIES(state, movies) {
      state.movies = movies
    },
    GET_REVIEWS(state, review) {
      state.review = review
    },
    SELECTED_MOVIE(state, movie) {
      state.movie = movie
    },
    SAVE_TOKEN(state, token) {
      console.log('SAVE_TOKEN')
      state.token = token
    }
  },
  actions: {
    // axios를 사용하여 데이터 가져오기
    getMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/popular/`,
      })
        .then((res) => {
          context.commit('GET_MOVIES', res.data)
        })
    },
    // SelectedMovie(context, movie) {
    //   context.commit('SELECTED_MOVIE', movie)
    // }
    SignUp(context, payload) {
      console.log(payload)
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          email: payload.email,
          // profile_image: payload.profile_image,
          nickname: payload.nickname,
          password1: payload.password1,
          password2: payload.password2
        }
      })
        .then((res) => {
          console.log(res)
          console.log('성공!')
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => {
          console.log(err)
          console.log('실패')
        })
    }
  },
  modules: {
  }
})
