<template>
  <div>
    <h3>ActorList</h3>
    <div>
      <ActorListItem
        v-for="actor in actors"
        :key="actor.id"
        :actor="actor"
      />
    </div>
  </div>
</template>

<script>
import ActorListItem from '@/components/ActorListItem.vue'

export default {
  name: 'ActorList',
  props: {
    actors: Array,
  },
  components: {
    ActorListItem
  }
}
</script>

<style>

</style>