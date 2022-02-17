<template>
  <div>
    <h1 class="title has-text-white">Latest:</h1>
    <div v-for="article of articles" :key="article.slug" class="columns ">
      <div class="column is-three-fifths">
        <NuxtLink :to="{ name: 'blog-slug', params: { slug:article.slug }}">
          <div class="card has-background-primary testhover">
            <!--          <div class="card-image">-->
            <!--            <figure class="image is-16by9">-->
            <!--              <img style="height: 100%" src="https://via.placeholder.com/420x236.png " alt="Placeholder image">-->
            <!--            </figure>-->
            <!--          </div>-->
            <div class="card-content">
              <div class="media">
                <div class="media-content">
                  <span class="title is-4 has-text-white">{{ article.title }}</span>
                  <div class="pt-2">
                    <span class="subtitle is-6 has-text-tresh">
                        <time :datetime="article.createdAt">
                          <o-icon pack="fa" icon="calendar" variant="tresh"></o-icon>
                          {{ formatDate(article.createdAt) }}
                        </time>
                    </span>
                  </div>
                </div>
              </div>
              <div class="content has-text-white">
                <p>{{ article.description }}</p><br>
                <nav class="level">
                  <div class="level-left">
                    <span class="tags">
                      <span class="tag" v-for="tag in article.tags.split(',')">{{ tag }}</span>
                    </span>
                  </div>
                  <div class="level-right">
                    <span class="pl-2 has-text-white">
                        <o-icon pack="fa" icon="book-open" variant="tresh-light"></o-icon>
                          5 minute read
                      </span>
                  </div>
                </nav>
              </div>
            </div>
          </div>
        </NuxtLink>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  async asyncData({$content, params}) {
    const articles = await $content('articles')
      .only(['title', 'description', 'slug', 'createdAt', 'tags'])
      .sortBy('createdAt', 'asc')
      .fetch()
    console.log(articles)
    return {
      articles
    }
  },
  methods: {
    formatDate(date) {
      return new Date(date).toLocaleDateString('en-CA', {year: 'numeric', month: 'numeric', day: 'numeric'})
    }
  }
}
</script>

<style scoped>
.testhover{
  transition:all .4s ease;
-webkit-transition-delay:all .4s ease;
-moz-transition-delay:all .4s ease;
-ms-transition-delay:all .4s ease;
-o-transition-delay:all .4s ease;
}

.testhover:hover {
  background-color: rgba(77, 83, 94, 0.99) !important;
}
</style>
