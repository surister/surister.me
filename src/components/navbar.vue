<template>
  <section class="hero is-primary is-small">
    <!-- Hero head: will stick at the top -->
    <div class="hero-head" ref="hero-head">
    </div>

    <!-- Hero content: will be in the middle -->
    <div class="hero-body" ref="hero-body">
      <div class="container has-text-centered">
        <div class="columns">
          <div class="column is-narrow">asdf</div>
          <div class="column is-two-thirds">
            <h1 class="title">Surister.me</h1>
            <h2 class="subtitle">"Yet another TechBlog"</h2>
          </div>
          <div class="column">
          </div>
        </div>

      </div>
    </div>

    <!-- Hero footer: will stick at the bottom -->
    <div class="hero-foot">
      <nav class="navbar has-background-primary" v-bind:class="{ 'is-fixed-top': is_sticky }">
        <div class="container">
          <!--        <div class="navbar-brand">-->
          <!--          <a class="navbar-item">-->
          <!--            <img src="https://bulma.io/images/bulma-type-white.png" alt="Logo">-->
          <!--          </a>-->
          <!--          <span class="navbar-burger" data-target="navbarMenuHeroA">-->
          <!--            <span></span>-->
          <!--            <span></span>-->
          <!--            <span></span>-->
          <!--          </span>-->
          <!--        </div>-->
          <div id="navbarMenuHeroB" class="navbar-menu">
            <div class="navbar-start">
              <a class="navbar-item is-active is-size-4 has-text-weight-medium pl-4 pr-4 has-border-top-rounded">
                HOME
              </a>
              <a class="navbar-item  is-size-4 has-text-weight-medium pl-4 pr-4">
                ABOUT
              </a>
              <a class="navbar-item  is-size-4 has-text-weight-medium pl-4 pr-4">
                FAQ
              </a>
              <a class="navbar-item  is-size-4 has-text-weight-medium pl-4 pr-4 ">
                SURPRISE
              </a>
            </div>
            <div class="navbar-end">
              <a class="navbar-item">
                <o-icon pack="fab" icon="github" size="large"></o-icon>
              </a>
            </div>
          </div>
        </div>
      </nav>
    </div>
  </section>
</template>

<script>
export default {
  name: "navbar",
  data: function () {
    return {
      is_sticky: false,
    }
  }, created() {
    window.addEventListener('scroll', this.handleScroll);
  },
  destroyed() {
    window.removeEventListener('scroll', this.handleScroll);
  },
  methods: {
    handleScroll() {
      this.scrollPosition = window.scrollY
      this.is_sticky = this.scrollPosition >= this.$refs["hero-body"].clientHeight + this.$refs["hero-head"].clientHeight;
    }
  },
}
</script>

<style scoped lang="scss">

.has-border-top-rounded {
  border-top-left-radius: .25rem;
  border-top-right-radius: .25rem;
}


</style>