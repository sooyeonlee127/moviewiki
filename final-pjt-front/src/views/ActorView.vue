<template>
  <div class="actor">
    <div class="actor_content">
      <caption>
        <p>
          이름: {{ actor.name }}
          <br>
          출생지: {{ actor.place_of_birth }}
          <br>
          출생연도: {{actor.birthday.slice(0,4)}}년 
          {{actor.birthday.slice(5,7)}}월 
          {{actor.birthday.slice(8,10)}}일
        </p>
      </caption>
    </div>
    <div class="actor_content">
      <img :src="`https://image.tmdb.org/t/p/original/${ actor.profile_path }`" style="width: 300px;" fluid alt="Fluid image">
    </div>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
  </div>
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
.actor {
  width: 100%;
  margin: 20px auto;
  height: 100%;
  min-height: 500px;
  background: black;
  margin: 100px;


}

.actor_content {
  margin-bottom: 60px;
  height: 100%;;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: start;
}

.actor_content > caption {
  line-height: 60px;
  font-size: 40px;    /* 원래 60*/ 
  color: white;
  font-weight: 500;
 
}
.actor_content > caption > span {
  color: rgb(137, 255, 68);
}

.actor_content > p {
  line-height: 60px;
  font-size: 30px; 
  color: white;
  font-weight: 1;
  align-items: start;
 
}


</style>