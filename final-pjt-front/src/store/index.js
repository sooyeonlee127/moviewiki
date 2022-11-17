import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

// const API_URL = "http://127.0.0.1:8000" // django 서버

export default new Vuex.Store({
  state: {
    filter_list: [],
    questions: [
      ["가족과 함께 보시나요?", ["Yes", "No"], "adult", True, 1],
    ]
  },
  getters: {
  },
  mutations: {
  },
  actions: {
    // axios를 사용하여 데이터 가져오기


  },
  modules: {
  }
})
