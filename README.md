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
