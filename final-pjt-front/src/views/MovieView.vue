<template>
  <div class="home">
    <MoviePoster
      :movies="movies"
    />
    <MovieList
      :movies="movies"
    />
    <ActorList/>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList.vue'
import ActorList from '@/components/ActorList.vue'
import MoviePoster from '@/components/MoviePoster.vue'

export default {
  name: 'MovieView',
  components: {
    MovieList,
    ActorList,
    MoviePoster
  },
  created() {
    this.getMovies()
  },
  methods: {
    getMovies() {
      this.$store.dispatch('getMovies')
    }
  },
  computed: {
    movies() {
      return this.$store.state.movies
    }
  },
}
</script>
 