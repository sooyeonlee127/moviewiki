<template>
  <div>
    <b-card
      overlay
      :img-src="`https://image.tmdb.org/t/p/original/${ trend.poster_path }`"        
      img-alt="Card Image"
      text-variant="white"
      style="max-width: 10rem;"
    >
    </b-card>
  </div>
</template>

<script>
export default {
  name: 'TrendingListItem',
  props: {
    trend: Object,
  }
}
</script>

<style>

</style>