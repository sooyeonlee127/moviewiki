<template>
    <b-card
      overlay
      :img-src="`https://image.tmdb.org/t/p/original/${ actor.profile_path }`"        
      img-alt="Card Image"
      text-variant="white"
      style="max-width: 10rem;"
    >
    </b-card>
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