<template>
  <div>
    <div>
      <hr>
      <h1>{{ question }}</h1>
      <b-button variant="outline-success"> Yes </b-button>
      <b-button variant="outline-success"> No </b-button>
    </div>
  </div>
</template>

<script>

export default {
  name: 'ChoiceList',
  data() {
    return {
      filter_list: [],
      question: '',
    }
  },
  created() {
    
  },
  methods: {
    
  }
}
</script>

<style>

</style>