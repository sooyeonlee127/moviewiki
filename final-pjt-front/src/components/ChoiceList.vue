<template>
  <div>
    <div>
      <hr>
      {{ question[0] }}
      <b-button variant="outline-success">{{ question[1][0] }}</b-button>
      <b-button variant="outline-success">{{ question[1][1] }}</b-button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ChoiceList',
  props: {
    question: Object
  }
}
</script>

<style>

</style>