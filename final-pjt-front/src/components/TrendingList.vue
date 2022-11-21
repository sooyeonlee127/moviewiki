<template>
  <div>
    <div class="row row-horizon">
    <h3>trending</h3>
    <b-card-group>
      <TrendingListItem
      v-for="trend in trending"
      :key="trend.id"
      :trend="trend"
    />
    </b-card-group>
  </div>
  </div>
</template>

<script>
import TrendingListItem from '@/components/TrendingListItem.vue'

export default {
  name: 'TrendingList',
  components: {
    TrendingListItem
  },
  props: {
    trending: Array,
  }
}
</script>

<style>

</style>