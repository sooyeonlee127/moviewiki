<template>
  <div class="element" :style="{ backgroundImage: 'url(https://image.tmdb.org/t/p/original/' + movie.backdrop_path + ')' }">
    <div class="font">
      <img class="child box scale" 
        :src="`https://image.tmdb.org/t/p/original/${ movie.poster_path }`" 
         align="right" 
      >
      <div id="review">
        <ReviewList
        :reviews="movie.comment_set"
        :movie_id="movie.id"
        />
      </div>
      <b-icon-arrow-up></b-icon-arrow-up>


      <h1>
        {{ movie.title }}
      </h1>

      <p id="text" align="left">
        <span class="material-symbols-outlined"> closed_caption </span>
        {{ movie.release_date.slice(0,4)}}
      </p>
      <p id="text"> 
        {{ movie.overview }}
      </p>
    </div>

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
  computed: {
    back() {
      return {
        '--back-url' :  'https://image.tmdb.org/t/p/original/'+ this.movie.backdrop_path
      }
    }
  }

}
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200");
@import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@400;700;800&display=swap');


#review {
  position: relative;
  z-index: 2;
  top: 500px;
  left: 50px;
}

#text{
  position: relative;
  z-index: 2;
  top: 60px;
  left: 50px;
}

body {
  font-family: 'Nanum Gothic', sans-serif;
  -webkit-font-smoothing: antialiassed;
  -moz-osx-font-smoothing: grayscale;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;

}
.font {
  text-align: center;
}
.font h1 {
  font-size: 8vw;
  color: #fff;
  position: relative;
  top: -20px;
  text-shadow: 1px 1px 2px rgb(0, 0, 0), 0 0 1em rgb(15, 14, 14), 0 0 0.2em rgb(0, 0, 0);
}


/* ---------------------- */




.element {
  width: 100vw;
  height: 100vh;
  position: relative;
  background-size: cover;
  top: 0px;
  left: 0px;
  right: 0px;
  bottom: 0px;

}

.element::before {
  width: 100vw;
  height: 100vh;
  content: "";
  opacity: 0.5;
  position: absolute;
  top: 0px;
  left: 0px;
  right: 0px;
  bottom: 0px;

  /* background: linear-gradient(
            to left,
            rgba(20, 20, 20, 0) 15%,
            rgba(20, 20, 20, 0.25) 25%,
            rgba(20, 20, 20, 0.5) 50%,
            rgba(20, 20, 20, 0.75) 75%,*/

  background-color: #000;
}

.box {
    margin: 60px;
    width: 300px;
    height: 450px;
    line-height: 500px;
    color: white;
    text-align: center;
    border-radius: 6px;
    animation-iteration-count: infinite;
    box-shadow: 10px 10px 5px rgba(245, 245, 245, 0.102);

  }
  /* .original {
    margin: 30px;
    border: 1px dashed #cecfd5;
    background: #eaeaed;
    float: left;
  } */
  .child {
    background: #2db34a;
    cursor: pointer;
  }
  .scale {
    transform: scale(.95);
  }
  .scale:hover {
    transition: transform 1s linear;
    transform: scale(1);
  }
  /* --------------아이콘 */
  .material-symbols-outlined {
    font-variation-settings:
    'FILL' 0,
    'wght' 400,
    'GRAD' 0,
    'opsz' 48
  }

</style>