<template>
    <div class="slider" >
      <!-- Slider component -->
      <slider ref="slider" :options="options">
        <!-- slideritem -->
        <slideritem>
          <div class="slider_content">
            <caption>
              하이테크
              <br>
              슈퍼히어로의 탄생
              <!-- Lorem ipsum <br>dolor sit. -->
            </caption>
            <p>
              <button @click="getTrailer('아이언맨')">
                Trailer
              </button>
              <button @click="getSearch('아이언맨')">
                More detail
              </button>
            </p>
            <table class="movie_info">
              <tr>
                <td>32K+</td>
                <td>109K+</td>
                <td>10K+</td>
              </tr>
              <tr>
                <td>Reviews</td>
                <td>Popularity</td>
                <td>Likes</td>
              </tr>
            </table>
          </div>
          <img src="@/assets/Actor-PNG-Isolated-File.png" style="width: 300px" alt="">
        </slideritem>
        <slideritem>
          <div class="slider_content">
            <caption>
              지상 최강의 액션 블록버스터, <br> 분노의 질주
            </caption>
            <p>
              <button id="clickbtn" @click="getTrailer('분노의 질주')">
                Trailer
              </button>
              <button @click="getSearch('분노의 질주')">
                More detail
              </button>
            </p>
            <table class="movie_info">
              <tr>
                <td>32K+</td>
                <td>20K+</td>
                <td>10K+</td>
              </tr>
              <tr>
                <td>Reviews</td>
                <td>Popularity</td>
                <td>Likes</td>
              </tr>
            </table>
          </div>
          <img src="@/assets/Standing-Jason-Statham-PNG.png" style="width: 300px" alt="">
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
          currentPage: 0,
          thresholdDistance: 500,
          thresholdTime: 100,
          pagination: true,
          speed: 1500,
          // loop: true,
          autoplay:7000,
        }
      }
    },
    components: {
      slider,
      slideritem,
    },
    props: {
      movies: Array,
    },
    methods: {
      getTrailer(movie_title) {
        this.$router.push({name: 'trailer', params: {movie_title}})
      },
      getSearch(movie_title) {
        this.$router.push({name: 'search', params: {movie_title}})
      }
      }

    }
  
</script>

<style>

.slider {
  width: 100%;
  margin: 20px auto;
  height: 60vh;
  min-height: 500px;
  background: black;

}

.slider_content {
  height: 100%;;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: start;
  margin-right: 50px;
}

.slider_content > caption {
  line-height: 60px;
  font-size: 60px;    /* 원래 60*/
  margin-bottom: 70px; 
  color: white;
  font-weight: 700; 
}

.slider_content > img {
  margin-left: 30px;
}


.slider_content button {
  padding: 10px 20px;
  box-sizing: border-box;
  font-size: 25px;
  font-weight: 700;
  height: 60px;
  border: 3px solid rgb(137, 255, 68);
  background-color: rgb(137, 255, 68);
}

.slider_content button:first-child {
  margin-right: 30px;
}

.slider_content button:first-child:hover{
  border: 3px solid rgb(255, 255, 255);
  background-color: rgb(255, 255, 255);
}

.slider_content button:last-child {
  color: rgb(137, 255, 68);
  border: 3px solid rgb(137, 255, 68);
  background: transparent;
}

.slider_content button:last-child:hover{
  color: white;
  border: 3px solid rgb(255, 255, 255);
}

.slider-pagination-bullet, .slider-pagination-bullet-active{
  background: rgb(137, 255, 68) !important;
  padding: 5px;
}

.movie_info {
  margin-top: 30px;
  text-align: left;
}

.movie_info tr, .movie_info td{
  padding: 0 30px 0 0;
  margin: 0;
  border: none;
}

.movie_info tr:first-child{
  font-size: 30px;
}

.movie_info tr:last-child {
  opacity: 0.6;
  font-size: 15px;
}

</style>