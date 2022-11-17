<template>
  <div>
    <ChoiceList/>
    <hr>
    <h3>선택 끝났을 때 출력할 영상</h3>
    <TrailerPlay/>
  </div>
</template>

<script>
import TrailerPlay from '@/components/TrailerPlay.vue'
import ChoiceList from '@/components/ChoiceList.vue'
export default {
  name: 'ChoiceView',
  components: {
    TrailerPlay,
    ChoiceList
  }
}
</script>

<style>

</style>