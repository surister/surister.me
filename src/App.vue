<template>

  <div class="">
    <navbar></navbar>
    <router-view></router-view>
  </div>

</template>
<script>
import Navbar from "@/components/navbar";

export default {
  components: {Navbar}
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');
body {
  font-family: 'Roboto', "Segoe UI", serif;
}
</style>