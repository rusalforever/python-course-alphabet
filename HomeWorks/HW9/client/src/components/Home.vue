<template>
<div class="container">
  <div class="row col-md-12">
      <hr>
      <p>
        <img width="100px" src="@/assets/logo.png">
        <span>Single Page App with Flask and Vue.js</span>
        <img  width="100px" src="@/assets/flask-logo.png">
      </p>
      <hr>
    </div>
  <div class="row col-md-12">
    <Vegetables></Vegetables>
    <Fruits></Fruits>
  </div>
</div>
</template>

<script>
  import Vegetables from './Vegetables';
  import Fruits from './Fruits';

  export default {
    name: 'Home',
    components: {
      Vegetables,
      Fruits
    },
  };
</script>
