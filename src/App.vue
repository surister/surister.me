<template>

  <div>
    <navbar :is_navbar_sticky="isNavbarSticky"></navbar>
    <div class="has-background-secondary pt-8">
      <div class="container is-fluid-mobile pb-6">
        <router-view></router-view>
      </div>
      <sfooter></sfooter>
    </div>
  </div>

</template>
<script>
import Navbar from "@/components/Navbar";
import Sfooter from "@/components/SFooter";


export default {
  components: {Sfooter, Navbar},
  data: function () {
    return {
      isNavbarSticky: true
    }
  },

  // created() {
  //   window.addEventListener('scroll', this.handleScroll);
  // },
  // destroyed() {
  //   window.removeEventListener('scroll', this.handleScroll);
  // },
  // methods: {
  //   handleScroll() {
  //     this.scrollPosition = window.scrollY
  //     this.is_sticky = this.scrollPosition >= this.$refs["hero-body"].clientHeight + this.$refs["hero-head"].clientHeight;
  //   }
  // },
}
</script>

<style>
.pt-8 {padding-top: 8rem}
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');
body {
  font-family: 'Roboto', "Segoe UI", serif;
}
</style>
