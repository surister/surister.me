<template>
  <div class="mt-5">
    <span class="anchor" :id="anchor_id" v-if="anchor_id"></span>
    <p class="has-text-white">
      <slot name="cont"></slot>
    </p>
  </div>
</template>

<script>
export default {
  name: "TextBlock",
  props: ['anchor_id']
}
</script>

<style scoped>

</style>
