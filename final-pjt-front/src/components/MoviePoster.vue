<template>
  <div class="slider" >
    <!-- Slider component -->
    <slider ref="slider" :options="options">
        <!-- slideritem -->
        <slideritem class="slideritem">
          <button>
            More detail
            <div></div>
          </button>
          <div class="movie_info">
            <span>32K+</span>
            <span>20K+</span>
            <span>10K+</span>
          </div>
          <img src="https://www.pngmart.com/files/21/Actor-PNG-Isolated-File.png" style="width: 300px" alt="">
        </slideritem>
        <slideritem class="slideritem">
          <img src="https://www.pngall.com/wp-content/uploads/4/Standing-Jason-Statham-PNG.png" style="width: 300px" alt="">
        </slideritem>
        <!-- Customizable loading indicator -->
        <div slot="loading">loading...</div>
    </slider>
  </div>
</template>

<script>
import { slider, slideritem } from 'vue-concise-slider'
  export default {
    name: 'MoviePoster',
    data() {
      return {
        options: {
          currentPage: 0
        }
      }
        
    },
    components: {
      slider,
      slideritem
    },
    props: {
      movies: Array,
    },
    methods: {
    },
    computed: {
    }
  }
</script>

<style>
.slider {
  width: 100%;
  margin: 20px auto;
  height: 700px
}
.slideritem > img {
  margin-left: 30px;
}
.slideritem button {
  border-radius: 10px;
  padding: 10px 20px;
  font-size: 30px;
  font-weight: 800;
  background-color: rgb(137, 255, 68);
}
.movie_info > span {
  font-size: 30px;
  margin: 0 15px;
}
</style>