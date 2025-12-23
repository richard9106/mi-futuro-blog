<template>
  <div class="min-h-screen bg-gradient-to-br from-indigo-900 via-purple-900 via-pink-900 to-orange-900 relative overflow-hidden">
    <!-- Decorative Shapes -->
    <div class="absolute inset-0 overflow-hidden pointer-events-none">
      <div class="absolute top-20 left-10 w-72 h-72 bg-blue-500/20 rounded-full blur-3xl animate-pulse"></div>
      <div class="absolute top-40 right-20 w-96 h-96 bg-pink-500/20 rounded-full blur-3xl animate-pulse delay-1000"></div>
      <div class="absolute bottom-20 left-1/4 w-80 h-80 bg-cyan-500/20 rounded-full blur-3xl animate-pulse delay-2000"></div>
      <div class="absolute -top-40 -right-40 w-[500px] h-[500px] bg-yellow-500/10 rounded-full blur-3xl"></div>

      <!-- Geometric shapes -->
      <div class="absolute top-32 right-1/4 w-32 h-32 border-4 border-cyan-400/30 rotate-45"></div>
      <div class="absolute bottom-32 left-1/3 w-24 h-24 border-4 border-pink-400/30 rotate-12"></div>
      <div class="absolute top-1/2 right-10 w-16 h-16 bg-orange-400/20 rotate-45"></div>
    </div>

    <div class="relative flex flex-col md:flex-row">
      <!-- Sidebar -->
      <aside
        class="w-full md:fixed md:left-0 md:top-0 md:h-screen md:w-80 border-b md:border-b-0 md:border-r border-cyan-400/30 bg-gradient-to-b from-indigo-950/70 via-purple-950/60 to-pink-950/60 backdrop-blur-xl"
      >
        <div class="h-full p-6 flex flex-col gap-6">
          <!-- Profile -->
          <div class="flex items-center gap-4">
            <UAvatar
              src="/profile.svg"
              alt="Profile"
              size="3xl"
              class="ring-4 ring-cyan-400/40 shadow-2xl shadow-cyan-500/20"
            />
            <div class="min-w-0">
              
              <h1 class="text-xl font-black text-white truncate">Richard Marles</h1>
              <p class="text-sm text-white/70">{{ labels.role }}</p>
            </div>
          </div>

          <!-- Language -->
          <div class="rounded-2xl border border-white/15 bg-white/5 p-4">
            <p class="text-sm font-bold text-white mb-3 flex items-center gap-2">
              <UIcon name="i-heroicons-language" class="w-5 h-5 text-cyan-300" />
              {{ labels.language }}
            </p>
            <div class="flex items-center gap-2">
              <button
                @click="goSpanish"
                :class="[
                  'px-3 py-2 rounded-lg text-sm font-bold transition-all duration-300 flex-1',
                  !isEnglish
                    ? 'bg-gradient-to-r from-purple-500 to-pink-500 text-white shadow-lg shadow-purple-500/40'
                    : 'bg-white/10 text-white/70 hover:bg-white/20 hover:text-white'
                ]"
              >
                ES
              </button>
              <button
                @click="goEnglish"
                :class="[
                  'px-3 py-2 rounded-lg text-sm font-bold transition-all duration-300 flex-1',
                  isEnglish
                    ? 'bg-gradient-to-r from-purple-500 to-pink-500 text-white shadow-lg shadow-purple-500/40'
                    : 'bg-white/10 text-white/70 hover:bg-white/20 hover:text-white'
                ]"
              >
                EN
              </button>
            </div>
          </div>

          <!-- Navigation -->
          <div class="rounded-2xl border border-white/15 bg-white/5 p-4">
            <p class="text-sm font-bold text-white mb-3 flex items-center gap-2">
              <UIcon name="i-heroicons-squares-2x2" class="w-5 h-5 text-pink-300" />
              {{ labels.navigation }}
            </p>
            <nav class="grid gap-2">
              <NuxtLink
                v-for="item in navItems"
                :key="item.to"
                :to="item.to"
                class="group flex items-center gap-3 px-3 py-2 rounded-xl border border-white/10 bg-white/5 hover:bg-white/10 transition-colors"
              >
                <UIcon :name="item.icon" class="w-5 h-5 text-white/80 group-hover:text-cyan-200" />
                <span class="text-sm font-semibold text-white/80 group-hover:text-white">{{ item.label }}</span>
              </NuxtLink>
            </nav>
          </div>

          <!-- Contact / Social -->
          <div class="rounded-2xl border border-white/15 bg-white/5 p-4 overflow-hidden">
            <p class="text-sm font-bold text-white mb-3 flex items-center gap-2">
              <UIcon name="i-heroicons-identification" class="w-5 h-5 text-orange-300" />
              {{ labels.contact }}
            </p>

            <div class="grid gap-3">
              <a
                :href="profile.website"
                target="_blank"
                rel="noopener noreferrer"
                class="w-full max-w-full overflow-hidden flex items-center gap-3 px-3 py-2 rounded-xl border border-white/10 bg-white/5 hover:bg-white/10 transition-colors"
                v-if="profile.website"
              >
                <UIcon name="i-heroicons-globe-alt" class="w-5 h-5 text-purple-200" />
                <div class="min-w-0">
                  <p class="text-xs text-white/60">{{ labels.website }}</p>
                  <p class="text-sm font-semibold text-white truncate">{{ profile.websiteLabel }}</p>
                </div>
              </a>

              <a
                :href="profile.linkedin"
                target="_blank"
                rel="noopener noreferrer"
                class="w-full max-w-full overflow-hidden flex items-center gap-3 px-3 py-2 rounded-xl border border-white/10 bg-white/5 hover:bg-white/10 transition-colors"
              >
                <UIcon name="i-heroicons-briefcase" class="w-5 h-5 text-pink-200" />
                <div class="min-w-0">
                  <p class="text-xs text-white/60">{{ labels.linkedin }}</p>
                  <p class="text-sm font-semibold text-white truncate">{{ profile.linkedinLabel }}</p>
                </div>
              </a>

              <a
                :href="profile.github"
                target="_blank"
                rel="noopener noreferrer"
                class="w-full max-w-full overflow-hidden flex items-center gap-3 px-3 py-2 rounded-xl border border-white/10 bg-white/5 hover:bg-white/10 transition-colors"
              >
                <UIcon name="i-heroicons-code-bracket" class="w-5 h-5 text-orange-200" />
                <div class="min-w-0">
                  <p class="text-xs text-white/60">{{ labels.github }}</p>
                  <p class="text-sm font-semibold text-white truncate">{{ profile.githubLabel }}</p>
                </div>
              </a>
            </div>
          </div>

          <div class="mt-auto text-xs text-white/50">
            {{ labels.footer }}
          </div>
        </div>
      </aside>

      <!-- Main content -->
      <main class="flex-1 md:ml-80">
        <div class="min-h-screen">
          <slot />
        </div>
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
const route = useRoute()
const router = useRouter()

