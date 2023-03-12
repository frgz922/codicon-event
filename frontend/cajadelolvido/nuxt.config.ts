export default defineNuxtConfig({
    image: {
        dir: 'assets/images'
    },
    modules: [
        '@nuxtjs/tailwindcss',
        '@nuxt/image-edge',
    ],
    css: [
        '@/assets/css/main.css',
        '@/assets/css/fontface.css',
    ],
})
