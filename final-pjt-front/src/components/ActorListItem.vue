<template>
  <div>
    <b-avatar
    :src="`https://image.tmdb.org/t/p/original/${ actor.profile_path }`"     
      v-if="actor.adult==false"
      size="120px"
    >
    </b-avatar>
  </div>
</template>

<script>
export default {
  name: 'ActorListItem',
  props: {
    actor: Object,
  }

}
</script>

<style>

</style>