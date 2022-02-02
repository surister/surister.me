<template>
  <div class="home has-background-secondary">
<!--    <img alt="Vue logo" src="@/assets/logo.png">-->
    <br>
    <div class="columns">
      <div class="column has-text-white">
        <div class="title has-text-white">Welcome to <i>Surister.me</i> - Yet Another Tech blog! <br><span
            style="text-decoration: line-through">(because there are not enough already)</span></div>
        <wednesday></wednesday>
        <div class="content has-text-white pt-6">
          <h1 class="subtitle has-text-white">5 keypoints about this blog:</h1>
          <ul class="is-size-4">
            <li>99% of the web is extremely boring, I will try to spice things up a bit.</li>
            <li>Main topics will be Software Engineering, Python, Django and whatever new tech I pick up.</li>
            <li>I will try to write about advanced topics.</li>
            <li>To the best of my ability I will be concise and to the point.</li>
          </ul>
        </div>
      </div>
    </div>
    <div style="height: 4000px"></div>
  </div>
</template>

<script>
// @ is an alias to /src

import Wednesday from "@/components/wednesday";
export default {
  name: 'Home',
  components: {
    Wednesday
  },

}
</script>
