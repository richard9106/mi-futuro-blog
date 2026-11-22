<template>
  <main class="min-h-screen bg-indigo-950 text-white px-6 py-20 flex flex-col justify-center items-center text-center">
    <p class="text-cyan-200 font-bold mb-4">Richard Marles</p>
    <h1 class="text-4xl font-black mb-5">{{ missing ? 'Página no encontrada · Page not found' : 'No se pudo cargar la página · Unable to load this page' }}</h1>
    <p class="text-white/75 max-w-xl leading-relaxed">{{ missing ? 'Esta dirección no existe. Puedes volver a mi perfil profesional.' : 'Inténtalo de nuevo más tarde o vuelve al inicio.' }}</p>
    <nav class="flex flex-wrap justify-center gap-4 mt-8" aria-label="Volver al perfil · Return to profile">
      <a href="/" class="rounded-xl bg-cyan-300 text-indigo-950 font-bold px-5 py-3">Perfil en español</a>
      <a href="/index-en" class="rounded-xl border border-white/30 px-5 py-3 font-bold">English profile</a>
    </nav>
  </main>
</template>
<script setup lang="ts">
const props = defineProps<{ error: { statusCode?: number } }>()
const missing = computed(() => props.error.statusCode === 404)
useSeoMeta({ title: missing.value ? 'Página no encontrada | Richard Marles' : 'Error | Richard Marles', robots: 'noindex, nofollow' })
useHead({ htmlAttrs: { lang: 'es' } })
</script>
