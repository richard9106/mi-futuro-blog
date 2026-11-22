<template>
  <div class="max-w-6xl mx-auto">
    <section id="experience" class="mt-16 md:mt-20 scroll-mt-8" aria-labelledby="experience-title">
      <div class="mb-8">
        <p class="text-sm font-bold uppercase tracking-widest text-cyan-200 mb-3">{{ copy.eyebrow }}</p>
        <h2 id="experience-title" class="text-3xl md:text-4xl font-black text-white">{{ copy.title }}</h2>
        <p class="text-white/80 mt-3 max-w-3xl leading-relaxed">{{ copy.intro }}</p>
      </div>
      <div class="grid lg:grid-cols-2 gap-6">
        <article v-for="job in copy.jobs" :key="job.company" class="rounded-2xl border border-white/20 bg-indigo-950/45 p-6 md:p-8">
          <div class="flex flex-wrap items-center justify-between gap-3 mb-4">
            <p class="text-cyan-200 font-bold">{{ job.company }}</p>
            <span class="text-xs font-semibold rounded-full px-3 py-1 bg-white/10 text-white/85">{{ job.dates }}</span>
          </div>
          <h3 class="text-xl md:text-2xl font-extrabold text-white mb-4">{{ job.role }}</h3>
          <p class="text-white/80 leading-relaxed">{{ job.summary }}</p>
          <ul class="mt-5 space-y-3 text-sm leading-relaxed text-white/80">
            <li v-for="item in job.details" :key="item" class="flex gap-3"><span aria-hidden="true" class="text-cyan-300">→</span><span>{{ item }}</span></li>
          </ul>
          <div class="flex flex-wrap gap-2 mt-6"><span v-for="tag in job.tags" :key="tag" class="text-xs text-cyan-100 rounded-full border border-cyan-300/20 bg-cyan-300/5 px-3 py-1">{{ tag }}</span></div>
        </article>
      </div>
      <a href="https://www.linkedin.com/in/richard-marles/" target="_blank" rel="noopener noreferrer" class="inline-flex mt-6 text-sm font-bold text-cyan-200 hover:text-white underline underline-offset-4">{{ copy.linkedin }} ↗</a>
    </section>

    <section id="nuviamy" class="mt-16 md:mt-20 scroll-mt-8" aria-labelledby="nuviamy-title">
      <article class="relative overflow-hidden rounded-3xl border border-purple-300/40 bg-gradient-to-br from-indigo-950/85 via-purple-950/85 to-slate-950/80 p-6 md:p-10">
        <div class="flex flex-wrap items-center gap-3 mb-5"><span class="text-xs uppercase tracking-widest font-bold text-purple-200">{{ copy.projectLabel }}</span><span class="rounded-full border border-emerald-300/30 bg-emerald-300/10 px-3 py-1 text-xs font-bold text-emerald-200">{{ copy.live }}</span></div>
        <div class="grid xl:grid-cols-[1.1fr_1fr] gap-8 items-start">
          <div>
            <h2 id="nuviamy-title" class="text-4xl md:text-5xl font-black text-white">NuviaMy</h2>
            <p class="text-lg text-purple-100 mt-3 font-semibold">{{ copy.projectTitle }}</p>
            <p class="text-white/80 leading-relaxed mt-5">{{ copy.projectIntro }}</p>
            <p class="text-white/80 leading-relaxed mt-4">{{ copy.projectRole }}</p>
            <div class="flex flex-wrap gap-2 mt-6"><span v-for="tag in projectStack" :key="tag" class="text-xs font-semibold text-white/90 rounded-full bg-white/10 border border-white/15 px-3 py-1.5">{{ tag }}</span></div>
            <div class="flex flex-wrap gap-3 mt-7">
              <a href="https://nuviamy.com/" target="_blank" rel="noopener noreferrer" class="rounded-xl px-5 py-3 bg-cyan-300 text-indigo-950 font-bold hover:bg-cyan-200 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-cyan-200">{{ copy.visit }} ↗</a>
              <a href="https://nuviamy.com/features/" target="_blank" rel="noopener noreferrer" class="rounded-xl px-5 py-3 border border-white/30 text-white font-bold hover:bg-white/10">{{ copy.features }} ↗</a>
            </div>
          </div>
          <div class="rounded-2xl bg-white/5 border border-white/15 p-5 md:p-6">
            <figure class="mb-6"><img src="/nuviamy-overview.webp" width="1265" height="712" :alt="copy.screenshotAlt" loading="lazy" class="w-full rounded-xl border border-white/15"><figcaption class="text-xs text-white/60 leading-relaxed mt-2">{{ copy.screenshotCaption }}</figcaption></figure>
            <h3 class="text-lg font-bold text-white mb-5">{{ copy.builtTitle }}</h3>
            <ul class="space-y-5"><li v-for="item in copy.built" :key="item.title"><h4 class="font-bold text-cyan-200">{{ item.title }}</h4><p class="text-sm text-white/75 leading-relaxed mt-1">{{ item.text }}</p></li></ul>
          </div>
        </div>
      </article>
    </section>
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{ language: 'es' | 'en' }>()
const projectStack = ['Python', 'Django', 'PostgreSQL', 'Docker', 'AWS', 'Stripe', 'Google Calendar', 'GitHub Actions']
const content = {
  es: {
    eyebrow: 'Experiencia profesional', title: 'Backend que conecta software y negocio.',
    intro: 'Desarrollo soluciones con Python, APIs e integraciones. Mi experiencia con Odoo me ha llevado a trabajar con procesos de negocio, bases de datos y sistemas en producción.',
    jobs: [
      { company: 'MAGAPOR', dates: 'Mayo 2026 — Actualidad', role: 'Desarrollador Senior Odoo',
        summary: 'Desarrollo, personalización, integración y mantenimiento de entornos Odoo para las distintas sedes internacionales de la empresa.',
        details: ['Módulos a medida e integraciones entre sistemas para entornos multiempresa y multipaís.', 'Automatización de procesos, optimización del rendimiento y soporte de producción.', 'Coordinación de requisitos técnicos, control de versiones, despliegues y documentación.'], tags: ['Python', 'Odoo', 'Integraciones', 'Multiempresa'] },
      { company: 'Wanapix', dates: 'Mayo 2024 — Mayo 2026', role: 'Python Backend Developer',
        summary: 'Desarrollo backend y módulos personalizados en Odoo, con Python y XML, para automatizar procesos internos.',
        details: ['Automatización de flujos de facturación y recursos humanos.', 'Integración de APIs de terceros y mejora de la interoperabilidad del ERP.', 'Optimización de PostgreSQL y colaboración con otros equipos en la entrega de funcionalidades.'], tags: ['Python', 'XML', 'APIs', 'PostgreSQL'] }
    ],
    linkedin: 'Ver mi trayectoria completa en LinkedIn', projectLabel: 'Proyecto propio · Desde 2026', live: 'En producción',
    projectTitle: 'Software de gestión para terapeutas y consultas.',
    projectIntro: 'NuviaMy reúne citas, expedientes, notas clínicas, formularios, facturación, portal del cliente y videollamadas en un mismo espacio de trabajo.',
    projectRole: 'Soy el creador y desarrollador del producto. Me encargo del diseño de la aplicación, el backend, las integraciones, el despliegue y el mantenimiento de la plataforma.',
    visit: 'Conocer NuviaMy', features: 'Explorar funcionalidades', builtTitle: 'Mi trabajo en el producto',
    screenshotAlt: 'Panel de NuviaMy con datos ficticios de demostración', screenshotCaption: 'Vista del producto con datos ficticios de demostración.',
    built: [
      { title: 'Backend y datos', text: 'Aplicación Django con PostgreSQL, separación de datos por consulta, permisos por rol y registro de actividad.' },
      { title: 'Integraciones', text: 'Suscripciones y pagos con Stripe, conexión con Google Calendar y videollamadas integradas mediante AWS.' },
      { title: 'Operación y despliegue', text: 'Contenedores Docker, alojamiento en AWS, almacenamiento privado de documentos y despliegues con GitHub Actions.' },
      { title: 'Producto y experiencia de uso', text: 'Calendario interactivo, formularios configurables, firmas electrónicas y seguimiento de cuestionarios PHQ-9 y GAD-7.' }
    ]
  },
  en: {
    eyebrow: 'Professional experience', title: 'Backend engineering grounded in business needs.',
    intro: 'I build solutions with Python, APIs and integrations. My Odoo experience has given me hands-on work with business processes, databases and production systems.',
    jobs: [
      { company: 'MAGAPOR', dates: 'May 2026 — Present', role: 'Senior Odoo Developer',
        summary: 'Development, customization, integration and maintenance of Odoo environments across the company’s international offices.',
        details: ['Custom modules and system integrations for multi-company, multi-country environments.', 'Workflow automation, performance optimization and production support.', 'Technical requirements coordination, version control, deployments and documentation.'], tags: ['Python', 'Odoo', 'Integrations', 'Multi-company'] },
      { company: 'Wanapix', dates: 'May 2024 — May 2026', role: 'Python Backend Developer',
        summary: 'Backend development and custom Odoo modules using Python and XML to automate internal business processes.',
        details: ['Automation of invoicing and HR workflows.', 'Third-party API integration and improved ERP interoperability.', 'PostgreSQL optimization and collaboration with cross-functional teams to deliver features.'], tags: ['Python', 'XML', 'APIs', 'PostgreSQL'] }
    ],
    linkedin: 'View my full experience on LinkedIn', projectLabel: 'Independent project · Since 2026', live: 'Live in production',
    projectTitle: 'Practice management software for therapists.',
    projectIntro: 'NuviaMy brings appointments, client records, clinical notes, forms, billing, a client portal and video sessions into one workspace.',
    projectRole: 'I created and develop the product, taking responsibility for application design, backend engineering, integrations, deployment and ongoing platform maintenance.',
    visit: 'Visit NuviaMy', features: 'Explore features', builtTitle: 'My work on the product',
    screenshotAlt: 'NuviaMy dashboard showing fictional demonstration data', screenshotCaption: 'Product preview with fictional demonstration data.',
    built: [
      { title: 'Backend and data', text: 'Django application with PostgreSQL, practice-scoped data, role-based permissions and activity auditing.' },
      { title: 'Integrations', text: 'Stripe subscriptions and payments, Google Calendar connectivity and embedded video sessions through AWS.' },
      { title: 'Operations and delivery', text: 'Docker containers, AWS hosting, private document storage and deployments through GitHub Actions.' },
      { title: 'Product and user experience', text: 'Interactive scheduling, configurable forms, electronic signatures and PHQ-9 and GAD-7 questionnaire tracking.' }
    ]
  }
}
const copy = computed(() => content[props.language])
</script>
