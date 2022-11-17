<template>
  <div class="home">
    <MoviePoster/>
    <MovieList/>
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
  }
}
</script>
