<template>
  <div style="max-width: 30rem;">
    <form>
      <h3></h3>
      <div>
        <label for="rating-inline">별점 : </label>
        <b-form-rating id="rating-inline" inline value="value"></b-form-rating>
      </div>
      <b-form-textarea
        id="content-textarea-no-resize"
        placeholder="Fixed height textarea"
        rows="3"
        no-resize
      ></b-form-textarea>
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