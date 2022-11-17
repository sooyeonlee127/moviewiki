<template>
  <div>
    <b-card-group deck>
      <MovieListItem
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
        />
    </b-card-group>

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
      return this.$store.state.movies
    }
  }
}
</script>

<style>

</style>