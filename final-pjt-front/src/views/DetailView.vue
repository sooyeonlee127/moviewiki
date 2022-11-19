<template>
  <div>
    <div class="container">
    {{ movie.title }}
    <b-card 
      :img-src="`https://image.tmdb.org/t/p/original/${ movie.poster_path }`" 
      style="max-width: 20rem;"
      img-right
    >
    </b-card>
    <b-card-text>
      <p>개봉일: {{ movie.release_date}}</p>
      <p>{{ movie.genre_ids }}</p>
    </b-card-text>
    </div>
    <ReviewCreate/>
    <hr>
  </div>
</template>

<script>
import ReviewCreate from '@/components/ReviewCreate.vue'


export default {
  name: 'DetailView',
  data() {
    return {
      movie: null
    }
  },
  components: {
    ReviewCreate,
  },
  computed: {
    movies() {
      return this.$store.state.movies
    }
  },
  created() {
    this.getMovieById(this.$route.params.movie_id)
  },
  methods: {
    getMovieById() {
      const id = this.$route.params.movie_id
      for (const movie of this.movies) {
        if (movie.id === Number(id)) {
          this.movie = movie
          break
        }
      }
    }
  },
}
</script>

<style>

</style>