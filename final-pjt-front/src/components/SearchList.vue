<template>
  <div>
    <h1>삭제할 페이지</h1>
    <b-pagination
      v-model="currentPage"
      :total-rows="rows"
      :per-page="perPage"
      aria-controls="itemList"
      align="center"
    ></b-pagination>
    <ul id="itemList">
      <li v-for="item in itemsForList" :key="item.id">
        <h1>{{item.header}}</h1>
        <span>{{item.text}}</span>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'SearchList',
  props: {
    SearchMovie: Object,
  },
  data() {
    return {
      currentPage: 1,
      perPage: 3,
    }
  },
  computed: {
    rows() {
      return this.searchmovie.length
    }
},
  methods: {
    itemsForList() {
      return this.searchmovie.slice(
        (this.currentPage - 1) * this.perPage,
        this.currentPage * this.perPage,
    );
  }
}}
</script>

<style>

</style>