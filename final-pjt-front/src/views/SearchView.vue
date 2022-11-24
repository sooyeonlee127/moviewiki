<template>
  <div>
    <h1>'{{ keyword }}'으로 검색한 결과입니다.</h1>
    <hr>
    <b-container fluid class="p-4 bg-dark">
      <b-row>
        <b-col 
          v-for="movie in searchmovie"
          :key="movie.id">
          <div class="container"
            style="width: 250px; display: flex; flex-direction: column; align-items: center; margin-bottom: 10px;">
            <img
              :src="`https://image.tmdb.org/t/p/original/${ movie.poster_path }`" 
              @click="getDetail(movie.id)"
              style="width: 200px;"
              >
              <span style="width: 200px; font-size: 20px; font-weight: 500;">
                {{ movie.title }}
              </span>
          </div>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'SearchView',
  created() {
    this.keyword = this.$route.params.movie_title
    this.SearchMovie(this.keyword)
  },
  watch:{
    $route(){
      this.keyword = this.$route.params.movie_title
      this.SearchMovie(this.keyword)}
    },
  data() {
    return {
      keyword: '',
      searchmovie: [],
    }
  },
  computed: {
      rows() {
        return this.SearchMovie.length
      }
  },
  methods: {
    SearchMovie(keyword) {
      axios({
        method: 'GET',
        url: `http://127.0.0.1:8000/api/v1/movies/search/${keyword}/`,
      })
      .then((res) => {
        console.log(res)
        this.searchmovie = res.data
      })
      .catch((error) => {
        console.log('search view의 catch')
        console.log(error)
      })},
  getDetail(movie_id){
    console.log('클릭')
    console.log(movie_id)
    this.$router.push({name: 'detail', params: {movie_id}})
  }
  }}
</script>

<style>
b-img {
  width: 100px;

}

</style>