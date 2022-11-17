<template>
  <div>
    <h3>MovieList</h3>
    <MovieListItem/>
    <movies/>
  </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem.vue'

export default {
  name: 'MovieList',
  components: {
    MovieListItem
  },
  computed: {
    movies() {
      console.log(this.$store.state.movies)
      return this.$store.state.movies
    }
  }
}
</script>

<style>

</style>