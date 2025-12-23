<template>
  <div class="px-4 sm:px-6 lg:px-10 py-10 md:py-14">
    <!-- Hero -->
    <section id="top" class="max-w-6xl mx-auto">
      <div class="text-center mb-10">
        <h1 class="text-5xl md:text-7xl font-black mb-4">
          <span class="block bg-gradient-to-r from-cyan-400 via-purple-400 via-pink-400 to-orange-400 bg-clip-text text-transparent bg-gradient-animated">
            Career Transformation
          </span>
        </h1>
        <p class="text-lg md:text-xl text-white/90 max-w-3xl mx-auto leading-relaxed drop-shadow-lg">
          From operating machines on the factory floor to building digital solutions. This is my journey from machine operator to software developer.
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
                  <h3 class="text-xl font-extrabold text-white">Machine Operator</h3>
                  <p class="text-orange-200">Years working with industrial machinery</p>
                </div>
              </div>
            </div>

            <div class="space-y-4 relative">
              <div class="flex items-center gap-4">
                <div class="w-14 h-14 bg-gradient-to-br from-cyan-500 via-blue-500 to-purple-500 rounded-xl flex items-center justify-center shadow-lg shadow-cyan-500/50">
                  <UIcon name="i-heroicons-computer-desktop" class="w-7 h-7 text-white" />
                </div>
                <div>
                  <h3 class="text-xl font-extrabold text-white">Software Developer</h3>
                  <p class="text-cyan-200">Building the future with code</p>
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
          Discover My Journey
          <UIcon name="i-heroicons-arrow-down" class="ml-2 w-5 h-5" />
        </button>
      </div>
    </section>

    <!-- Journey -->
    <section id="journey" class="max-w-6xl mx-auto mt-16 md:mt-20">
      <h2 class="text-4xl md:text-5xl font-black mb-10 text-center">
        <span class="bg-gradient-to-r from-purple-400 to-cyan-400 bg-clip-text text-transparent">
          The Journey
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
          Skills & Technologies
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
          Examples
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
          Other Blog Topics
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
    title: 'The Starting Point',
    description:
      'I began my career as a machine operator, working in manufacturing and production. Handling industrial machinery, ensuring quality control, and maintaining precision in every task taught me the value of discipline, attention to detail, and systematic thinking.',
    tags: ['Manufacturing', 'Production', 'Quality Control']
  },
  {
    title: 'The Spark',
    description:
      'The realization that I wanted to create, build, and solve problems in a different way. I discovered my passion for technology and coding, starting with self-learning, online courses, and eventually enrolling in a coding bootcamp.',
    tags: ['Self-Learning', 'Online Courses', 'Coding Bootcamp']
  },
  {
    title: 'Learning to Code',
    description:
      'I focused on Python, databases, and backend frameworks like Django and Flask, plus Odoo ERP. Each project became a stepping stone toward my new career path.',
    tags: ['Python', 'Django', 'Flask', 'Odoo ERP']
  },
  {
    title: 'Building the Future',
    description:
      "Today I’m focused on Backend with Python (Django/Flask) and solutions with Odoo ERP. This blog is where I document my journey, projects, and lessons learned.",
    tags: ['Backend', 'Python', 'Django', 'Odoo ERP']
  }
]

