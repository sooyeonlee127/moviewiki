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
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  created(){
    this.getChoice()
  },
  methods: {
    getChoice() {
      if (this.isLogin) {
        console.log("로그인 되어있음")
      } else {
        alert('로그인이 필요한 서비스입니다')
        this.$router.push({ name: 'login' })
      }
    }
  }
}
</script>

<style>

</style>