<template>


  <footer class="footer">
    <div class="content has-text-centered">
      <div class="columns is-vcentered">
        <div class="column has-text-right-tablet">
          <p>
            <strong>Surister.me</strong> by Surister © 2022<a href="https://jgthms.com"></a>
          </p></div>
        <div class="column has-text-left-tablet">
          <follow-github-button></follow-github-button>
        </div>
      </div>
      <hr>
      <section class="has-text-centered">
        <p class="subtitle has-text-weight-medium">
          Handcrafted with:
        </p>
        <div class="columns is-centered is-vcentered">
          <div class="column is-narrow">
            <a href="https://bulma.io" target="_blank">
              <img alt="Bulma css logo" style="margin-left: 10px" height="64" width="256"
                   src="https://bulma.io/images/bulma-logo.png">
            </a>
          </div>
          <div class="column is-narrow">
            <a href="https://vuejs.org" target="_blank">
              <vue-logo></vue-logo>
            </a>
          </div>
        </div>
        <p class="subtitle has-text-weight-medium">
          Tied together with:
        </p>
        <div class="columns has-text-centered is-centered is-vcentered">
          <div class="column is-paddingless is-narrow">
            <a href="https://oruga.io" target="_blank">
              <p class="image is-128x128" style="margin: 0 auto">
                <img alt="Oruga Logo" src="@/assets/images/orugalogo.png">
                <span class="title has-text-weight-bold"> Oruga</span>

              </p></a>

          </div>


        </div>
      </section>
    </div>
  </footer>
</template>

<script>

import FollowGithubButton from "@/components/FollowGithubButton";
import VueLogo from "@/components/logos/VueLogo";

export default {
  name: "sfooter",
  components: {VueLogo, FollowGithubButton},

}
</script>

<style scoped>

</style>