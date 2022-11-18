<template>
  <div>
    <h1>DetailView</h1>
    <DetailItem
      :movie="this.movie"/>
    <ReviewCreate/>
    <hr>


  </div>
</template>

<script>
import ReviewCreate from '@/components/ReviewCreate.vue'
import DetailItem from '@/components/DetailItem.vue'


export default {
  name: 'DetailView',
  data() {
    return {
      movie: null
    }
  },
  components: {
    ReviewCreate,
    DetailItem
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