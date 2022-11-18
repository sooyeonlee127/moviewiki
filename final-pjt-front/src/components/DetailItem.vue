<template>
  <div>
    <h3>detail</h3>
    <p>{{ movie.title }}</p>
    <p>{{ movie.overview }}</p>
    <p>{{ movie.release_date}}</p>
    <p>{{ movie.poster_path}}</p>
    <p>{{ movie.genre_ids }}</p>
  </div>
</template>

<script>
export default {
  name: 'DetailItem',
  props: {
    movie: Object,
  }
}
</script>

<style>

</style>