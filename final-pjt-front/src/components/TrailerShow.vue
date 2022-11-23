<template>
  <div>
    <b-embed
      type="iframe"
      aspect="16by9"
      :src="`https://youtube.com/embed/${this.video}`"
      allowfullscreen
    ></b-embed>

  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'https://www.googleapis.com/youtube/v3/search'
const API_KEY = 'AIzaSyDNA1XX0lkSwTF_ps6UJAuDMbsFmNakoeE'

export default {
  name: 'TrailerShow',
  data() {
    return {
      movie_title: this.$route.params.movie_title,
      video: '',
    }
  },
  created() {
    this.getVideo()
  },
  methods: {
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
  }
}
</script>

<style>

</style>