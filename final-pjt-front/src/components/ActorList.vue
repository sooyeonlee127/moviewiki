<template>
  <div>
    <h3>ActorList</h3>
    <p><ActorListItem/></p>
    
  </div>
</template>

<script>
import ActorListItem from '@/components/ActorListItem.vue'

export default {
  name: 'ActorList',
  components: {
    ActorListItem
  }
}
</script>

<style>

</style>