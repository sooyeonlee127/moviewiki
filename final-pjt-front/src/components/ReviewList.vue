<template>
  <div class='review_list'>
    <div class="review_item"
    v-for="(review, idx) in review_list"
    :key="`review_${idx}`"
    :review="review"
    >
      <div>
        <span>작성자: {{ review.user }}</span>
        <br>  
        <span>
          작성일: {{ review.created_at.slice(0,4) }}년 
          {{ review.created_at.slice(5,7) }}월 
          {{ review.created_at.slice(8,10) }}일
        </span>
        <br>
        <span>평점: {{ review.rating }}점</span>
        <br>
        <span>내용: {{ review.content }}</span>
        <button v-if="review.user==user.email" @click="deleteReview(review.id)">삭제</button>
        <hr>
      </div>
    </div>
    <form @submit.prevent="createComment" method="POST">
      <div>
        <label for="rating-inline"></label>
        <b-form-rating id="rating-inline" inline value="value" v-model="rating"></b-form-rating>
      </div>
      <div class="textarea">
        <input class="textarea_input" placeholder="Fixed height textarea" v-model="content" no-resize>
        <input class="textarea_submit" type="submit" value="입력">
      </div>
    </form>
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

.review_list {
  text-align: left;
}

.review_list .review_item {
  padding: 10px 0;
  font-weight: 300;
  border-bottom: 1px solid rgb(29, 29, 29);
  color: rgb(173, 173, 173);
}

.textarea {
  width: 100%;
  height: 70px;
  border-bottom: 1px solid rgb(63, 63, 63);
  display: flex;
  flex-direction: row;
}

.textarea_input {
  background: transparent;
  color: white;
  padding: 0 60px 0 20px;
  width: 100%;
  border: none;
}
.textarea_submit {
  background: rgb(0, 0, 0);
  border: 1px solid rgb(63, 63, 63);
  color: rgb(163, 163, 163);;
  font-weight: 600;
  padding: 0 30px;
  height: 50px;
  margin: 10px;
  transition: 0.1s;
}

.textarea_submit:hover {
  background: white;
  border: 1px solid white;
  color: black;
}

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