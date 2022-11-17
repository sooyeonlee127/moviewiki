<template>
  <div>
    <h1>DetailView</h1>
    <ReviewCreate/>
    <hr>


  </div>
</template>

<script>
import ReviewCreate from '@/components/ReviewCreate.vue'


export default {
  name: 'DetailView',
  components: {
    ReviewCreate,
  }
}
</script>

<style>

</style>