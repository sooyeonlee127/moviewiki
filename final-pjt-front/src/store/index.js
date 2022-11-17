import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'


Vue.use(Vuex)

const API_URL = "http://127.0.0.1:8000" // django 서버

export default new Vuex.Store({
  state: {
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
  },
  modules: {
  }
})
