<template>
  <div class="row row-horizon overflow-x-auto" :style="myStyle">
    <h3>꼭 봐야하는 콘텐츠</h3>
    <b-card-group>
      <MovieListItem
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
        />
    </b-card-group>
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
    movies: Object
  },
  components: {
    MovieListItem
  },
  data(){
    return{
      myStyle:{
        backgroundColor:"#000" 
      }
    }
  }
}
</script>

<style>


</style>