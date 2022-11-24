<template>
<div>
  <h3>Top 20! 오늘의 화제인물을 만나보세요</h3>
  <div class="row row-horizon">
  <b-card-group>
    <div
      v-for="actor in actors"
      :key="actor.id"
      :actor="actor"
      >
      <img
      :src="`https://image.tmdb.org/t/p/original/${ actor.profile_path }`"     
      v-if="actor.adult==false"
      width="80px"
      @click="getActorDetail(actor.id)"
      style="margin: 10px;"
      >
    </div>
  </b-card-group>
  </div>

</div>
</template>

<script>

export default {
  name: 'ActorList',
  props: {
    actors: Array,
  },
  components: {
  },
  methods: {
    getActorDetail(actor_id) {
      console.log('배우 클릭')
      this.$router.push({name: 'actor', params: {actor_id}})
    }
  }
}
</script>

<style>

</style>