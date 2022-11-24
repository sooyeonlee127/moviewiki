<template>
  <div>
    <h1>'{{ keyword }}'으로 검색한 결과입니다.</h1>


    <b-container fluid class="p-4 bg-dark">
      <b-row>
        <b-col 
          v-for="movie in searchmovie"
          :key="movie.id">
          <img :src="`https://image.tmdb.org/t/p/original/${ movie.poster_path }`">
          {{ movie.title }}
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

  }
  }
</script>

<style>

</style>