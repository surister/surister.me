<template>

  <div>
    <navbar ref="navbar"></navbar>
    <div class="has-background-secondary">
      <div class="container">
        <router-view></router-view>
      </div>
    </div>
  </div>

</template>
<script>
import Navbar from "@/components/navbar";

export default {
  components: {Navbar},
  methods: {
    test() {
      this.$refs.navbar.$emit('Stick')
    }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');
body {
  font-family: 'Roboto', "Segoe UI", serif;
}
</style>
