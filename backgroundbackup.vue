<template>
  <div class="intro">
    <div class="original box">
    <img class="child box scale" src="https://picsum.photos/1024/480/?image=52">
  </div>
  </div>  
</template>

<script>
export default {
  name: 'DetailView'
}
</script>

<style>
  body{
      margin:0;
  }
  .intro{
      background:url('https://newevolutiondesigns.com/images/freebies/cool-wallpaper-3.jpg'),linear-gradient(233deg, #e56420, #c22525, #3d9c31, #37bbde);
      width:100%;
      height:100vh;
      background-size:cover;
      background-blend-mode: hard-light;
      animation: hue-rotate 3s linear infinite;
  }
  @keyframes hue-rotate {
  from {
    -webkit-filter: hue-rotate(0);
    -moz-filter: hue-rotate(0);
    -ms-filter: hue-rotate(0);
    filter: hue-rotate(0);
  }
  to {
    -webkit-filter: hue-rotate(360deg);
    -moz-filter: hue-rotate(360deg);
    -ms-filter: hue-rotate(360deg);
    filter: hue-rotate(360deg);
    }
  }
  /* ---------------- */
  .box {
    width: 500px;
    height: 500px;
    line-height: 500px;
    color: white;
    text-align: center;
    border-radius: 6px;
    animation-iteration-count: infinite;
  }


  /* .original {
    margin: 30px;
    border: 1px dashed #cecfd5;
    background: #eaeaed;
    float: left;
  } */
  .child {
    background: #2db34a;
    cursor: pointer;
  }
  .scale {
    transform: scale(.95);
  }
  /* Animation Effect */
  .scale:hover {
    transition: transform 1s linear;
    transform: scale(1);
  }
</style>