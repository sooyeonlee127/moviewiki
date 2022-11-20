<template>
  <div>
    <p>나의 리뷰</p>
    <ReviewListItem
      />
  </div>
</template>

<script>
import ReviewListItem from '@/components/ReviewListItem.vue'
export default {
  name: 'ReviewList',
  components: {
    ReviewListItem,
  },

}
</script>

<style>

</style>