// Old list kept for reference
const technologiesOld = [
  {
    name: 'JavaScript',
    icon: '<svg viewBox="0 0 24 24" fill="#F7DF1E"><path d="M0 0h24v24H0V0zm22.034 18.276c-.175-1.095-.888-2.015-3.003-2.873-.736-.345-1.554-.585-1.797-1.14-.091-.33-.105-.51-.046-.705.15-.646.915-.84 1.515-.66.39.12.75.42.976.9 1.034-.676 1.034-.676 1.755-1.125-.27-.42-.404-.601-.586-.78-.63-.705-1.469-1.065-2.834-1.034l-.705.089c-.676.165-1.32.525-1.71 1.005-1.14 1.291-.811 3.541.569 4.471 1.365 1.02 3.361 1.244 3.616 2.205.24 1.17-.87 1.545-1.966 1.41-.811-.18-1.26-.586-1.755-1.336l-1.83 1.051c.21.48.45.689.81 1.109 1.74 1.756 6.09 1.666 7.001-1.004.029-.09.24-.705.074-1.65l.046.067zm-8.983-7.245h-2.248c0 1.938-.009 3.864-.009 5.805 0 1.232.063 2.363-.138 2.711-.33.689-1.18.601-1.566.48-.396-.196-.597-.466-.83-.855-.063-.105-.11-.196-.127-.196l-1.825 1.125c.305.63.75 1.172 1.324 1.517.855.51 2.004.675 3.207.405.783-.226 1.458-.691 1.811-1.411.51-.93.402-2.07.397-3.346.012-2.054 0-4.109 0-6.179l.004-.056z"/></svg>',
    gradient: 'from-yellow-500/50 to-orange-500/50'
  },
  {
    name: 'React',
    icon: '<svg viewBox="0 0 24 24" fill="#61DAFB"><path d="M14.23 12.004a2.236 2.236 0 0 1-2.235 2.236 2.236 2.236 0 0 1-2.236-2.236 2.236 2.236 0 0 1 2.235-2.236 2.236 2.236 0 0 1 2.236 2.236zm2.648-10.69c-1.346 0-3.107.96-4.888 2.622-1.78-1.653-3.542-2.602-4.887-2.602-.41 0-.783.093-1.106.278-2.375 1.368-3.853 7.277-3.853 12.834 0 5.555 1.478 11.465 3.853 12.833.323.185.696.277 1.106.277 1.345 0 3.107-.96 4.888-2.624 1.78 1.654 3.542 2.603 4.887 2.603.41 0 .783-.094 1.106-.278 2.375-1.366 3.853-7.277 3.853-12.833 0-5.557-1.478-11.467-3.853-12.835-.323-.184-.696-.277-1.106-.277zm-.14 1.735c.142 0 .254.037.328.11.638.582 2.046 4.32 2.683 9.51.056.468.093.934.11 1.39-2.277-1.368-4.36-3.48-5.745-5.956 1.384-2.48 3.467-4.59 5.744-5.956-.017.44-.054.9-.11 1.354-.637 5.19-2.045 8.928-2.683 9.51-.074.074-.186.111-.328.111-.143 0-.255-.037-.33-.112-.637-.58-2.044-4.317-2.68-9.508-.058-.468-.096-.933-.113-1.388 2.278 1.37 4.362 3.482 5.746 5.96-1.383 2.478-3.467 4.588-5.744 5.957.016-.44.053-.898.11-1.36.637-5.19 2.043-8.926 2.68-9.508.075-.074.188-.111.33-.111z"/></svg>',
    gradient: 'from-cyan-500/50 to-blue-500/50'
  },
  {
    name: 'Vue.js',
    icon: '<svg viewBox="0 0 24 24" fill="#4FC08D"><path d="M24 1.61h-9.94L12 5.16 9.94 1.61H0l12 20.78L24 1.61zM12 14.08L5.16 2.23h4.43L12 6.41l2.41-4.18h4.43L12 14.08z"/></svg>',
    gradient: 'from-green-500/50 to-emerald-500/50'
  },
  {
    name: 'Nuxt.js',
    icon: '<svg viewBox="0 0 24 24" fill="#00DC82"><path d="M13.705 0l-1.952 3.382L9.613 6.705l-2.14 3.707 4.267 7.394 4.268-7.394-2.14-3.707L13.705 0zM9.94 10.94l1.765 3.056-3.53 6.117-7.06.001L9.94 10.94zm8.12 0l5.884 10.177-7.06-.001-3.53-6.116 1.765-3.056z"/></svg>',
    gradient: 'from-emerald-500/50 to-green-500/50'
  },
  {
    name: 'HTML',
    icon: '<svg viewBox="0 0 24 24" fill="#E34F26"><path d="M1.5 0h21l-1.91 21.563L11.977 24l-8.564-2.438L1.5 0zm17.09 4.413L5.41 4.41l.213 2.622h10.125l-.255 2.716h-6.64l.24 2.573h6.182l-.366 3.523-2.91.804-2.955-.81-.188-2.11h-2.61l.29 3.855L12 19.288l5.373-1.53L18.59 4.414z"/></svg>',
    gradient: 'from-orange-500/50 to-red-500/50'
  },
  {
    name: 'CSS',
    icon: '<svg viewBox="0 0 24 24" fill="#1572B6"><path d="M1.5 0h21l-1.91 21.563L11.977 24l-8.565-2.438L1.5 0zm17.09 4.413L5.41 4.41l.213 2.622h10.125l-.255 2.716h-6.64l.24 2.573h6.182l-.366 3.523-2.91.804-2.955-.81-.188-2.11h-2.61l.29 3.855L12 19.288l5.373-1.53L18.59 4.414z"/></svg>',
    gradient: 'from-blue-500/50 to-indigo-500/50'
  },
  {
    name: 'Node.js',
    icon: '<svg viewBox="0 0 24 24" fill="#339933"><path d="M11.998,24c-0.321,0-0.641-0.084-0.922-0.247l-2.936-1.737c-0.438-0.245-0.224-0.332-0.08-0.383 c0.585-0.203,0.703-0.25,1.328-0.604c0.065-0.037,0.151-0.023,0.218,0.017l2.256,1.339c0.082,0.045,0.197,0.045,0.272,0l8.795-5.076 c0.082-0.047,0.134-0.141,0.134-0.238V6.921c0-0.099-0.053-0.192-0.137-0.242l-8.791-5.072c-0.081-0.047-0.189-0.047-0.271,0 L3.075,6.68C2.99,6.729,2.936,6.825,2.936,6.921v10.15c0,0.097,0.054,0.189,0.139,0.235l2.409,1.392 c1.307,0.654,2.104-0.116,2.104-0.89V7.787c0-0.142,0.114-0.253,0.256-0.253h1.115c0.139,0,0.255,0.112,0.255,0.253v10.021 c0,1.745-0.95,2.745-2.604,2.745c-0.508,0-0.909,0-2.026-0.551L2.28,18.675c-0.57-0.329-0.922-0.945-0.922-1.604V6.921 c0-0.659,0.353-1.275,0.922-1.603l8.795-5.082c0.557-0.315,1.296-0.315,1.848,0l8.794,5.082c0.570,0.329,0.924,0.944,0.924,1.603 v10.15c0,0.659-0.354,1.265-0.924,1.604l-8.794,5.078C12.643,23.916,12.324,24,11.998,24z M19.099,13.993 c0-1.9-1.284-2.406-3.987-2.763c-2.731-0.361-3.009-0.548-3.009-1.187c0-0.528,0.235-1.233,2.258-1.233 c1.807,0,2.473,0.389,2.747,1.607c0.024,0.115,0.129,0.199,0.247,0.199h1.141c0.071,0,0.138-0.031,0.186-0.081 c0.048-0.054,0.074-0.123,0.067-0.196c-0.177-2.098-1.571-3.076-4.388-3.076c-2.508,0-4.004,1.058-4.004,2.833 c0,1.925,1.488,2.457,3.895,2.695c2.88,0.282,3.103,0.703,3.103,1.269c0,0.983-0.789,1.402-2.642,1.402 c-2.327,0-2.839-0.584-3.011-1.742c-0.02-0.124-0.126-0.215-0.253-0.215h-1.137c-0.141,0-0.254,0.112-0.254,0.253 c0,1.482,0.806,3.248,4.655,3.248C17.501,17.007,19.099,15.91,19.099,13.993z"/></svg>',
    gradient: 'from-green-600/50 to-green-500/50'
  },
  {
    name: 'TypeScript',
    icon: '<svg viewBox="0 0 24 24" fill="#3178C6"><path d="M1.125 0C.502 0 0 .502 0 1.125v21.75C0 23.498.502 24 1.125 24h21.75c.623 0 1.125-.502 1.125-1.125V1.125C24 .502 23.498 0 22.875 0zm17.363 9.75c.612 0 1.154.037 1.627.111a6.38 6.38 0 0 1 1.306.34v2.458a3.95 3.95 0 0 0-.643-.361 5.093 5.093 0 0 0-.717-.26 5.453 5.453 0 0 0-1.426-.2c-.3 0-.573.028-.819.086a2.1 2.1 0 0 0-.623.242c-.17.104-.3.229-.393.374a.888.888 0 0 0-.14.49c0 .196.053.373.156.529.104.156.252.304.443.444s.423.276.696.41c.273.135.582.274.926.416.47.197.892.407 1.266.628.374.222.695.473.963.753.268.279.472.598.614.957.142.359.214.776.214 1.253 0 .657-.125 1.21-.373 1.656a3.033 3.033 0 0 1-1.012 1.085 4.38 4.38 0 0 1-1.487.596c-.566.12-1.163.18-1.79.18a9.916 9.916 0 0 1-1.84-.164 5.544 5.544 0 0 1-1.512-.493v-2.63a5.033 5.033 0 0 0 3.237 1.2c.333 0 .624-.03.872-.09.249-.06.456-.144.623-.25.166-.108.29-.234.373-.38a1.023 1.023 0 0 0-.074-1.089 2.12 2.12 0 0 0-.537-.5 5.597 5.597 0 0 0-.807-.444 7.303 7.303 0 0 0-1.007-.436c-.918-.383-1.602-.852-2.053-1.405-.45-.553-.676-1.222-.676-2.005 0-.614.123-1.141.369-1.582.246-.441.58-.804 1.004-1.089a4.494 4.494 0 0 1 1.47-.629 5.782 5.782 0 0 1 1.77-.272zm-15.113.188h9.563v2.166H9.506v9.646H6.789v-9.646H3.375z"/></svg>',
    gradient: 'from-blue-600/50 to-blue-500/50'
  }
]

