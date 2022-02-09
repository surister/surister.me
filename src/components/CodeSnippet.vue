<template>
  <div class="columns is-vcentered">
    <div class="column ">

      <span class="p-2 has-text-white has-background-editor has-top-rounded">{{ language }} {{ version }}</span>

      <div style="position: relative"
           @mouseenter="showCopyButton"
           @mouseleave="showCopyButton">
        <prism-editor class="my-editor has-background-editor"
                      v-model="code"
                      :highlight="highlighter"
                      line-numbers
                      :readonly="true"
                      data-inline="3,5">

        </prism-editor>

        <copy-button v-if="clipboard" :ishidden="isBeingHovered"></copy-button>
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

  // ['content', 'language', 'version', 'clipboard', 'highlightRange']
  props: {
    content: {
      type: String,
      required: true,
    },
    language: {
      type: String,
      required: true
    },
    version: {
      type: String,
      required: false
    },
    clipboard : {
      type: Boolean,
      required: false,
      default: false
    },
    highlightRange: {
      type: Array,
      required: false,
    }

  },
  data: function () {
    return {
      code: this.content,
      isBeingHovered: true,
      highlightLines: this.highlightRange
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

    highlight() {
      if (this.highlightRange) {
        this.highlightLineRange(this.highlightLines[0], this.highlightLines[1])
      }

    },

    highlightLineNumber(number) {
      let line = this.$el.querySelector(`.prism-editor__line-number:nth-child(${number + 1})`);
      if (!line) return;
      line.classList.add('highlight-line');
    },

  }
}
</script>
<style>
.highlight-line {
  border-left: 5px solid green !important;
  background: #42b9832a !important;
}

.has-background-editor{
  background-color: #2b2b2b;
}
.my-editor {

  font-family: Fira code, Fira Mono, Consolas, Menlo, Courier, monospace;
  font-size: 14px;
  line-height: 1.5;
  padding: 10px;
  -webkit-box-shadow: 10px 10px 5px -7px rgba(0, 0, 0, 0.58);
  -moz-box-shadow: 10px 10px 5px -7px rgba(0, 0, 0, 0.58);
  box-shadow: 10px 10px 5px -7px rgba(0, 0, 0, 0.58);
}

.my-editor pre {
  color: white;
}

/* optional class for removing the outline */
.prism-editor__textarea:focus {
  outline: none;
}

</style>
<style scoped>

.has-top-rounded {
  border-top-right-radius: 10px;
  border-top-left-radius: 10px
}


</style>