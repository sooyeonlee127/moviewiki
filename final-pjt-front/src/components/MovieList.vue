<template>
  <div>
    <h3>꼭 봐야하는 콘텐츠</h3>
    <div class="wrap_slider">
      <button @click="slide" class="slider_btn" id="left"><img src="@/assets/left-arrow.png" alt=""></button>
      <slider ref="slider" :options="options">
        <slideritem class="movie_item" 
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie">
        <img v-if="movie.adult==false" @click="SelectedMovie(movie.id)" :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`" img-alt="Card Image" alt="">
        </slideritem>
        <div slot="loading">영화를 불러오고 있어요</div>
      </slider>
      <button @click="slideNext" class="slider_btn" id="right"><img src="@/assets/right-arrow.png" alt=""></button>
    </div>
  </div>
</template>

<script>
import { slider, slideritem } from 'vue-concise-slider'

export default {
  name: 'MovieList',
  props: {
    movies: Array
  },
  data () {
    return {
      options: {
        currentPage: 0,
        thresholdDistance: 10,
        slidesToScroll: 5,
        loopedSlides:5,
        pagination: false,
      }
    }
  },
  methods: {
    SelectedMovie(movie_id) {
      console.log(movie_id)
      this.$router.push({name: 'detail', params: {movie_id}})
    },
    slideNext () {
      this.$refs.slider.$emit('slideNext')
    },
    slide () {
      this.$refs.slider.$emit('slidePre')
    }
  },
  components: {
    slider,
    slideritem,
  },
}
</script>

<style>

</style>