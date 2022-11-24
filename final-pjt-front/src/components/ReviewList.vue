<template>
  <div>
    <div style="max-width: 30rem;">

    <form @submit.prevent="createComment" method="POST">
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
    <div
    v-for="(review, idx) in review_list"
    :key="`review_${idx}`"
    :review="review"
    >
      <div>
      <p>작성자: {{ review.user }}</p>
      <p>
        <span>리뷰: {{ review.content }}</span> | 
        <span>작성일: {{ review.created_at }}</span> |
        <span>{{ review.rating }}점</span>
      </p>
      {{ review.user}}
      <p v-if="review.user==user.email"><button @click="deleteReview(review.id)">삭제</button></p>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ReviewList',
  components: {
  },
  data() {
    return {
      content: null,
      rating: null,
      user: null,
      API_URL: this.$store.state.API_URL
    }
  },
  created() {
    this.getUser()
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
    deleteReview(review_id) {
      axios({
        method: 'delete',
        url: `${this.API_URL}/api/v1/movies/comments/${review_id}/`,
        headers: {
          'Authorization': `Token ${this.$store.state.token}`
        },
      })
      .then((res) => {
        console.log(res)
        const itemToFind = this.review_list.find(function(item) {return item.id === review_id})
        const idx = this.review_list.indexOf(itemToFind)
        if (idx > -1) this.review_list.splice(idx, 1)
      })
      .catch((error) => {
        console.log(error)
      })
    },
    getUser() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/user/`,
        headers: {
          'Authorization': `Token ${this.$store.state.token}`
        },
      })
      .then((res) => {
        console.log(res)
        this.user = res.data
        console.log(res.data)
        console.log('회원정보')
      })
      .catch((error) => {
        console.log('회원정보 실패')
        console.log(error)
      })
    },
    
  }
  }


</script>

<style>
/*
=====
DEPENDENCES
=====
*/

.screen-reader{
  width: var(--screenReaderWidth, 1px) !important;
  height: var(--screenReaderHeight, 1px) !important;
  padding: var(--screenReaderPadding, 0) !important;
  border: var(--screenReaderBorder, none) !important;

  position: var(--screenReaderPosition, absolute) !important;
  clip: var(--screenReaderClip, rect(1px, 1px, 1px, 1px)) !important;
  overflow: var(--screenReaderOverflow, hidden) !important;
}

/*
=====
CORE STYLES
=====
*/

.rating{
  --uiRatingColor: var(--ratingColor, #eee);
  --uiRatingColorActive: var(--ratingColorActive, #ffcc00);

  display: var(--ratingDisplay, flex);
  font-size: var(--ratingSize, 1rem);
  color: var(--uiRatingColor);
}
    
.rating__control:nth-of-type(1):focus ~ .rating__item:nth-of-type(1)::before,
.rating__control:nth-of-type(2):focus ~ .rating__item:nth-of-type(2)::before,
.rating__control:nth-of-type(3):focus ~ .rating__item:nth-of-type(3)::before,
.rating__control:nth-of-type(4):focus ~ .rating__item:nth-of-type(4)::before,
.rating__control:nth-of-type(5):focus ~ .rating__item:nth-of-type(5)::before{
  content: ""; 
  box-shadow: 0 0 0 var(--ratingOutlineWidth, 4px) var(--uiRatingColorActive);

  position: absolute;
  top: -.15em;
  right: 0;
  bottom: -.15em;
  left: 0;
  z-index: -1;
}

.rating__item{
  cursor: pointer;  
  position: relative;
}

.rating__item{
  padding-left: .25em;
  padding-right: .25em;
}

.rating__star{
  display: block;
  width: 1em;
  height: 1em;

  fill: currentColor;
  stroke: var(--ratingStroke, #222);
  stroke-width: var(--ratingStrokeWidth, 1px);
}

.rating:hover,
.rating__control:nth-of-type(1):checked ~ .rating__item:nth-of-type(1),
.rating__control:nth-of-type(2):checked ~ .rating__item:nth-of-type(-n+2),
.rating__control:nth-of-type(3):checked ~ .rating__item:nth-of-type(-n+3),
.rating__control:nth-of-type(4):checked ~ .rating__item:nth-of-type(-n+4),
.rating__control:nth-of-type(5):checked ~ .rating__item:nth-of-type(-n+5){
  color: var(--uiRatingColorActive);
}

.rating__item:hover ~ .rating__item{
  color: var(--uiRatingColor);
}

/*
=====
SETTINGS
=====
*/

.rating{
  --ratingSize: 2rem;
  --ratingColor: #eee;
  --ratingColorActive: #ffcc00;
}

/*
=====
DEMO
=====
*/

/* body{
  font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Open Sans, Ubuntu, Fira Sans, Helvetica Neue, sans-serif;
  font-size: 1rem;
  margin: 0;
} */

.page{
  min-height: 100vh;
  display: flex;
}

.page__demo{
  margin: auto;  
}

.page__group{
  margin-top: 2rem;
  margin-bottom: 2rem;
  text-align: center;
}

.page__hint{
  display: block;
  font-weight: 700;
  margin-top: 1rem;
}

@media (min-width: 641px){
  .page__demo{
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
  }

  .page__group{
    margin-left: 3.5rem;
    margin-right: 3.5rem;
  }
}

</style>