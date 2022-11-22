<template>
  <div class="home">
    <MoviePoster
      :movies="movies"
    />
    <div class="article">
      <MovieList
        :movies="movies"
      />
      <TrendingList
        :trending="trending"  
      />
      <ActorList
        :actors="actors"
      />
    </div>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList.vue'
import ActorList from '@/components/ActorList.vue'
import MoviePoster from '@/components/MoviePoster.vue'
import TrendingList from '@/components/TrendingList.vue'
import axios from 'axios'


export default {
  name: 'MovieView',
  components: {
    MovieList,
    ActorList,
    MoviePoster,
    TrendingList
  },
  data() {
    return {
      actors: [],
      trending: [],
    }
  },
  created() {
    this.getMovies()
    this.requestActors()
    this.requestTrending()
  },
  methods: {
    getMovies() {
      console.log("getMovie")
      this.$store.dispatch('getMovies')
    },
    requestActors() {
      const API_URL = 'https://api.themoviedb.org/3/person/popular'
      const API_KEY = '53b8d4bdf76930f30d64c0bcd333285a'

      axios.get(API_URL, {
        params: {
            api_key: API_KEY,
            language: 'ko',
            page: 1,
        }
      }).then((response) => {
        const actors = response.data.results
        this.actors = actors

      }).catch((error) => {
          console.error(error)
      })
    },
    requestTrending() {
      const API_URL = 'https://api.themoviedb.org/3/trending/movie/day'
      const API_KEY = '53b8d4bdf76930f30d64c0bcd333285a'

      axios.get(API_URL, {
        params: {
            api_key: API_KEY,
        }
      }).then((response) => {
        const trending = response.data.results
        this.trending = trending

      }).catch((error) => {
          console.error(error)
      })
    }
  },
  computed: {
    movies() {
      return this.$store.state.movies
    }
  },
}
</script>
 