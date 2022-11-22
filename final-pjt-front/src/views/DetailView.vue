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
    <ReviewList 
    :reviews="movie.comment_set"
    :movie_id="movie.id"
    />
    <hr>
  </div>
</template>

<script>
import ReviewList from '../components/ReviewList.vue'
import axios from 'axios'

export default {
  name: 'DetailView',
  data() {
    return {
      movie: [],
      API_URL: this.$store.state.API_URL,
    }
  },
  components: {
    ReviewList,
  },
  created() {
    this.getMovieById(this.$route.params.movie_id)
  },
  methods: {
    getMovieById(movie_id) {
      axios({
        method: 'GET',
        url: `${this.API_URL}/api/v1/movies/${movie_id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
      .then((res) => {
        console.log(res)
        this.movie = res.data
      })
      .catch((error) => {
        console.log(error)
      })
    }
  },
}
</script>

<style>

</style>