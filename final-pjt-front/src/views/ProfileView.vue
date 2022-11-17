<template>
  <div>
    <h1>profile</h1>
    <LikeList/>
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
  }
}
</script>

<style>

</style>