<template>
  <div class="row row-horizon">
    <b-card-group>
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
  props: {
    movies: Array
  },
  components: {
    MovieListItem
  },
}
</script>

<style>

</style>