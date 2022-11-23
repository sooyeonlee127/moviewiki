<template>
  <div class="home">
    <MoviePoster
      :movies="movies"
    />
    <div class="article">
      <section>
        <MovieList :movies="movies"/>
      </section>
      <section>
        <TrendingList :trending="trending"/>
      </section>
      <section style="margin-bottom: 0;">
        <ActorList :actors="actors"/>
      </section>
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
    // this.getBestMovies()
  },
  methods: {
    getMovies() {
      console.log("getMovie")
      this.$store.dispatch('getMovies')
    },
    // getBestMovies() {
    //   this.$store.dispatch('getBestMovies')
    // },
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
    },
    // best_movies() {
    //   return this.$store.state.best_movies
    // }
  },
}
</script>
 
<style>

section {
  margin: 50px 0;
}

.wrap_slider{
  width:100%;
  height:100%;
  margin:20px auto;
  display: flex;
  flex-direction: row;
  justify-content:center;
}

.slider_btn {
  background: transparent;
}

.slider_btn:hover {
  opacity: 0.5;
}

.slider_btn img {
  width: 30px;
}

.movie_item {
  width: 11.75%;
  margin-right: 2%;
  cursor: pointer;
}

.movie_item img {
  width: 100%;
  transition: 0.1s;
}

.movie_item img:hover {
  opacity: 0.7;
}

.movie_item img:active {
  opacity: 0.5;
}
</style>