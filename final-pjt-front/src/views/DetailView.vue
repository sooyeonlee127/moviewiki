<template>
  <div class="container">
  <div class="element" :style="{ backgroundImage: 'url(https://image.tmdb.org/t/p/original/' + movie.backdrop_path + ')' }">
    <div class="content">
      <img class="child box scale" 
        :src="`https://image.tmdb.org/t/p/original/${ movie.poster_path }`" 
         align="right" 
      >
      <h1>
        {{ movie.title }}
      </h1>
      <p id="text" align="left">
        <span class="material-symbols-outlined"> closed_caption </span>
        {{ movie.release_date.slice(0,4)}} 개봉 | 평점 {{ movie.vote_average }}점
      </p>
      <p id="text"> 
        {{ movie.overview }}
      </p>
    </div>
    <div>
      <db-container class="bv-example-row" id="actorlist">
        <b-row>
          <div id="actoritem">
          <b-avatar
            rounded="lg"
            :src="`https://image.tmdb.org/t/p/original/${ credit[0].profile_path }`"     
            size="100px"
          >
          </b-avatar>
          </div>
          <div id="actoritem">
          <b-avatar
            rounded="lg"
            :src="`https://image.tmdb.org/t/p/original/${ credit[1].profile_path }`"     
            size="100px"
          >
          </b-avatar>
          </div>
          <div id="actoritem">
          <b-avatar
            rounded="lg"
            :src="`https://image.tmdb.org/t/p/original/${ credit[3].profile_path }`"     
            size="100px"
          >
          </b-avatar>
        </div>
        </b-row>
      </db-container>
      <db-container class="bv-example-row" id="actorlist">
        <b-row>
          <div id="actoritem">
            {{ credit[0].name }}
          </div>
          <div id="actoritem">
            {{ credit[1].name }}
          </div>
          <div id="actoritem">
            {{ credit[2].name }}
          </div>
        </b-row>
      </db-container>
    </div>

    <div id="review">
        <b-button v-b-modal.modal-xl variant="primary" @click="getVideo">예고편</b-button>
        <b-modal id="modal-xl" size="xl" :title="`${ this.movie.title }`">
          <div>
            <b-embed
              type="iframe"
              aspect="16by9"
              :src="`https://youtube.com/embed/${this.video}`"
              allowfullscreen
            ></b-embed>
          </div>
        </b-modal>
        
        <ReviewList
        :reviews="movie.comment_set"
        :movie_id="movie.id"
        />
    </div>
  </div>
</div>
</template>

<script>
import ReviewList from '../components/ReviewList.vue'
import axios from 'axios'

const API_URL = 'https://www.googleapis.com/youtube/v3/search'
const API_KEY = 'AIzaSyDNA1XX0lkSwTF_ps6UJAuDMbsFmNakoeE'

export default {
  name: 'DetailView',
  data() {
    return {
      movie: [],
      API_URL: this.$store.state.API_URL,
      credit: [],
      video: '',
    }
  },
  components: {
    ReviewList,
  },
  created() {
    this.getMovieById(this.$route.params.movie_id)
    this.requestCredit(this.$route.params.movie_id)

  },
  methods: {
    getMovieById(movie_id) {
      axios({
        method: 'GET',
        url: `${this.API_URL}/api/v1/movies/${movie_id}/`,
      })
      .then((res) => {
        console.log(res)
        this.movie = res.data
      })
      .catch((error) => {
        console.log(error)
      })
    },
    requestCredit(movie_id) {
      const API_URL = `https://api.themoviedb.org/3/movie/${movie_id}/credits`
      const API_KEY = '53b8d4bdf76930f30d64c0bcd333285a'

      axios.get(API_URL, {
        params: {
            api_key: API_KEY,
            language: 'ko',
        }
      }).then((response) => {
        const credit = response.data.cast
        this.credit = credit
        console.log('credit')
        console.log(this.credit)

      }).catch((error) => {
          console.error(error)
      })
    },
    getVideo() {
      axios.get(API_URL, {
        params: {
            key: API_KEY,
            type: 'video',
            part: 'snippet',
            q: this.movie.title + '예고편'
        }
    }).then((response) => {
        this.video = response.data.items[0].id.videoId
        console.log('video')
        console.log(this.video)
    }).catch((error) => {
        console.error(error)
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
  position: absolute;
  z-index: 1;
  top: 600px;
  left: 50px;
}



.container {
  height: 100%;
}

#actorlist {
  position: relative;
  top: 250px;
  border-radius: 6px;
  animation-iteration-count: infinite;
  box-shadow: 10px 10px 5px rgba(0, 0, 0, 0.102);
}

#actoritem {
  width: 150px;
}

#text{
  position: relative;
  z-index: 2;
  top: 200px;
  left: 5px;
  font-size: 1vw;
  color:#fff;
  text-shadow: 1px 1px 2px rgb(0, 0, 0), 0 0 1em rgb(15, 14, 14), 0 0 0.2em rgb(0, 0, 0);
  z-index: 2;

}


body {
  font-family: 'Nanum Gothic', sans-serif;
}

.content {
  text-align: center;
  position: relative;
  z-index: 2;
}
.content h1 {
  font-size: 3vw;
  color: #fff;
  position: relative;
  font-weight: bold;
  top: 200px;
  text-shadow: 1px 1px 2px rgb(0, 0, 0), 0 0 1em rgb(15, 14, 14), 0 0 0.2em rgb(0, 0, 0);
}


.element {
  height: 100vh;
  position: relative;
  background-size: cover;
  top: 30px;
  left: 0px;
  right: 0px;
  bottom: 0px;
  z-index: 0;
}

.element::before {
  height: 100%;
  width: 50%;
  content: "";
  position: absolute;
  top: 0px;
  left: 0px;
  bottom: 0px;
  background: linear-gradient(
    to right, rgb(0, 0, 0),transparent
  );
  /* background-color: #000; */
  z-index: -1;
}


.element::after {
  height: 100%;
  width: 50%;
  content: "";
  position: absolute;
  top: 0px;
  right: 0px;
  bottom: 0px;
  background: linear-gradient(
    to left, rgb(0, 0, 0),transparent
  );
  /* background-color: #000; */
  z-index: -1;
}


.box {
    margin-top: 100px;
    margin-right: 110px;
    width: 300px;
    height: 450px;
    line-height: 500px;
    color: white;
    border-radius: 6px;
    animation-iteration-count: infinite;
    box-shadow: 10px 10px 5px rgba(0, 0, 0, 0.102);
    z-index: 2;

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

  .material-symbols-outlined {
    font-variation-settings:
    'FILL' 0,
    'wght' 400,
    'GRAD' 0,
    'opsz' 48
  }

</style>