<template>
  <b-container class="bv-example-row">
    <b-row>
      <b-col align-self="center">
        <h3>이름: {{ actor.name }}</h3>
        <h3>출생지: {{ actor.place_of_birth }}</h3>
        <h3>
          출생연도: {{actor.birthday.slice(0,4)}}년 
          {{actor.birthday.slice(5,7)}}월 
          {{actor.birthday.slice(8,10)}}일
        </h3>
      </b-col>
      <b-col align-self="center">
        <img :src="`https://image.tmdb.org/t/p/original/${ actor.profile_path }`" style="width: 300px;" fluid alt="Fluid image">
      </b-col>
  </b-row>
  </b-container>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ActorView',
  data() {
    return {
      actor : [],
    }
  },
  created() {
    this.actor = this.$route.params.actor_id
    this.SearchActor(this.actor)
  },
  methods: {
    SearchActor(actor_id) {
      const API_URL = `https://api.themoviedb.org/3/person/${actor_id}`
      const API_KEY = '53b8d4bdf76930f30d64c0bcd333285a'
      axios.get(API_URL, {
        params: {
            api_key: API_KEY,
            language: 'ko',
        }
      }).then((res) => {
        const actor = res.data
        this.actor = actor
      }).catch((error) => {
          console.error(error)
      })
    },
    }
  }
</script>

<style>

</style>