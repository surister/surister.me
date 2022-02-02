<template>
  <figure v-if="isItWednesdayMyDude" class="image" style="width: 500px">
    <img alt="it is wednesday my dudes" src="@/assets/images/wednesdaymydudeswide.jpg">
  </figure>
</template>

<script>
export default {
  name: "wednesday",
  data: function () {
    return {
      isItWednesdayMyDude: new Date().getDay() === 3
    }
  }
}
</script>

<style scoped>

</style>