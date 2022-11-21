<template>
  <div>
    <div>
      <hr>
      {{ question[0] }}
      <b-button variant="outline-success">{{ question[1][0] }}</b-button>
      <b-button variant="outline-success">{{ question[1][1] }}</b-button>
      <h1>{{ question }}</h1>
      <b-button variant="outline-success"> Yes </b-button>
      <b-button variant="outline-success"> No </b-button>
    </div>
  </div>
</template>

<script>

export default {
  name: 'ChoiceList',
  props: {
    question: Object
  },
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