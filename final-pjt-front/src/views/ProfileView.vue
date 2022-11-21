<template>
  <div>
    <h1>profile</h1>
    <b-avatar size="72px"></b-avatar>
    <hr>
    <hr>
    <ReviewList/>
  </div>
</template>

<script>
import ReviewList from '@/components/ReviewList.vue'

export default {
  name: 'ProfileView',
  components: {
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