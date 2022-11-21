<template>
  <div>
    <div>
      <b-card
        overlay
        :img-src="`https://image.tmdb.org/t/p/original/${ movie.backdrop_path }`" 
        img-alt="Card Image"
        text-variant="white"
        :title="`${ movie.title }`"
      >
        <b-card-text>
          {{ movie.overview }}
        </b-card-text>
        <b-button ref="show" variant="primary">
          찜하기
        </b-button>
      </b-card>
    </div>
    <ReviewList :movie="movie"/>
    <hr>
  </div>
</template>

<script>
import ReviewList from '../components/ReviewList.vue'


export default {
  name: 'DetailView',
  data() {
    return {
      movie: null
    }
  },
  components: {
    ReviewList,
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