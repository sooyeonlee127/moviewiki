<template>
  <div class="view overlay">
    <img src="" alt="">
    <img
      v-if="movie.adult==false"
      overlay
      :src="`https://image.tmdb.org/t/p/original/${ movie.poster_path }`"        
      img-alt="Card Image"
      text-variant="white"
      @click="SelectedMovie(movie.id)"
      style="width: 10rem; height:15rem;"
      b-aspect="1:1"
    >
      <div class="mask flex-center rgba-red-strong">
      <p class="white-text">{{ movie.title }}</p>
    </div>
  </div>
</template>
 
<script>
export default {
  name: 'MovieListItem',
  props: {
    movie: Object,
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