const skillCardGradientsOld = ['from-purple-500 to-pink-500', 'from-cyan-500 to-blue-500', 'from-orange-500 to-red-500']

const skillCardStylesOld = [
  'from-purple-500/30 to-pink-500/30 border-purple-400/40 hover:border-purple-400/70',
  'from-cyan-500/30 to-blue-500/30 border-cyan-400/40 hover:border-cyan-400/70',
  'from-orange-500/30 to-red-500/30 border-orange-400/40 hover:border-orange-400/70'
]

const skillsOld = [
  {
    name: 'Frontend Development',
    description: 'Creating beautiful, responsive user interfaces with modern frameworks',
    icon: 'i-heroicons-code-bracket'
  },
  {
    name: 'UI/UX Design',
    description: 'Designing intuitive and engaging user experiences',
    icon: 'i-heroicons-paint-brush'
  },
  {
    name: 'Backend Development',
    description: 'Building robust server-side applications and APIs',
    icon: 'i-heroicons-server'
  }
]

// Updated stack: Backend-focused (Python) + your frameworks (Django/Flask/Odoo ERP)
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
    icon: '<svg width="32" height="32" viewBox="0 0 24 24" fill="none"><path fill="#ffffff" d="M9 2h6v2h-1v3.2l3.7 6.4c.2.4.3.8.3 1.2 0 1.8-1.5 3.2-3.2 3.2H9.2C7.4 18 6 16.6 6 14.8c0-.4.1-.8.3-1.2L10 7.2V4H9V2zm3 6-3.3 5.7c-.1.2-.2.5-.2.8 0 .9.7 1.7 1.7 1.7h5.6c.9 0 1.7-.7 1.7-1.7 0-.3-.1-.5-.2-.8L12 8z"/><path fill="#ffffff" opacity="0.7" d="M10 4h4v2h-4z"/></svg>',
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

