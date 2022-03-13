<template>
  <li><a class="has-text-info" :href="'#' + anchor_id">{{ title }}</a></li>
</template>

<script>
export default {
  name: "TextIndexAnchor",
  props: ['anchor_id', 'title'],

}
</script>

<style scoped>

</style>
