import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '@/router'
import createPersistedState from 'vuex-persistedstate'



Vue.use(Vuex)

const API_URL = "http://127.0.0.1:8000" // django 서버

export default new Vuex.Store({
  plugins : [
    createPersistedState(),
  ],
  state: {
    token: null,
    review: [],
    movies: [],
    filter_list: []//[['title', '블랙 팬서', 0], ['title', '아바타', 0]],
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
        url: `${API_URL}/api/v1/popular/`,
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
        url: `${API_URL}/accounts/login/`,
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
