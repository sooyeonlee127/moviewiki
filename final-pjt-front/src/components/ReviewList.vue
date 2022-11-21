<template>
  <div>
    <div style="max-width: 30rem;">
    <form @submit.prevent="createComment">
      <h3></h3>
      <div>
        <label for="rating-inline">별점 : </label>
        <b-form-rating id="rating-inline" inline value="value"></b-form-rating>
      </div>
      <b-form-textarea
        id="content-textarea-no-resize"
        placeholder="Fixed height textarea"
        rows="3"
        v-model="content"
        no-resize
      ></b-form-textarea>
      <input type="submit">
    </form>
  </div>
    <ReviewListItem/>
  </div>
</template>

<script>
import axios from 'axios'
import ReviewListItem from '@/components/ReviewListItem.vue'

const API_URL = "http://127.0.0.1:8000" // django 서버

export default {
  name: 'ReviewList',
  components: {
    ReviewListItem,
  },
  data() {
    return {
      content: null,
    }
  },  
  props: {
    movie: Object,
  },
  methods: {
    createComment() {
      console.log(this.content)
      axios({
        method: 'POST',
        url: `${API_URL}/api/v1/movies/${this.movie.id}/comment_create/`,
        header: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data: {
          content: this.content,
        }
      })
      .then((res) => {
        console.log(res)
      })
      .catch((error) => {
        console.log(error)
      })
    },
  }

}
</script>

<style>

</style>