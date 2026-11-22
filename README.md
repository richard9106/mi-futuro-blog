# Mi Futuro - Career Transformation Blog

A bold and technological blog built with Nuxt.js and Nuxt UI, documenting the journey from machine operator to software developer.

## Features

- 🎨 **Bold & Modern Design**: Gradient backgrounds, glassmorphism effects, and smooth animations
- 🌍 **Bilingual Support**: Full English and Spanish translations
- 📱 **Responsive**: Works perfectly on all devices
- ⚡ **Fast & Optimized**: Built with Nuxt.js for optimal performance
- 🎯 **Nuxt UI**: Beautiful components out of the box

## Tech Stack

- [Nuxt.js](https://nuxt.com/) - The Intuitive Vue Framework
- [Nuxt UI](https://ui.nuxt.com/) - UI Library for Nuxt
- [@nuxtjs/i18n](https://i18n.nuxtjs.org/) - Internationalization module
- [Tailwind CSS](https://tailwindcss.com/) - Utility-first CSS framework (via Nuxt UI)

## Getting Started

### Installation

```bash
npm install
```

### Development

```bash
npm run dev
```

Visit `http://localhost:3000` to see your blog.

### Build

```bash
npm run build
```

### Preview Production Build

```bash
npm run preview
```

## Project Structure

```
.
├── assets/
│   └── css/
│       └── main.css          # Global styles
├── locales/
│   ├── en.json               # English translations
│   └── es.json               # Spanish translations
├── pages/
│   └── index.vue             # Main blog page
├── app.vue                   # Root component
├── nuxt.config.ts            # Nuxt configuration
└── package.json              # Dependencies
```

## Language Switching

The blog supports both English and Spanish. Users can switch languages using the buttons in the navigation bar. The language preference is saved in cookies.

## Customization

- Edit translations in `locales/en.json` and `locales/es.json`
- Modify the design in `pages/index.vue`
- Update styles in `assets/css/main.css`
- Configure Nuxt in `nuxt.config.ts`

## License

MIT

## Professional profile and NuviaMy

`components/CareerHighlights.vue` contains the shared Spanish/English experience and featured project sections. The latest role is Senior Odoo Developer at MAGAPOR (May 2026–present). Wanapix is May 2024–May 2026; the end date was confirmed by Richard. Responsibilities were checked against https://www.linkedin.com/in/richard-marles/ . NuviaMy is presented as Richard's live independent software project, with the implemented stack and features; no customer numbers or compliance certifications are claimed.

The live pages are `pages/index.vue` (Spanish) and `pages/index-en.vue` (English). They use page-specific SEO metadata, canonical URLs and language alternates. Existing `locales/` files are legacy reference content; an i18n module is not currently enabled. Shared navigation lives in `layouts/default.vue`.

Cloudflare Pages is connected to the GitHub repository and publishes `main`. Validate with `npm ci` and `npm run build`, check both language pages and a narrow viewport, then review the Cloudflare Pages check for the released commit. An older separate Workers Builds integration may also appear in GitHub; it is not the successful Pages deployment for this site.

## SEO and crawlability

`composables/useProfileSeo.ts` renders the language-specific title/description, canonical URLs, reciprocal `hreflang` links (including x-default), social previews and a ProfilePage/Person/WebSite JSON-LD graph on the server. The marked-up identity, employer, city and technologies match visible portfolio content. There are no invented ratings, job offers or article records. Google does not guarantee rich results or rankings from markup.

`public/sitemap.xml` contains only the two canonical published pages, with language alternates. Update its `lastmod` only after substantive content changes. `public/robots.txt` advertises the sitemap and permits public crawling; Cloudflare may prepend its existing managed bot directives. Do not block the JavaScript or stylesheet assets needed for rendering.

The error page preserves Nuxt's 404/error response and adds noindex. The server middleware redirects the exact www hostname to HTTPS apex and normalizes `/index-en/`. Because Cloudflare Pages needs the hostname connected before an origin request can work, the edge www redirect is also configured in Cloudflare. Validate HTTPS/apex/www, path and query preservation, both source HTML documents, sitemap XML, robots, social image and an actual missing URL after release.

References: https://developers.google.com/search/docs/appearance/structured-data/profile-page , https://developers.google.com/search/docs/crawling-indexing/localized-versions , https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap . Submit `https://rmarles.com/sitemap.xml` in the rmarles.com Search Console property when available; publishing a sitemap does not itself request or guarantee indexing.

## Supporting the project

The `#support` section in `CareerHighlights.vue` links to the existing GoFundMe campaign in both languages. It describes NuviaMy as an independent commercial software project and directs visitors to the campaign for the budget and updates. It does not embed a third-party payment widget, collect payment details or claim charitable/tax-exempt status. Update `fundraiserUrl` there if the campaign address changes.
