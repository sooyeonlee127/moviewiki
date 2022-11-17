<template>
  <div>
    <form>
      <h3></h3>
      <div>
        <label for="rating-inline">별점 : </label>
        <b-form-rating id="rating-inline" inline value="value"></b-form-rating>
      </div>
      <label for="content">한줄평 :</label>
      <textarea id="content" cols="30" rows="10"></textarea>
    </form>
  </div>
</template>

<script>
export default {
  name: 'ReviewCreate',
  data() {
    return {
      value: null
    }
  }
}
</script>

<style>

</style>