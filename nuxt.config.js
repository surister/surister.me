const createSitemapRoutes = async () => {
  let routes = [];
  const { $content } = require('@nuxt/content')
  if (posts === null || posts.length === 0)
    posts = await $content('blog').fetch();
  for (const post of posts) {
    routes.push(`blog/${post.slug}`);
  }
  return routes;
}


export default {
  target: 'static',
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'test',
    htmlAttrs: {
      lang: 'en'
    },
    meta: [
      {charset: 'utf-8'},
      {name: 'viewport', content: 'width=device-width, initial-scale=1'},
      {hid: 'description', name: 'description', content: ''},
      {name: 'format-detection', content: 'telephone=no'}
    ],
    link: [
      {rel: 'icon', type: 'image/x-icon', href: '/favicons/favicon.ico'},
      {rel: 'apple-touch-icon', type: 'image/x-icon', sizes: '180x180', href: '/favicons/apple-touch-icon.png'}
      // <link rel="icon" type="image/png" sizes="32x32" href="<%= BASE_URL %>favicons/favicon-32x32.png">
      // <link rel="icon" type="image/png" sizes="16x16" href="<%= BASE_URL %>favicons/favicon-16x16.png">
      // <link rel="manifest" href="<%= BASE_URL %>favicons/site.webmanifest">
      // <link rel="mask-icon" href="<%= BASE_URL %>favicons/safari-pinned-tab.svg" color="#5bbad5">
      // <meta name="msapplication-TileColor" content="#da532c">
      // <meta name="theme-color" content="#333333">
    ]
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    {src: '~/plugins/bulma-theme.js'},
    {src: '~/plugins/fontawesome.js'}
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [],


  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    // https://go.nuxtjs.dev/content
    '@nuxt/content',
    '@nuxtjs/feed',
    '@nuxtjs/sitemap'
  ],

  feed: [
    {
      path: '/feed.xml',
      async create(feed, args) {
        const baseUrlArticles = 'https://mywebsite.com/articles'
        const baseLinkFeedArticles = '/feed/articles'
        const {$content} = require('@nuxt/content')
        const articles = await $content('articles').fetch()

        articles.forEach((article) => {
          const url = `${baseUrlArticles}/${article.slug}`
          feed.addItem({
            id: article.slug,
            link: url,
            title: article.title,
            description: article.description,
            tags: article.tags,
            date: new Date(article.createdAt)
          })
        })

        feed.addContributor({
          name: 'Surister',
          email: 'contact@surister.me',
          link: 'https://surister.me'
        })

        feed.options = {
          title: "Surister's Programming Blog",
          link: 'https://surister.me/feed.xml',
          description: 'This is my personal feed!',
          language: "en",
          favicon: "https://surister.me/favicons/favicon.ico",
          copyright: "All rights reserverd 2022, Surister",
        }
      },
      cacheTime: 1000 * 60 * 15,
      type: 'rss2',
      data: ['blog', 'xml', 'title']
    },

  ],

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    // Workaround to avoid enforcing hard-coded localhost:3000: https://github.com/nuxt-community/axios-module/issues/308
    baseURL: '/'
  },

  // Content module configuration: https://go.nuxtjs.dev/config-content
  content: {},

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {},


  // Site Maps
  sitemap: {
    hostname: 'https://my-domain-name.com',
    gzip: true,
    routes: createSitemapRoutes
  },


}
