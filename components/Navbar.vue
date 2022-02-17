<template>
    <div>
    <section class="hero is-primary is-small">
      <!-- Hero head: will stick at the top -->
      <div class="hero-head" ref="hero-head">
      </div>

      <!-- Hero content: will be in the middle -->
      <div class="hero-body" ref="hero-body">
        <div class="container has-text-centered">
          <div class="columns">
            <div class="column">
              <logo color="white"></logo>
            </div>
          </div>
        </div>
      </div>

      <!-- Hero footer: will stick at the bottom -->
      <div class="hero-foot" ref="hero-navbar" style="height: 0">
        <nav class="navbar has-background-primary has-bottom-shadow" v-bind:class="{ 'is-fixed-top': is_sticky }">
          <div class="container">
            <div class="navbar-brand">

              <span class="navbar-burger has-text-white" :class="{ 'is-active': isBurgerMenuActive }"
                    data-target="navbarMenuHeroA"
                    @click="isBurgerMenuActive =  !isBurgerMenuActive">
                                                <span></span>
                                                <span></span>
                                                <span></span>
              </span>
            </div>
            <div id="navbarMenuHeroB" class="navbar-menu" :class="{ 'is-active': isBurgerMenuActive }">
              <div class="navbar-start">
                <NuxtLink class="navbar-item  is-size-4 has-text-weight-medium pl-4 pr-4" to="/">
                  HOME
                </NuxtLink>
                <NuxtLink class="navbar-item is-size-4 has-text-weight-medium pl-4 pr-4"
                             to="/about">
                  ABOUT
                </NuxtLink>

                <NuxtLink class="navbar-item is-size-4 has-text-weight-medium pl-4 pr-4"
                             to="/blog">
                  READ
                </NuxtLink>
              </div>
              <div class="navbar-end">
                <a class="navbar-item has-background-primary" href="https://www.github.com/surister" target="_blank">
                  <o-icon pack="fab" icon="github" size="large"></o-icon>
                </a>
                <a class="navbar-item has-background-primary" href="http://localhost:3000/feed.xml">
                  <o-icon pack="fas" icon="rss" size="large"></o-icon>
                </a>
              </div>
            </div>
          </div>
        </nav>
      </div>
    </section>
  </div>

</template>

<script>
import Logo from "@/components/Logo";

export default {
  name: "navbar",
  components: {Logo},
  data: function () {
    return {
      is_sticky: false,
      isBurgerMenuActive: false
    }
  },
  computed: {},
  beforeMount() {
    window.addEventListener('scroll', this.handleScroll);
  },
  beforeDestroy() {
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

<style lang="scss">
.has-bottom-shadow {
  -webkit-box-shadow: 0px 10px 5px -4px rgba(0, 0, 0, 0.5);
  -moz-box-shadow: 0px 10px 5px -4px rgba(0, 0, 0, 0.5);
  box-shadow: 0px 10px 5px -4px rgba(0, 0, 0, 0.5);
}

.has-border-top-rounded {
  border-top-left-radius: .25rem;
  border-top-right-radius: .25rem;
}
</style>
