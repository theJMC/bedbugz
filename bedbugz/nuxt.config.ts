// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  modules: ['@nuxt/eslint', '@nuxt/devtools', '@nuxt/image', 'nuxt-umami'],
  app: {
    head: {
      title: 'BedBugZ',
      meta: [
        { name: 'description', content: 'Welcome to BedBugz! A bug-inspired dating simulator designed to teach users about the wildlife and nature around Bournemouth University campuses.' },
        { name: 'keywords', content: 'bug dating, bug dating simulator, BedBugZ, wildlife game, nature education, bug romance game, BU, uni' },
        { name: 'author', content: 'BedBugZ Team'},
        { property: 'og:title', content: 'BedBugZ | Bug Dating Simulator' },
        { property: 'og:description', content: 'Visit BedBugZ: The ultimate bug dating simulator that teaches you about wildlife and nature around Bournemouth University.' },
        { property: 'og:type', content: 'website' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1, viewport-fit=cover' }
      ]
    }
  },
  umami: {
    id: 'f5517b10-c3e1-4c81-b958-9708ea44576c',
    host: 'https://analytics.thejmc.net',
    autoTrack: true,
    // proxy: 'cloak',
    // useDirective: true,
    // ignoreLocalhost: true,
    // excludeQueryParams: false,
    // domains: ['cool-site.app', 'my-space.site'],
    // customEndpoint: '/my-custom-endpoint',
    // enabled: false,
    // logErrors: true,
  },
})