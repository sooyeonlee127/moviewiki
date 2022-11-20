<template>
  <div>
    <ChoiceList
      v-for="question in questions"
      :key="question.id"
      :question="question"
    />
    <div class="view overlay zoom">
      <img src="https://mdbootstrap.com/img/Photos/Horizontal/Nature/6-col/img%20(131).webp" class="img-fluid " alt="smaple image">
      <div class="mask flex-center">
        <p class="white-text">Zoom effect</p>
      </div>
    </div>
    <hr>
    <p>선택 끝났을 때 출력할 영상</p>
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
  },
  computed: {
    questions() {
      return this.$store.state.questions
    }
  },
}
</script>

<style>

</style>