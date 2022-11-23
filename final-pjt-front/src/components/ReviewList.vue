<template>
  <div>
    <div style="max-width: 30rem;">

    <form @submit.prevent="createComment" method="POST">
      <!-- <h3>-------------------------</h3>
      <div class="page">
        <div class="page__demo">
          <div class="page__group">
            <div class="rating">
              <input type="radio" name="rating-star" class="rating__control screen-reader" id="rc1" @click="this.rating=1">
              <input type="radio" name="rating-star" class="rating__control screen-reader" id="rc2" @click="this.rating=2">
              <input type="radio" name="rating-star" class="rating__control screen-reader" id="rc3" @click="this.rating=3">
              <input type="radio" name="rating-star" class="rating__control screen-reader" id="rc4" @click="this.rating=4">
              <input type="radio" name="rating-star" class="rating__control screen-reader" id="rc5" @click="this.rating=5">
              <label for="rc1" class="rating__item">
                <svg class="rating__star">
                  <use xlink:href="#star"></use>
                </svg>
                <span class="screen-reader">1</span>
              </label>
              <label for="rc2" class="rating__item">
                <svg class="rating__star">
                  <use xlink:href="#star"></use>
                </svg>
                <span class="screen-reader">2</span>
              </label>
              <label for="rc3" class="rating__item">
                <svg class="rating__star">
                  <use xlink:href="#star"></use>
                </svg>
                <span class="screen-reader">3</span>
              </label>
              <label for="rc4" class="rating__item">
                <svg class="rating__star">
                  <use xlink:href="#star"></use>
                </svg>
                <span class="screen-reader">4</span>
              </label>
              <label for="rc5" class="rating__item">
                <svg class="rating__star">
                  <use xlink:href="#star"></use>
                </svg>
                <span class="screen-reader">5</span>
              </label>	
            </div>
            <span class="page__hint">unselected state</span>
          </div>
        </div>
      </div>
      <svg xmlns="http://www.w3.org/2000/svg" style="display: none">
        <symbol id="star" viewBox="0 0 26 28">
          <path d="M26 10.109c0 .281-.203.547-.406.75l-5.672 5.531 1.344 7.812c.016.109.016.203.016.313 0 .406-.187.781-.641.781a1.27 1.27 0 0 1-.625-.187L13 21.422l-7.016 3.687c-.203.109-.406.187-.625.187-.453 0-.656-.375-.656-.781 0-.109.016-.203.031-.313l1.344-7.812L.39 10.859c-.187-.203-.391-.469-.391-.75 0-.469.484-.656.875-.719l7.844-1.141 3.516-7.109c.141-.297.406-.641.766-.641s.625.344.766.641l3.516 7.109 7.844 1.141c.375.063.875.25.875.719z"/>
        </symbol>
      </svg>
      <h3>---------------------------------</h3> -->
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
    <ReviewListItem
    v-for="(review, idx) in review_list"
    :key="`review_${idx}`"
    :review="review"
    />
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