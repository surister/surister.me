<template>
  <div class="columns is-vcentered">
    <div class="column ">

      <span class="pl-2 has-text-white">{{ language }} {{ version }}</span>

      <div style="position: relative" @mouseenter="showCopyButton" @mouseleave="showCopyButton">
        <prism-editor class="my-editor"
                      v-model="code"
                      :highlight="highlighter"
                      line-numbers
                      :readonly="true"
                      data-inline="3,5"
        ></prism-editor>
        <copy-button :ishidden="isBeingHovered"></copy-button>
      </div>
    </div>
  </div>
</template>

<script>
import {highlight, languages} from 'prismjs/components/prism-core';
import 'vue-prism-editor/dist/prismeditor.min.css'; // import the styles somewhere
import 'prismjs/components/prism-python'
import '../assets/css/darcula.css'

import {PrismEditor} from 'vue-prism-editor';
import CopyButton from "@/components/CopyButton";

export default {
  name: "CodeSnippet",
  components: {
    CopyButton,
    PrismEditor
  },
  props: ['code_snippet', 'language', 'version'],
  data: function () {
    return {
      code: this.code_snippet,
      isBeingHovered: true,
      highlightLines: [3,5]
    }
  },
  mounted() {

    this.highlight();

  },
  methods: {
    highlightLineRange(start, end) {
      for (let idx = start; idx <= end; idx++) {
        let line = this.$el.querySelector(`.prism-editor__line-number:nth-child(${idx + 1})`);
        if (!line) return;
        line.classList.add('highlight-line');
      }
    },

    highlighter(code) {
      return highlight(code, languages.python);
    },
    showCopyButton() {
      this.isBeingHovered = !this.isBeingHovered
      // this.highlightLineRange(1, 10);

    },

    highlight(){
      this.highlightLineRange(this.highlightLines[0], this.highlightLines[1])
    },

    highlightLineNumber(number) {
      let line = this.$el.querySelector(`.prism-editor__line-number:nth-child(${number + 1})`);
      if (!line) return;
      line.classList.add('highlight-line');
    },

  }
}
</script>

<style >
.highlight-line {
  border-left: 5px solid green !important;
  background: #42b9832a !important;
}

</style>