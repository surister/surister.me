<template>
  <div class="home has-background-secondary">
    <!--    <img alt="Vue logo" src="@/assets/logo.png">-->
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
    <p class="has-text-white pt-5">Look at this code component, isn't it sweet?</p><br>
    <div class="columns">
      <div class="column is-narrow">
      <code-snippet :code_snippet="code" language="Python" version="3.10" ></code-snippet>
      </div>
    </div>

<!--    <div style="height: 4000px"></div>-->
  </div>
</template>

<script>
import Wednesday from "@/components/Wednesday";
import CodeSnippet from "@/components/CodeSnippet";

export default {
  name: 'Home',
  components: {
    CodeSnippet,
    Wednesday,
  },
  data: function () {
    return {
      code: 'def accumulate(iterable, func=operator.add, *, initial=None):\n' +
          '    \'Return running totals\'\n' +
          '    # accumulate([1,2,3,4,5]) --> 1 3 6 10 15\n' +
          '    # accumulate([1,2,3,4,5], initial=100) --> 100 101 103 106 110 115\n' +
          '    # accumulate([1,2,3,4,5], operator.mul) --> 1 2 6 24 120\n' +
          '    it = iter(iterable)\n' +
          '    total = initial\n' +
          '    if initial is None:\n' +
          '        try:\n' +
          '            total = next(it)\n' +
          '        except StopIteration:\n' +
          '            return\n' +
          '    yield total\n' +
          '    for element in it:\n' +
          '        total = func(total, element)\n' +
          '        yield total',
      isHovering: false,


    }
  },
  methods: {

  },

}
</script>
<style>


</style>
