<template>
  <div class="px-4 sm:px-6 lg:px-10 py-10 md:py-14">
    <!-- Hero -->
    <section id="top" class="max-w-6xl mx-auto">
      <div class="text-center mb-10">
        <h1 class="text-5xl md:text-7xl font-black mb-4">
          <span class="block bg-gradient-to-r from-cyan-400 via-purple-400 via-pink-400 to-orange-400 bg-clip-text text-transparent bg-gradient-animated">
            Transformación Profesional
          </span>
        </h1>
        <p class="text-lg md:text-xl text-white/90 max-w-3xl mx-auto leading-relaxed drop-shadow-lg">
          Desde operar máquinas en la fábrica hasta construir soluciones digitales. Este es mi viaje de operario de máquina a desarrollador de software.
        </p>
      </div>

      <!-- From -> To card -->
      <div class="relative mb-10">
        <div class="absolute inset-0 bg-grid-pattern opacity-30 rounded-3xl"></div>
        <div class="relative bg-gradient-to-br from-indigo-500/20 via-purple-500/20 to-pink-500/20 backdrop-blur-xl rounded-3xl p-8 md:p-12 border-2 border-cyan-400/40 shadow-2xl shadow-purple-500/20">
          <div class="grid md:grid-cols-2 gap-8">
            <div class="space-y-4 relative">
              <div class="flex items-center gap-4">
                <div class="w-14 h-14 bg-gradient-to-br from-orange-500 via-red-500 to-pink-500 rounded-xl flex items-center justify-center shadow-lg shadow-orange-500/50">
                  <UIcon name="i-heroicons-wrench-screwdriver" class="w-7 h-7 text-white" />
                </div>
                <div>
                  <h3 class="text-xl font-extrabold text-white">Operario de Máquina</h3>
                  <p class="text-orange-200">Años trabajando con maquinaria industrial</p>
                </div>
              </div>
            </div>

            <div class="space-y-4 relative">
              <div class="flex items-center gap-4">
                <div class="w-14 h-14 bg-gradient-to-br from-cyan-500 via-blue-500 to-purple-500 rounded-xl flex items-center justify-center shadow-lg shadow-cyan-500/50">
                  <UIcon name="i-heroicons-computer-desktop" class="w-7 h-7 text-white" />
                </div>
                <div>
                  <h3 class="text-xl font-extrabold text-white">Desarrollador de Software</h3>
                  <p class="text-cyan-200">Construyendo el futuro con código</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="text-center">
        <button
          @click="scrollToSection('journey')"
          class="inline-flex items-center px-8 py-4 text-base md:text-lg font-bold text-white bg-gradient-to-r from-purple-500 via-pink-500 to-orange-500 rounded-xl shadow-2xl shadow-purple-500/40 hover:shadow-purple-500/60 transform hover:scale-[1.03] transition-all duration-300"
        >
          Descubre Mi Viaje
          <UIcon name="i-heroicons-arrow-down" class="ml-2 w-5 h-5" />
        </button>
      </div>
    </section>

    <!-- Journey -->
    <section id="journey" class="max-w-6xl mx-auto mt-16 md:mt-20">
      <h2 class="text-4xl md:text-5xl font-black mb-10 text-center">
        <span class="bg-gradient-to-r from-purple-400 to-cyan-400 bg-clip-text text-transparent">
          El Viaje
        </span>
      </h2>

      <div class="space-y-10">
        <div v-for="(step, index) in journeySteps" :key="index" class="relative">
          <div class="flex flex-col md:flex-row gap-6 items-start">
            <div class="flex-shrink-0 relative">
              <div
                class="w-16 h-16 md:w-20 md:h-20 bg-gradient-to-br rounded-full flex items-center justify-center text-2xl md:text-3xl font-black text-white shadow-2xl relative z-10"
                :class="stepGradients[index]"
              >
                {{ index + 1 }}
              </div>
              <div class="absolute -inset-2 bg-gradient-to-br rounded-full opacity-50 blur-xl" :class="stepGradients[index]"></div>
            </div>

            <div
              class="flex-1 bg-gradient-to-br from-indigo-500/30 via-purple-500/30 to-pink-500/30 backdrop-blur-xl rounded-2xl p-6 md:p-8 border-2 transition-all duration-300 transform hover:scale-[1.01]"
              :class="stepBorders[index]"
            >
              <h3 class="text-2xl md:text-3xl font-extrabold text-white mb-3 drop-shadow-lg">{{ step.title }}</h3>
              <p class="text-base md:text-lg text-white/90 leading-relaxed">{{ step.description }}</p>

              <div class="mt-4 flex flex-wrap gap-2">
                <span
                  v-for="(tag, tagIndex) in step.tags"
                  :key="tagIndex"
                  class="px-4 py-2 rounded-full text-sm font-semibold bg-white/20 backdrop-blur-sm border border-white/30 text-white hover:bg-white/30 transition-colors"
                >
                  {{ tag }}
                </span>
              </div>
            </div>
          </div>

          <div
            v-if="index < journeySteps.length - 1"
            class="hidden md:block absolute left-10 top-24 w-1 h-12 bg-gradient-to-b rounded-full shadow-lg"
            :class="stepGradients[index]"
          ></div>
        </div>
      </div>
    </section>

    <!-- Technologies -->
    <section id="technologies" class="max-w-6xl mx-auto mt-16 md:mt-20">
      <h2 class="text-4xl md:text-5xl font-black mb-10 text-center">
        <span class="bg-gradient-to-r from-cyan-400 via-purple-400 to-pink-400 bg-clip-text text-transparent">
          Habilidades y Tecnologías
        </span>
      </h2>

      <!-- Mobile carousel: Technologies -->
      <div class="md:hidden -mx-4 px-4 mb-10">
        <div class="flex gap-4 overflow-x-auto no-scrollbar snap-x snap-mandatory pb-4">
          <div
            v-for="(tech, index) in technologies"
            :key="index"
            class="snap-center shrink-0 w-[82%] sm:w-[60%] group relative bg-gradient-to-br from-indigo-500/30 via-purple-500/30 to-pink-500/30 backdrop-blur-xl rounded-2xl p-6 border-2 border-white/20"
          >
            <div class="absolute inset-0 rounded-2xl blur-xl opacity-60" :class="tech.gradient"></div>
            <div class="relative z-10">
              <div class="w-16 h-16 mb-4 flex items-center justify-center bg-white/10 rounded-xl backdrop-blur-sm border border-white/20">
                <span class="text-3xl" v-html="tech.icon"></span>
              </div>
              <h3 class="text-lg font-bold text-white mb-1">{{ tech.name }}</h3>
              <p class="text-sm text-white/70">Swipe →</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Desktop grid: Technologies -->
      <div class="hidden md:grid md:grid-cols-2 lg:grid-cols-4 gap-6 mb-12">
        <div
          v-for="(tech, index) in technologies"
          :key="index"
          class="group relative bg-gradient-to-br from-indigo-500/30 via-purple-500/30 to-pink-500/30 backdrop-blur-xl rounded-2xl p-6 border-2 border-white/20 hover:border-cyan-400/60 transition-all duration-300 transform hover:scale-110 hover:rotate-1"
        >
          <div
            class="absolute inset-0 bg-gradient-to-br opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-2xl blur-xl"
            :class="tech.gradient"
          ></div>
          <div class="relative z-10">
            <div class="w-16 h-16 mb-4 flex items-center justify-center bg-white/10 rounded-xl backdrop-blur-sm border border-white/20 group-hover:bg-white/20 transition-all">
              <span class="text-3xl" v-html="tech.icon"></span>
            </div>
            <h3 class="text-lg font-bold text-white mb-2">{{ tech.name }}</h3>
          </div>
        </div>
      </div>

      <!-- Mobile carousel: Skills -->
      <div class="md:hidden -mx-4 px-4">
        <div class="flex gap-4 overflow-x-auto no-scrollbar snap-x snap-mandatory pb-4">
          <div
            v-for="(skill, index) in skills"
            :key="index"
            class="snap-center shrink-0 w-[86%] sm:w-[60%] relative bg-gradient-to-br backdrop-blur-xl rounded-2xl p-6 border-2"
            :class="skillCardStyles[index]"
          >
            <div class="absolute -inset-1 bg-gradient-to-br opacity-50 blur-xl rounded-2xl" :class="skillCardGradients[index]"></div>
            <div class="relative z-10">
              <div class="w-12 h-12 rounded-lg flex items-center justify-center mb-4 shadow-lg" :class="skillCardGradients[index]">
                <UIcon :name="skill.icon" class="w-6 h-6 text-white" />
              </div>
              <h3 class="text-xl font-bold text-white mb-2">{{ skill.name }}</h3>
              <p class="text-white/80">{{ skill.description }}</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Desktop grid: Skills -->
      <div class="hidden md:grid md:grid-cols-3 gap-6">
        <div
          v-for="(skill, index) in skills"
          :key="index"
          class="relative bg-gradient-to-br backdrop-blur-xl rounded-2xl p-6 border-2 transition-all duration-300 transform hover:scale-105"
          :class="skillCardStyles[index]"
        >
          <div class="absolute -inset-1 bg-gradient-to-br opacity-50 blur-xl rounded-2xl" :class="skillCardGradients[index]"></div>
          <div class="relative z-10">
            <div class="w-12 h-12 rounded-lg flex items-center justify-center mb-4 shadow-lg" :class="skillCardGradients[index]">
              <UIcon :name="skill.icon" class="w-6 h-6 text-white" />
            </div>
            <h3 class="text-xl font-bold text-white mb-2">{{ skill.name }}</h3>
            <p class="text-white/80">{{ skill.description }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Examples -->
    <section id="examples" class="max-w-6xl mx-auto mt-16 md:mt-20">
      <h2 class="text-4xl md:text-5xl font-black mb-10 text-center">
        <span class="bg-gradient-to-r from-orange-300 via-pink-400 to-cyan-300 bg-clip-text text-transparent">
          Ejemplos
        </span>
      </h2>

      <div class="grid md:grid-cols-3 gap-6">
        <a
          v-for="(ex, index) in examples"
          :key="index"
          :href="ex.url"
          target="_blank"
          rel="noopener noreferrer"
          class="group relative overflow-hidden rounded-2xl border-2 border-white/20 bg-white/5 backdrop-blur-xl p-6 hover:border-cyan-300/60 transition-all duration-300"
        >
          <div class="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-300 blur-2xl"
               :class="ex.glow"></div>
          <div class="relative z-10">
            <div class="flex items-start justify-between gap-3">
              <h3 class="text-xl font-extrabold text-white">{{ ex.title }}</h3>
              <UIcon name="i-heroicons-arrow-top-right-on-square" class="w-5 h-5 text-white/70 group-hover:text-white" />
            </div>
            <p class="mt-2 text-white/80">{{ ex.description }}</p>
            <div class="mt-4 flex flex-wrap gap-2">
              <span
                v-for="(tag, tIndex) in ex.tags"
                :key="tIndex"
                class="px-3 py-1 rounded-full text-xs font-semibold bg-white/15 border border-white/20 text-white/90"
              >
                {{ tag }}
              </span>
            </div>
          </div>
        </a>
      </div>
    </section>

    <!-- Other Topics -->
    <section id="topics" class="max-w-6xl mx-auto mt-16 md:mt-20">
      <h2 class="text-4xl md:text-5xl font-black mb-10 text-center">
        <span class="bg-gradient-to-r from-cyan-300 via-purple-300 to-pink-300 bg-clip-text text-transparent">
          Otros temas del blog
        </span>
      </h2>

      <div class="grid md:grid-cols-2 gap-6">
        <div
          v-for="(topic, index) in topics"
          :key="index"
          class="rounded-2xl border-2 border-white/15 bg-white/5 backdrop-blur-xl p-6 hover:border-white/25 transition-colors"
        >
          <div class="flex items-center gap-3">
            <div class="w-10 h-10 rounded-xl flex items-center justify-center bg-white/10 border border-white/15">
              <UIcon :name="topic.icon" class="w-5 h-5 text-white/80" />
            </div>
            <h3 class="text-xl font-extrabold text-white">{{ topic.title }}</h3>
          </div>
          <p class="mt-3 text-white/80">{{ topic.description }}</p>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
const scrollToSection = (id: string) => {
  const element = document.getElementById(id)
  element?.scrollIntoView({ behavior: 'smooth' })
}

const stepGradients = [
  'from-orange-500 to-red-500',
  'from-yellow-500 to-orange-500',
  'from-green-500 to-cyan-500',
  'from-purple-500 to-pink-500'
]

const stepBorders = [
  'border-orange-400/40 hover:border-orange-400/70',
  'border-yellow-400/40 hover:border-yellow-400/70',
  'border-cyan-400/40 hover:border-cyan-400/70',
  'border-pink-400/40 hover:border-pink-400/70'
]

const journeySteps = [
  {
    title: 'El Punto de Partida',
    description:
      'Comencé mi carrera como operario de máquina, trabajando en manufactura y producción. Manejar maquinaria industrial, asegurar control de calidad y mantener la precisión en cada tarea me enseñó el valor de la disciplina, la atención al detalle y el pensamiento sistemático.',
    tags: ['Manufactura', 'Producción', 'Control de Calidad']
  },
  {
    title: 'La Chispa',
    description:
      'La realización de que quería crear, construir y resolver problemas de una manera diferente. Descubrí mi pasión por la tecnología y la programación, comenzando con autoaprendizaje, cursos en línea y eventualmente inscribiéndome en un bootcamp de programación.',
    tags: ['Autoaprendizaje', 'Cursos Online', 'Bootcamp de Programación']
  },
  {
    title: 'Aprendiendo a Programar',
    description:
      'Me enfoqué en Python, bases de datos y frameworks de backend como Django y Flask, además de Odoo ERP. Cada proyecto se convirtió en un escalón hacia mi nueva carrera.',
    tags: ['Python', 'Django', 'Flask', 'Odoo ERP']
  },
  {
    title: 'Construyendo el Futuro',
    description:
      'Hoy mi enfoque está en Backend con Python (Django/Flask) y soluciones con Odoo ERP. Este blog es donde documento mi camino, proyectos y aprendizajes.',
    tags: ['Backend', 'Python', 'Django', 'Odoo ERP']
  }
]

const technologies = [
  {
    name: 'Python',
    icon: '<svg width="32" height="32" viewBox="0 0 24 24" fill="none"><path fill="#3776AB" d="M12.07 2c-4.5 0-4.22 1.95-4.22 1.95l.01 2.02h4.3v.61H6.16S2 6.1 2 12.04c0 5.94 3.64 5.73 3.64 5.73h2.17v-3.05s-.12-3.64 3.58-3.64h6.14s3.45.06 3.45-3.34V5.46S24 2 18.5 2h-6.43z"/><path fill="#FFD43B" d="M11.93 22c4.5 0 4.22-1.95 4.22-1.95l-.01-2.02h-4.3v-.61h6s4.16-.52 4.16-6.46c0-5.94-3.64-5.73-3.64-5.73h-2.17v3.05s.12 3.64-3.58 3.64H6.48S3 11.86 3 15.26v3.28S3 22 8.5 22h3.43z"/></svg>',
    gradient: 'from-blue-500/45 to-yellow-500/35'
  },
  {
    name: 'Django',
    icon: '<svg width="32" height="32" viewBox="0 0 24 24" fill="none"><path fill="#092E20" d="M11.99 2h3.05v20c-1.57.31-2.8.44-4.06.44-3.82 0-5.82-1.73-5.82-5.02 0-3.17 2.1-5.23 5.34-5.23.5 0 .88.04 1.49.17V2zm0 12.82c-.41-.14-.75-.2-1.22-.2-1.73 0-2.72 1.05-2.72 2.87 0 1.78.94 2.77 2.68 2.77.37 0 .69-.03 1.26-.11v-4.33z"/><path fill="#092E20" d="M18.99 8.02v9.99c0 3.45-.26 5.1-1.05 6.56-.72 1.36-1.66 2.2-3.48 3.09l-2.83-1.32c1.82-.86 2.76-1.63 3.38-2.86.65-1.27.83-2.76.83-6.68V8.02h3.15z"/></svg>',
    gradient: 'from-emerald-500/35 to-green-500/35'
  },
  {
    name: 'Flask',
    icon: '<svg width="32" height="32" viewBox="0 0 24 24" fill="none"><path fill="#ffffff" d="M9 2h6v2h-1v3.2l3.7 6.4c.2.4.3.8.3 1.2 0 1.8-1.5 3.2-3.2 3.2H9.2C7.4 18 6 16.6 6 14.8c0-.4.1-.8.3-1.2L10 7.2V4H9V2zm3 6-3.3 5.7c-.1.2-.2.5-.2.8 0 .9.7 1.7 1.7 1.7h5.6c.9 0 1.7-.7 1.7-1.7 0-.3-.1-.5-.2-.8L12 8z"/><path fill="#ffffff" opacity=\"0.7\" d="M10 4h4v2h-4z"/></svg>',
    gradient: 'from-slate-400/30 to-white/20'
  },
  {
    name: 'Odoo ERP',
    icon: '<svg width="32" height="32" viewBox="0 0 24 24" fill="none"><path fill="#714B67" d="M12 2.2c-5.41 0-9.8 4.39-9.8 9.8 0 5.41 4.39 9.8 9.8 9.8 5.41 0 9.8-4.39 9.8-9.8 0-5.41-4.39-9.8-9.8-9.8zm0 3.1a6.7 6.7 0 1 1 0 13.4 6.7 6.7 0 0 1 0-13.4z"/><path fill="#714B67" d="M12 7.2a4.8 4.8 0 1 0 0 9.6 4.8 4.8 0 0 0 0-9.6z"/></svg>',
    gradient: 'from-fuchsia-500/35 to-purple-500/35'
  },
  {
    name: 'PostgreSQL',
    icon: '<svg width="32" height="32" viewBox="0 0 24 24" fill="none"><path fill="#4169E1" d="M12 2c-3.9 0-7 2.6-7 6v8c0 2.8 2.2 5 5 5h1v-2h-1c-1.7 0-3-1.3-3-3V8c0-2.3 2.2-4 5-4s5 1.7 5 4v8c0 1.7-1.3 3-3 3h-1v2h1c2.8 0 5-2.2 5-5V8c0-3.4-3.1-6-7-6z"/><path fill="#4169E1" d="M9 9h6v2H9zM9 13h6v2H9z"/></svg>',
    gradient: 'from-blue-500/35 to-indigo-500/35'
  },
  {
    name: 'Docker',
    icon: '<svg width="32" height="32" viewBox="0 0 24 24" fill="none"><path fill="#2496ED" d="M10 6h2v2h-2V6zm-3 0h2v2H7V6zm6 0h2v2h-2V6zM4 9h2v2H4V9zm3 0h2v2H7V9zm3 0h2v2h-2V9zm3 0h2v2h-2V9zm3 0h2v2h-2V9z"/><path fill="#2496ED" d="M22 11.5c-.6-.4-1.5-.4-2.2 0-.2-.8-.8-1.5-1.6-1.8-.6 1 .1 2.3 1 2.8-1.1 2.9-3.9 4.7-7.2 4.7H7.3c-2.5 0-4.3-1.7-4.7-3.9H2V11h1.8c.2 1.3.8 2.5 1.7 3.4 1.2 1.2 2.8 1.9 4.5 1.9H12c3 0 5.5-1.6 6.4-4 .7.3 1.6.2 2.2-.3.6-.5.6-1.1.4-1.5z"/></svg>',
    gradient: 'from-sky-500/35 to-cyan-500/30'
  },
  {
    name: 'Git',
    icon: '<svg width="32" height="32" viewBox="0 0 24 24" fill="none"><path fill="#F05032" d="M12 2.5 4.5 10a1.5 1.5 0 0 0 0 2.1l7.4 7.4a1.5 1.5 0 0 0 2.1 0l7.5-7.5a1.5 1.5 0 0 0 0-2.1L14.1 2.5a1.5 1.5 0 0 0-2.1 0z"/><path fill="#fff" d="M12 6.3a1.6 1.6 0 0 0-1.6 1.6c0 .5.2 1 .6 1.3v3.6a1.6 1.6 0 1 0 2 0V9.7c.4-.3.6-.8.6-1.3A1.6 1.6 0 0 0 12 6.3z"/><path fill="#fff" d="M16 10.4a1.6 1.6 0 0 0-1.6 1.6c0 .5.2 1 .6 1.3v1a1.6 1.6 0 1 0 2 0v-1c.4-.3.6-.8.6-1.3A1.6 1.6 0 0 0 16 10.4z"/></svg>',
    gradient: 'from-orange-500/35 to-red-500/35'
  },
  {
    name: 'Nuxt.js',
    icon: '<svg width="32" height="32" viewBox="0 0 24 24" fill="#00DC82"><path d="M13.705 0l-1.952 3.382L9.613 6.705l-2.14 3.707 4.267 7.394 4.268-7.394-2.14-3.707L13.705 0zM9.94 10.94l1.765 3.056-3.53 6.117-7.06.001L9.94 10.94zm8.12 0l5.884 10.177-7.06-.001-3.53-6.116 1.765-3.056z"/></svg>',
    gradient: 'from-emerald-500/35 to-green-500/35'
  }
]

// Re-ordered so Backend (Python) is first and visually strongest
const skillCardGradients = ['from-cyan-500 to-blue-500', 'from-purple-500 to-pink-500', 'from-orange-500 to-red-500']

const skillCardStyles = [
  'from-cyan-500/30 to-blue-500/30 border-cyan-400/40 hover:border-cyan-400/70',
  'from-purple-500/30 to-pink-500/30 border-purple-400/40 hover:border-purple-400/70',
  'from-orange-500/30 to-red-500/30 border-orange-400/40 hover:border-orange-400/70'
]

const skills = [
  {
    name: 'Backend (Python)',
    description: 'APIs y lógica de negocio con Django, Flask y Odoo ERP.',
    icon: 'i-heroicons-server'
  },
  {
    name: 'Frontend',
    description: 'Interfaces modernas y responsive (este blog está hecho con Nuxt).',
    icon: 'i-heroicons-code-bracket'
  },
  {
    name: 'Bases de datos & Deploy',
    description: 'PostgreSQL, Docker y buenas prácticas para producción.',
    icon: 'i-heroicons-circle-stack'
  }
]

const examples = [
  {
    title: 'The Elite VA - Courses',
    description: 'Plataforma de cursos para asistentes virtuales (Django + Nuxt.js).',
    tags: ['Python', 'Django', 'Nuxt.js'],
    url: 'https://the-eliteva-course.com/',
    glow: 'bg-gradient-to-r from-emerald-500/25 to-cyan-500/25'
  },
  {
    title: 'The Elite VA',
    description: 'Website + blog (Nuxt.js).',
    tags: ['Nuxt.js', 'Frontend'],
    url: 'https://the-eliteva.com/',
    glow: 'bg-gradient-to-r from-purple-500/25 to-pink-500/25'
  },
  {
    title: 'Iron Gym',
    description: 'Plataforma web para gimnasio local (Django).',
    tags: ['Python', 'Django', 'Deploy'],
    url: 'https://ironhavengym-225d29547ff8.herokuapp.com',
    glow: 'bg-gradient-to-r from-orange-500/25 to-red-500/25'
  },
  {
    title: 'Memory Game (Live)',
    description: 'Juego de cartas de memoria (HTML/CSS/JS).',
    tags: ['JavaScript', 'HTML', 'CSS'],
    url: 'https://richard9106.github.io/remember-me-javaScript-essentials/',
    glow: 'bg-gradient-to-r from-yellow-500/25 to-orange-500/25'
  },
  {
    title: 'Summer Hackathon',
    description: 'Location Guessing Game (proyecto colaborativo).',
    tags: ['Django', 'Bootstrap', 'Team'],
    url: 'https://github.com/richard9106/Summer_Hackaton',
    glow: 'bg-gradient-to-r from-cyan-500/25 to-blue-500/25'
  },
  {
    title: 'PhantomForge (Live)',
    description: 'Hackathon: eventos Halloween + ideas disfraces.',
    tags: ['HTML', 'CSS', 'Bootstrap'],
    url: 'https://richard9106.github.io/PhantomForge/',
    glow: 'bg-gradient-to-r from-fuchsia-500/25 to-purple-500/25'
  }
]

const topics = [
  {
    title: 'Backend con Python',
    description: 'APIs REST, lógica de negocio, testing y buenas prácticas.',
    icon: 'i-heroicons-bolt'
  },
  {
    title: 'Django / Flask',
    description: 'Arquitectura, patrones, ORM, seguridad y performance.',
    icon: 'i-heroicons-command-line'
  },
  {
    title: 'Odoo ERP',
    description: 'Módulos, personalización, integraciones y soporte.',
    icon: 'i-heroicons-cog-6-tooth'
  },
  {
    title: 'Bases de datos',
    description: 'Modelado, MySQL/PostgreSQL y optimización.',
    icon: 'i-heroicons-circle-stack'
  }
]
</script>
