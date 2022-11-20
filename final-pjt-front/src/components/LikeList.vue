<template>
  <div>
    <p>내가 찜한 영화 & 콘텐츠</p>
    <LikeListItem/>
  </div>
</template>

<script>
import LikeListItem from '@/components/LikeListItem.vue'
export default {
  name: 'LikeList',
  components: {
    LikeListItem,
  }
}
</script>

<style>

</style>