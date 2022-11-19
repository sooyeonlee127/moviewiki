<template>
  <div>
    <b-card
      overlay
      :img-src="`https://image.tmdb.org/t/p/original/${ trend.poster_path }`"        
      img-alt="Card Image"
      text-variant="white"
      style="max-width: 10rem;"
      @click="SelectedMovie(movie.id)"
    >
    </b-card>
  </div>
</template>

<script>
export default {
  name: 'TrendingListItem',
  props: {
    trend: Object,
  },
  methods: {
    SelectedMovie(movie_id) {
      console.log(movie_id)
      this.$router.push({name: 'detail', params: {movie_id}})
      }
    }
  }
</script>

<style>

</style>