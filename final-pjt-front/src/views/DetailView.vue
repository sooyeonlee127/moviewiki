<template>
  <div class="container" style="padding: 0;">
    <div class="element">
      <div class="content row m-0" :style="{ backgroundImage: 'linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url(https://image.tmdb.org/t/p/original/' + movie.backdrop_path + ')' }">
        <div class="movie_info col-8">
          <h1 class="movie_title">{{ movie.title }}</h1>
          <table class="movie_summery">
            <tr>
              <td>{{ movie.release_date.slice(0,4)}}</td>
              <td>{{ movie.vote_average }}점</td>
            </tr>
            <tr>
              <td>개봉</td>
              <td>평점</td>
            </tr>
          </table>
        </div>
        <img class="detail_poster col-4" 
          :src="`https://image.tmdb.org/t/p/original/${ movie.poster_path }`"  
        >
      </div>
      <div class="section">
        <section class="row">
          <div class="col-8">
            <div class="information">
              <p style="font-size: 30px; text-align:center;">줄거리</p>
              <div class="overview">
                {{ movie.overview }}
              </div>
            <div style="display: flex; flex-direction: row;">
              <button class="btnGroup" v-b-modal.modal-xl @click="getVideo">Trailer</button>
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
              </div>
            </div>
            <div class="review">
              <ReviewList
              :reviews="movie.comment_set"
              :movie_id="movie.id"
              />
            </div>
          </div>
          <div class="actorlist col-4">
            <p style="font-size: 30px; text-align:center;">Actors</p>
            <vue-custom-scrollbar class="scroll-area"  :settings="settings" @ps-scroll-y="scrollHanle">
              <div class="row" style="margin:0;">
                <div 
                v-for="(actor, idx) in credit"
                :key="`actor_${idx}`"
                :actor="actor"
                class="actoritem col-4"
                >
                  <img :src="`https://image.tmdb.org/t/p/original/${ actor.profile_path }`">
                  <p>{{ actor.name }}</p>
                </div>
              </div>
            </vue-custom-scrollbar>
          </div>
        </section>
      </div>
    </div>
  </div>
</template>

<script>
import ReviewList from '../components/ReviewList.vue'
import axios from 'axios'
import vueCustomScrollbar from 'vue-custom-scrollbar'
import "vue-custom-scrollbar/dist/vueScrollbar.css"

const API_URL = 'https://www.googleapis.com/youtube/v3/search'
const API_KEY = 'AIzaSyDNA1XX0lkSwTF_ps6UJAuDMbsFmNakoeE'

export default {
  name: 'DetailView',
  data() {
    return {
      movie: {
        id: null,
        adult: null,
        original_language: null,
        original_title: null,
        overview: null,
        popularity: null,
        release_date: null,
        title: null,
        video: null,
        vote_average: null,
        vote_count: null,
        genre_ids: null,
      },
      API_URL: this.$store.state.API_URL,
      credit: [
        {
          name: null,
        }
      ],
      video: '',
      settings: {
        suppressScrollY: false,
        suppressScrollX: false,
        wheelPropagation: false
      },
    }
  },
  components: {
    ReviewList,
    vueCustomScrollbar,
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
      .catch(() => {
        this.createMovie(movie_id)
      })
    },
    createMovie(movie_id) {
      const API_URL = `https://api.themoviedb.org/3/movie/${movie_id}`
      const API_KEY = '53b8d4bdf76930f30d64c0bcd333285a'
      axios({
        method: 'GET',
        url: API_URL,
        params: {
          'api_key': API_KEY,
        }
      })
      .then((res) => {
        console.log(res.data)
        this.movie=res.data
        axios({
          method: 'POST',
          url: `${this.API_URL}/api/v1/movies/create/`,
          headers: {
            'Authorization': `Token ${this.$store.state.token}`
          },
          data: {
            'movie': this.movie
          },
        })
        .then((res) => {
          console.log(res)
        })
        .catch((err) => {
          console.log(err)
        })
      })
      .catch((err) => {
        console.log(err)
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
        const credit = response.data.cast.slice(0,10)
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
    },
    scrollHanle(evt) {
      console.log(evt)
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




.element {
  height: 100%;
  position: relative;
  background-size: cover;
  top: 0px;
  left: 0px;
  z-index: 0;
}
.content{
  padding: 20px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  
}
.detail_poster {
  padding: 0 !important;
  box-shadow: 0px 0px 50px 5px black;
}
.movie_info {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: start;
  box-sizing: border-box;
  padding-left: 100px !important;
}

.movie_title {
  text-align: left;
  margin: 0 0 30px 0;
  font-weight: 600;
}

.movie_summery {
  text-align: left;
}

.movie_summery tr:first-child{
  font-weight: 600;
  font-size: 30px;
}

.movie_summery tr:last-child {
  color: rgb(184, 184, 184);
  text-align: center;
  font-size: 15px;
}

.movie_summery tr td {
  padding: 0 30px 0 0;
}


.actorlist {
  padding: 0 !important;
}

.actorlist .actoritem {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 0;
  padding: 10px;
  z-index: -1;
}
.actorlist .actoritem img {
  height: 100px;
  width: 100%;
  object-fit: cover;
  margin-bottom: 5px;
}

.scroll-area {
  position: relative;
  margin: 0 auto;
  padding: 0;
  height: 450px;
  box-shadow: inset 0px -30px 20px -10px black;
}
section {
  margin: 0;
}
.section {
  padding: 20px;
}
.information {
  padding: 0 50px 0 0;
}

.overview {
  padding: 10px;
  text-align: left;
  min-height: 120px;
}

.review {
  margin-top: 50px;
}

.btnGroup{
  font-size: 25px;
  font-weight: 500;
  width: 250px;
  background: transparent;
  border: 3px solid rgb(165, 165, 165);
  color: rgb(165, 165, 165);
  transition: 0.1s;
}
.btnGroup:hover {
  background: rgb(255, 255, 255);
  border: 3px solid rgb(255, 255, 255);
  color: rgb(0, 0, 0);
}
</style>