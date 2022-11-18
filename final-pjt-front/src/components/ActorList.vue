<template>
<div>
  <div class="row row-horizon">
  <h3>movie</h3>
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