<template>
  <div class="container">
    <hr>
    <div>
      <img :src="`https://image.tmdb.org/t/p/original/${img}`" style="width: 120px;">
      <p>영화제목: {{ title }}</p>
      <p>작성일: {{ review.created_at.slice(0,4) }}년 
        {{ review.created_at.slice(5,7) }}월 
        {{ review.created_at.slice(8,10) }}일</p>
      <p>평점: {{ review.rating }}점</p>
      <p>내용: {{ review.content }} </p>       
    </div>
    <button @click="deleteReview(review.id)">삭제</button>
  </div>
</template>

<script>
import axios from 'axios'


export default {
  name: 'ProfileReview',
  data() {
    return {
      title: null,
      img: null,
    }
  },
  props: {
    review : Object,
  },
  created() {
    this.getReviewMovieTitle(this.review.movie)
  },
  methods: {
    getReviewMovieTitle(movie_id) { 
      axios({
        method: 'GET',
        url: `http://127.0.0.1:8000/api/v1/movies/${movie_id}/`,
      })
      .then((res) => {
        this.title = res.data.title
        this.img = res.data.poster_path
      })
      .catch((error) => {
        console.log(error)
      })
    },
    deleteReview(review_id) {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/api/v1/movies/comments/${review_id}`,
        headers: {
          'Authorization': `Token ${this.$store.state.token}`
        },
      })
      .then((res) => {
        console.log(res)
        console.log('삭제 성공!')
        this.$emit('delete-review', review_id)
      })
      .catch((error) => {
        console.log(error)
      })
    }
  }
}
</script>

<style>

</style>