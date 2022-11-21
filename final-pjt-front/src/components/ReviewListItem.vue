<template>
  <div>
    <p>{{ review.user }}</p>
    <p>
      <span>{{ review.content }}</span> | 
      <span>{{ review.created_at }}</span> |
      <span>{{ review.rating }}점</span>
    </p>
    
  </div>
</template>

<script>
export default {
  name: 'ReviewListItem',
  props: {
    review: Object
  }
}
</script>

<style>

</style>