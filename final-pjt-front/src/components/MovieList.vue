<template>
  <div>
    <h3>MovieList</h3>
    <MovieListItem/>
  </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem.vue'


export default {
  name: 'MovieList',
  components: {
    MovieListItem
  }
}
</script>

<style>

</style>