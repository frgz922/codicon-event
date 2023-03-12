<template>
  <div class="h-full">
    <header class="bg-bkg pb-4 sticky top-0 border-b-4 border-accent" id="header">
      <nav class="container mx-auto pt-4 flex justify-between items-center">
        <NuxtLink to="/" class="font-bold">
          <img src="~/assets/images/logo.png" class="w-80" />
        </NuxtLink>
        <ul class="flex gap-4">
          <li>
            <NuxtLink to="/contacto" class="font-bold  text-sm"
              :class="{ 'text-accent hover:text-white': isContact, 'hover:text-accent text-white': !isContact }">
              Contacto</NuxtLink>
          </li>
        </ul>
      </nav>
    </header>
    <div class="mx-auto min-h-[calc(100vh_-_5rem)]">
      <slot />
    </div>
    <footer class="bg-bkg py-4">
      <div class="container mx-auto flex justify-between items-center">
        <p class="text-sm text-white">
          © 2023 - Todos los derechos reservados
        </p>
        <img src="/images/logo.png" alt="logo" class="w-44">
      </div>
    </footer>
  </div>
</template>

<script lang="ts">
export default ({
  data() {
    return {
      path: '/'
    }
  },
  computed: {
    isContact() {
      return this.$route.path === '/contacto'
    }
  }
})
</script>