const isEnglish = computed(() => route.path.endsWith('-en'))

const labels = computed(() => {
  if (isEnglish.value) {
    return {
      profileLabel: 'PROFILE',
      role: 'Full Stack Software Development · Code Institute',
      language: 'Language',
      navigation: 'Navigation',
      contact: 'Contact',
      website: 'Website',
      linkedin: 'LinkedIn',
      github: 'GitHub',
      nav: {
        home: 'Home',
        journey: 'Journey',
        technologies: 'Technologies',
        examples: 'Examples',
        topics: 'Other Topics'
      },
      footer: 'Built with Nuxt.js & Nuxt UI • 2024'
    }
  }

  return {
    profileLabel: 'PERFIL',
    role: 'Full Stack Software Development · Code Institute',
    language: 'Idioma',
    navigation: 'Navegación',
    contact: 'Contacto',
    website: 'Página web',
    linkedin: 'LinkedIn',
    github: 'GitHub',
    nav: {
      home: 'Inicio',
      journey: 'Viaje',
      technologies: 'Tecnologías',
      examples: 'Ejemplos',
      topics: 'Otros temas'
    },
    footer: 'Construido con Nuxt.js & Nuxt UI • 2024'
  }
})

const toEnglishPath = (path: string) => {
  if (path === '/') return '/index-en'
  if (path.endsWith('-en')) return path
  return `${path}-en`
}

const toSpanishPath = (path: string) => {
  if (path === '/index-en') return '/'
  if (!path.endsWith('-en')) return path
  const without = path.replace(/-en$/, '')
  return without === '' ? '/' : without
}

const goEnglish = async () => {
  await router.push(`${toEnglishPath(route.path)}${route.hash || ''}`)
}

const goSpanish = async () => {
  await router.push(`${toSpanishPath(route.path)}${route.hash || ''}`)
}

const profile = {
  // If you want to show a website card later, set these:
  website: '',
  websiteLabel: '',
  linkedin: 'https://www.linkedin.com/in/richard-marles/',
  linkedinLabel: 'linkedin.com/in/richard-marles',
  github: 'https://github.com/richard9106',
  githubLabel: 'github.com/richard9106'
}

const navItems = computed(() => [
  { to: `${route.path}#top`, icon: 'i-heroicons-home', label: labels.value.nav.home },
  { to: `${route.path}#journey`, icon: 'i-heroicons-bolt', label: labels.value.nav.journey },
  { to: `${route.path}#technologies`, icon: 'i-heroicons-command-line', label: labels.value.nav.technologies },
  { to: `${route.path}#examples`, icon: 'i-heroicons-square-3-stack-3d', label: labels.value.nav.examples },
  { to: `${route.path}#topics`, icon: 'i-heroicons-chat-bubble-left-right', label: labels.value.nav.topics }
])
</script>


