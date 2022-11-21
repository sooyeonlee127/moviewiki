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
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  created() {
    this.getReviews()
  },
  methods: {
    getReviews() {
      if (this.isLogin) {
        this.$store.dispatch('getReviews')
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