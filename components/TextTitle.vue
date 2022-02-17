<template>
<div>
  <span class="anchor" :id="anchor_id" v-if="anchor_id"></span>
  <h3 class="title has-text-white">
    <slot name="content"></slot>
    <span>
      <o-icon class="pl-5" v-if="anchor_id" icon="link" pack="fa" variant="danger"></o-icon>
    </span>
  </h3>
</div>
</template>

<script>
export default {
  name: "TextTitle",
  props: ['anchor_id']
}
</script>

<style scoped>

</style>

