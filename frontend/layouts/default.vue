<template>
  <div>
    <navbar :is_navbar_sticky="isNavbarSticky"></navbar>
    <div class="has-background-secondary pt-6-rem">
      <div class="container p-5 pb-6">
        <Nuxt></Nuxt>
      </div>
      <sfooter></sfooter>
    </div>
  </div>

</template>
<script>
import Navbar from "@/components/Navbar";
import Sfooter from "@/components/SFooter";


export default {
  name: "default",
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
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');

.pt-6-rem {
  padding-top: 6rem
}

body {
  font-family: 'Roboto', "Segoe UI", serif;
}
</style>
