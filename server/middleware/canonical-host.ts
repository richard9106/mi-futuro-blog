export default defineEventHandler((event) => {
  const url = getRequestURL(event)
  if (url.hostname.toLowerCase() === 'www.rmarles.com') {
    return sendRedirect(event, `https://rmarles.com${url.pathname}${url.search}`, 301)
  }
  if (url.pathname === '/index-en/') {
    return sendRedirect(event, `/index-en${url.search}`, 301)
  }
})
