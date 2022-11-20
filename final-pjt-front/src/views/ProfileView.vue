<template>
  <div>
    <h1>profile</h1>
    <b-avatar size="72px"></b-avatar>
    <hr>
    <LikeList/>
    <hr>
    <ReviewList/>
  </div>
</template>

<script>
import LikeList from '@/components/LikeList.vue' 
import ReviewList from '@/components/ReviewList.vue'

export default {
  name: 'ProfileView',
  components: {
    LikeList,
    ReviewList
  },
  created() {
    this.getReviews()
  },
  methods: {
    getReviews() {
      this.$store.dispatch('getReviews')
    }
  }

}
</script>

<style>

</style>