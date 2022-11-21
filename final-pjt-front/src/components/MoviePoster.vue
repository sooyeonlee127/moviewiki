<template>
  <div>
    <b-carousel
      id="carousel-1"
      v-model="slide"
      :interval="4000"
      indicators
      controls
      fade="true"
      label-next=" "
      label-prev=" "
      background="#000"
      img-width="1024"
      img-height="480"
      style="text-shadow: 1px 1px 2px #333;"
    >
      <!-- Text slides with image -->
      <b-carousel-slide :img-src="`https://image.tmdb.org/t/p/original/${ movies[1]?.backdrop_path }`"
      ></b-carousel-slide>

      <!-- Slides with custom text -->
      <b-carousel-slide :img-src="`https://image.tmdb.org/t/p/original/${ movies[1]?.backdrop_path }`"
      ></b-carousel-slide>

      <b-carousel-slide :img-src="`https://image.tmdb.org/t/p/original/${ movies[0].backdrop_path }`">
        <h1>
          {{ movies[0].title }}
        </h1>
      </b-carousel-slide>

      <b-carousel-slide :img-src="`https://image.tmdb.org/t/p/original/${ movies[1].backdrop_path }`">
        <h1>
          {{ movies[1].title }}
        </h1>
      </b-carousel-slide>

      <b-carousel-slide :img-src="`https://image.tmdb.org/t/p/original/${ movies[2].backdrop_path }`">
        <h1>
          {{ movies[2].title }}
        </h1>
      </b-carousel-slide>

    </b-carousel>
  </div>
</template>

<script>
  export default {
    name: 'MoviePoster',
    data() {
      return {
        slide: 0,
        sliding: null,
        myStyle:{
          backgroundColor:"#000" 
        }
      }
    },
    
    props: {
      movies: Array,
    },
    methods: {
      onSlideStart(slide) {
        this.sliding = true
        console.log(slide)
      },
      onSlideEnd(slide) {
        this.sliding = false
        console.log(slide)
      }
    },
    computed: {
    }
  }
</script>

<style>

</style>