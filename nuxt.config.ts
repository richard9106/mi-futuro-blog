export default defineNuxtConfig({
  devtools: { enabled: false },
  modules: [
    '@nuxt/ui'
  ],
  css: ['~/assets/css/main.css'],
  nitro: {
    preset: 'cloudflare-pages'
  },
  app: {
    head: {
      title: 'Richard Marles | Backend Software Engineer',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'description', content: 'Richard Marles: Python backend developer, Senior Odoo Developer at MAGAPOR and creator of NuviaMy.' }
      ],
      link: [
        { rel: 'icon', type: 'image/svg+xml', href: '/profile.svg' }
      ]
    }
  }
})
