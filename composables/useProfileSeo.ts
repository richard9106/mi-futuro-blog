/** Server-rendered metadata for the two published portfolio pages. */
export const useProfileSeo = (language: 'es' | 'en') => {
  const spanish = language === 'es'
  const origin = 'https://rmarles.com'
  const url = spanish ? `${origin}/` : `${origin}/index-en`
  const title = spanish
    ? 'Richard Marles | Desarrollador Python y Django en Zaragoza'
    : 'Richard Marles | Python & Django Backend Developer'
  const description = spanish
    ? 'Desarrollador backend Python y Django en Zaragoza. Senior Odoo Developer en MAGAPOR y creador de NuviaMy. APIs, PostgreSQL, Docker y AWS.'
    : 'Python and Django backend developer based in Zaragoza, Spain. Senior Odoo Developer at MAGAPOR and creator of NuviaMy. APIs, PostgreSQL, Docker and AWS.'

  useSeoMeta({
    title, description, author: 'Richard Marles',
    ogTitle: title, ogDescription: description, ogType: 'website', ogUrl: url,
    ogSiteName: 'Richard Marles', ogLocale: spanish ? 'es_ES' : 'en_US',
    ogImage: `${origin}/mia.jpeg`, ogImageAlt: 'Richard Marles',
    ogImageWidth: 800, ogImageHeight: 800, ogImageType: 'image/jpeg',
    twitterCard: 'summary', twitterTitle: title, twitterDescription: description,
    twitterImage: `${origin}/mia.jpeg`, twitterImageAlt: 'Richard Marles'
  })

  const personId = `${origin}/#richard-marles`
  const websiteId = `${origin}/#website`
  const schema = {
    '@context': 'https://schema.org',
    '@graph': [
      {
        '@type': 'Person', '@id': personId, name: 'Richard Marles',
        url: `${origin}/`, image: `${origin}/mia.jpeg`, description,
        jobTitle: ['Backend Software Engineer', 'Senior Odoo Developer'],
        worksFor: { '@type': 'Organization', name: 'MAGAPOR' },
        address: { '@type': 'PostalAddress', addressLocality: 'Zaragoza', addressRegion: 'Aragón', addressCountry: 'ES' },
        sameAs: ['https://www.linkedin.com/in/richard-marles/', 'https://github.com/richard9106'],
        knowsAbout: ['Python', 'Django', 'Odoo', 'API integration', 'PostgreSQL', 'Docker', 'AWS'],
        subjectOf: [{ '@id': `${origin}/#profile-es` }, { '@id': `${origin}/#profile-en` }]
      },
      {
        '@type': 'WebSite', '@id': websiteId, url: `${origin}/`, name: 'Richard Marles',
        inLanguage: ['es', 'en'], publisher: { '@id': personId }
      },
      {
        '@type': 'ProfilePage', '@id': `${origin}/#profile-${language}`, url, name: title,
        description, inLanguage: language, mainEntity: { '@id': personId },
        isPartOf: { '@id': websiteId },
        hasPart: [
          { '@type': 'WebPageElement', '@id': `${url}#experience`, name: spanish ? 'Experiencia profesional' : 'Professional experience' },
          { '@type': 'WebPageElement', '@id': `${url}#nuviamy`, name: 'NuviaMy' },
          { '@type': 'WebPageElement', '@id': `${url}#support`, name: spanish ? 'Apoyar NuviaMy' : 'Support NuviaMy' }
        ]
      }
    ]
  }
  useHead({
    htmlAttrs: { lang: language },
    link: [
      { rel: 'canonical', href: url },
      { rel: 'alternate', hreflang: 'es', href: `${origin}/` },
      { rel: 'alternate', hreflang: 'en', href: `${origin}/index-en` },
      { rel: 'alternate', hreflang: 'x-default', href: `${origin}/` }
    ],
    script: [{ key: 'profile-schema', type: 'application/ld+json', innerHTML: JSON.stringify(schema).replace(/</g, '\\u003c') }]
  })
}
