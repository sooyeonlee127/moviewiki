<template>
  <div>
    <b-card
      overlay
      :img-src="`https://image.tmdb.org/t/p/original/${ movie.poster_path }`"        
      img-alt="Card Image"
      text-variant="white"
      style="max-width: 10rem;"
    >
      <!-- <b-card-text class="text-xl-center">
        {{ movie.title }}
      </b-card-text> -->
    </b-card>
  </div>
</template>

<script>
export default {
  name: 'MovieListItem',
  props: {
    movie: Object,
  }
}
</script>

<style>

</style>