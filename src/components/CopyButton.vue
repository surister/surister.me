<template>
  <o-tooltip v-bind:class="{ 'is-hidden': ishidden }"
             variant="primary clip-board-button"
             position="right"
             :active="isClicked" always>
    <template v-slot:content>
      Copied!
    </template>
    <o-button
        @click="clickEvent"
        :style="copyButtonStyle"
        icon-pack="fa"
        :icon-left="icon">
    </o-button>
  </o-tooltip>
</template>

<script>
export default {
  name: "CopyButton",
  props: ['ishidden'],
  data: function () {
    return {
      isClicked: false,
    }
  },
  mounted() {

  },
  computed: {
    icon: function () {
      // This stuff does not work
      if (this.isClicked){
        return 'times-circle'
      }
      return 'copy'
    },
    copyButtonStyle: function () {
      if (this.isClicked) {
        return {
          color: '#48c774',
          backgroundColor: '#2b2b2b',
          border: '1px solid #48c774',

        }
      }
      return {
        color: 'gray',
        backgroundColor: '#2b2b2b',
        border: '1px solid gray'
      }
    }
  },
  methods: {
    copyTextToClipboard(text) {
      console.log('Copying')
      console.log(text)
      if (!navigator.clipboard){
        return
      }
      navigator.clipboard.writeText('asdf').then(function () {
        /* clipboard successfully set */
      }, function () {
        /* clipboard write failed */
      });

    },
    clickEvent() {
      if (!this.isClicked) {
        this.toggleIsClicked()
        this.copyTextToClipboard("Test")
        setTimeout(() => {
          this.toggleIsClicked()
        }, 1200)
      }

    },
    toggleIsClicked() {
      this.isClicked = !this.isClicked
    }
  }
}
</script>

<style scoped>
.clip-board-button {
  position: absolute !important;
  right: 10px;
  top: 10px;
  animation: fade-out 200ms both !important;
  transition: .3s cubic-bezier(0.3, 0, 0.5, 1);
  transition-property: all;
}
</style>