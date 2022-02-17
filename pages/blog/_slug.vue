<template>
  <article class="content is-large">
    <h1 class="title is-1 has-text-white">{{ article.title }}.</h1>
    <p class="subtitle is-6 pt-2">
      <span class="subtitle is-6 has-text-tresh">
        <time :datetime="article.createdAt">
          <o-icon pack="fa" icon="calendar" variant="tresh"></o-icon>
          {{ formatDate(article.createdAt) }}
        </time>
      </span>
      <span class="subtitle has-text-white pl-2">-</span>
      <span class="pl-2 has-text-white">
                        <o-icon pack="fa" icon="book-open" variant="tresh-light"></o-icon>
                          5 minute read
      </span>
      <span class="subtitle has-text-white pl-2">-</span>
      <span class="pl-2 tags is-inline">
                      <span class="tag" v-for="tag in article.tags.split(',')">{{ tag }}</span>
                    </span>
    </p>
    <nuxt-content class="pt-3" :document="article"/>
  </article>
</template>
<script>
export default {
  async asyncData({$content, params}) {
    const article = await $content('articles', params.slug).fetch()
    return {article}
  },
  methods: {
    formatDate(date) {
      return new Date(date).toLocaleDateString('en-CA', {year: 'numeric', month: 'numeric', day: 'numeric'})
    }
  }
}
</script>

<style scoped>

</style>
