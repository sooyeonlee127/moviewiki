<template>
  <div>
    <div style="max-width: 30rem;">
    <ReviewListItem
    v-for="(review, idx) in review_list"
    :key="`review_${idx}`"
    :review="review"
    />
    <form @submit.prevent="createComment" method="POST">
      <h3></h3>
      <div>
        <label for="rating-inline">별점 : </label>
        <b-form-rating id="rating-inline" inline value="value" v-model="rating"></b-form-rating>
      </div>
      <b-form-textarea
        class="textarea"
        id="content-textarea-no-resize"
        placeholder="Fixed height textarea"
        rows="3"
        v-model="content"
        no-resize
      ></b-form-textarea>
      <b-button variant="secondary" type="submit">입력</b-button>
    </form>
  </div>

  </div>
</template>

<script>
import axios from 'axios'
import ReviewListItem from '@/components/ReviewListItem.vue'

export default {
  name: 'ReviewList',
  components: {
    ReviewListItem,
  },
  data() {
    return {
      content: null,
      rating: null,
      API_URL: this.$store.state.API_URL
    }
  },
  props: {
    reviews: Array,
    movie_id: Number,
  },
  computed: {
    review_list() {
      return this.reviews
    }
  },  
  methods: {
    createComment() {
      axios({
        method: 'POST',
        url: `${this.API_URL}/api/v1/movies/${this.movie_id}/comment_create/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data: {
          content: this.content,
          rating: this.rating,
        }
      })
      .then((res) => {
        const review = res.data
        this.review_list.push(review)
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