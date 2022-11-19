<template>
<div>
  <h3>오늘의 화제인물을 만나보세요</h3>
  <div class="row row-horizon">
  <b-card-group>
    <ActorListItem
      v-for="actor in actors"
      :key="actor.id"
      :actor="actor"

    />
  </b-card-group>
  </div>

</div>
</template>

<script>
import ActorListItem from '@/components/ActorListItem.vue'

export default {
  name: 'ActorList',
  props: {
    actors: Object,
  },
  components: {
    ActorListItem
  }
}
</script>

<style>

</style>