const skillCardGradients = ['from-cyan-500 to-blue-500', 'from-purple-500 to-pink-500', 'from-orange-500 to-red-500']

const skillCardStyles = [
  'from-cyan-500/30 to-blue-500/30 border-cyan-400/40 hover:border-cyan-400/70',
  'from-purple-500/30 to-pink-500/30 border-purple-400/40 hover:border-purple-400/70',
  'from-orange-500/30 to-red-500/30 border-orange-400/40 hover:border-orange-400/70'
]

const skills = [
  {
    name: 'Backend (Python)',
    description: 'Business logic and APIs with Django, Flask, and Odoo ERP.',
    icon: 'i-heroicons-server'
  },
  {
    name: 'Frontend',
    description: 'Modern, responsive UIs (this blog is built with Nuxt).',
    icon: 'i-heroicons-code-bracket'
  },
  {
    name: 'Databases & Deploy',
    description: 'PostgreSQL, Docker, and production best practices.',
    icon: 'i-heroicons-circle-stack'
  }
]

const examples = [
  {
    title: 'The Elite VA - Courses',
    description: 'Courses platform for virtual assistants (Django + Nuxt.js).',
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
    description: 'Web platform for a local gym (Django).',
    tags: ['Python', 'Django', 'Deploy'],
    url: 'https://ironhavengym-225d29547ff8.herokuapp.com',
    glow: 'bg-gradient-to-r from-orange-500/25 to-red-500/25'
  },
  {
    title: 'Memory Game (Live)',
    description: 'Card matching game (HTML/CSS/JS).',
    tags: ['JavaScript', 'HTML', 'CSS'],
    url: 'https://richard9106.github.io/remember-me-javaScript-essentials/',
    glow: 'bg-gradient-to-r from-yellow-500/25 to-orange-500/25'
  },
  {
    title: 'Summer Hackathon',
    description: 'Location guessing game (collaborative project).',
    tags: ['Django', 'Bootstrap', 'Team'],
    url: 'https://github.com/richard9106/Summer_Hackaton',
    glow: 'bg-gradient-to-r from-cyan-500/25 to-blue-500/25'
  },
  {
    title: 'PhantomForge (Live)',
    description: 'Hackathon: Halloween events + costume ideas.',
    tags: ['HTML', 'CSS', 'Bootstrap'],
    url: 'https://richard9106.github.io/PhantomForge/',
    glow: 'bg-gradient-to-r from-fuchsia-500/25 to-purple-500/25'
  }
]

const topics = [
  {
    title: 'Python Backend',
    description: 'REST APIs, business logic, testing, and best practices.',
    icon: 'i-heroicons-bolt'
  },
  {
    title: 'Django / Flask',
    description: 'Architecture, patterns, ORM, security, and performance.',
    icon: 'i-heroicons-command-line'
  },
  {
    title: 'Odoo ERP',
    description: 'Modules, customization, integrations, and support.',
    icon: 'i-heroicons-cog-6-tooth'
  },
  {
    title: 'Databases',
    description: 'Data modeling, MySQL/PostgreSQL, and optimization.',
    icon: 'i-heroicons-circle-stack'
  }
]
</script>


