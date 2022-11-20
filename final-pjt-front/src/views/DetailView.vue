<template>
  <div>
    <!-- <div class="mt-4">
      <b-card 
      :img-src="`https://image.tmdb.org/t/p/original/${ movie.poster_path }`" 
      style="width: 10rem; height:15rem;"
      img-art="card image" img-right
      >
        <b-card-text>
        {{ movie.title }}
          개봉일: {{ movie.release_date}}
          {{ movie.genre_ids }}
        </b-card-text>
      </b-card>
    </div> -->
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