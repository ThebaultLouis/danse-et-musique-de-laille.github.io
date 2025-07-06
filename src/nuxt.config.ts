// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },

  modules: [
    '@nuxt/eslint',
    '@nuxt/icon',
    '@nuxt/image',
    '@nuxtjs/tailwindcss',
    '@pinia/nuxt'
  ],

  runtimeConfig: {
    NOTION_API_KEY: process.env.NOTION_API_KEY,
    NOTION_DANSES_DATABASE_ID: process.env.NOTION_DANSES_DATABASE_ID,
    NOTION_COURS_DATABASE_ID: process.env.NOTION_COURS_DATABASE_ID,
  }
})