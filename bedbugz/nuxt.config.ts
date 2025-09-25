// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  modules: ['@nuxt/eslint', '@nuxt/devtools', '@nuxt/image'],
  app: {
    head: {
      title: 'BedBugZ',
      meta: [
        { name: 'description', content: 'Welcome to BedBugz! A bug-inspired dating simulator designed to teach users about the wildlife and nature around Bournemouth University campuses.' }
      ]
    }
  }
})