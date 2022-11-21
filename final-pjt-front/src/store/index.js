import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '@/router'
import createPersistedState from 'vuex-persistedstate'



Vue.use(Vuex)



export default new Vuex.Store({
  plugins : [
    createPersistedState(),
  ],
  state: {
    API_URL : "http://127.0.0.1:8000", // django 서버
    token: null,
    review: [],
    movies: [],
    filter_list: [],//[['title', '블랙 팬서', 0], ['title', '아바타', 0]],
    questions: [
      {
        'content': "가족과 함께 보시나요?",
        'answers': ["네", "아니오"],
        'answers_option': [0, 2],
        'field_name': "adult",
        'field_value': [true],
      },
      {
        'content': "겁이 많으신가요?",
        'answers': ["네", "아니오"],
        'answers_option': [0, 2],
        'field_name': "genre_ids",
        'field_value': [27, 80, 53],
      },
      {
        'content': "음악 영화 좋아하세요?",
        'answers': ["네", "아니오"],
        'answers_option': [2, 0],
        'field_name': "genre_ids",
        'field_value': [10402],
      },
      {
        'content': "연인과 함께 보시나요?",
        'answers': ["네", "아니오"],
        'answers_option': [1, 2],
        'field_name': "genre_ids",
        'field_value': [10749],
      },
      {
        'content': "확실한 기분전환이 필요하신가요?",
        'answers': ["네", "아니오"],
        'answers_option': [1, 2],
        'field_name': "genre_ids",
        'field_value': [35],
      },
      {
        'content': "잔잔한 영화로 힐링하고 싶으신가요?",
        'answers': ["네", "아니오"],
        'answers_option': [1, 0],
        'field_name': "genre_ids",
        'field_value': [99, 18],
      },
      {
        'content': "동심을 자극하는 만화영화는 어떠세요?",
        'answers': ["보고싶어요", "싫어요"],
        'answers_option': [1, 0],
        'field_name': "genre_ids",
        'field_value': [16],
      },
      {
        'content': "미지의 세계로! 모험을 떠나는 이야기는 어때요?",
        'answers': ["보고싶어요", "싫어요"],
        'answers_option': [1, 2],
        'field_name': "genre_ids",
        'field_value': [12],
      },
      {
        'content': "실화를 바탕으로 한 옛날 이야기가 듣고 싶지는 않으세요?",
        'answers': ["보고싶어요", "싫어요"],
        'answers_option': [1, 2],
        'field_name': "genre_ids",
        'field_value': [36],
      },
      {
        'content': "흥미진진, 상상력을 자극하는 스토리는 어때요?",
        'answers': ["보고싶어요", "싫어요"],
        'answers_option': [1, 2],
        'field_name': "genre_ids",
        'field_value': [9648],
      },
      {
        'content': "카우보이의 스토리, 황량한 배경에서의 총격전도 추천해요!",
        'answers': ["보고싶어요", "싫어요"],
        'answers_option': [1, 0],
        'field_name': "genre_ids",
        'field_value': [37],
      },
      {
        'content': "전쟁 영화 좋아하세요?",
        'answers': ["좋아해요", "싫어요"],
        'answers_option': [2, 0],
        'field_name': "genre_ids",
        'field_value': [10752],
      },
    ]
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
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
      router.push({ name: 'movie' })
    }
  },
  actions: {
    getMovies(context) {
      axios({
        method: 'get',
        url: `${this.state.API_URL}/api/v1/popular/`,
      })
        .then((res) => {
          context.commit('GET_MOVIES', res.data)
        })
    },
    SignUp(context, payload) {
      console.log(payload)
      axios({
        method: 'post',
        url: `${this.state.API_URL}/accounts/signup/`,
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
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    logIn(context, payload) {
      const email = payload.email
      const password = payload.password
      axios({
        method: 'post',
        url: `${this.state.API_URL}/accounts/login/`,
        data: {
          email, password
        }
      })
      .then(res => {
        context.commit('SAVE_TOKEN', res.data.key)
      })
      .catch(error => console.log(error))
    }
  },
  modules: {
  }
})
