<template>
  <div>
    <p>작성자: {{ review.user }}</p>
    <p>
      <span>리뷰: {{ review.content }}</span> | 
      <span>작성일: {{ review.created_at }}</span> |
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