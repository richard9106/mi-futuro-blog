"""Check rendered SEO contracts against local, Pages-preview or production HTTP.

Usage: python3 scripts/check_seo.py https://rmarles.com --www
No credentials, analytics or external validation services are used.
"""
import argparse
from html.parser import HTMLParser
import json
from urllib.error import HTTPError
from urllib.parse import urljoin
from urllib.request import Request, build_opener, HTTPRedirectHandler
from xml.etree import ElementTree


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, *args):
        return None


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.meta, self.links, self.schemas, self.anchors = [], [], [], []
        self.h1s, self.language, self.in_schema = 0, '', False
        self.schema_text = ''

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'html': self.language = attrs.get('lang')
        if tag == 'h1': self.h1s += 1
        if tag == 'meta': self.meta.append(attrs)
        if tag == 'link': self.links.append(attrs)
        if tag == 'a': self.anchors.append(attrs)
        if tag == 'script' and attrs.get('type') == 'application/ld+json':
            self.in_schema, self.schema_text = True, ''

    def handle_endtag(self, tag):
        if tag == 'script' and self.in_schema:
            self.schemas.append(json.loads(self.schema_text))
            self.in_schema = False

    def handle_data(self, text):
        if self.in_schema: self.schema_text += text


def fetch(url):
    request = Request(url, headers={'Accept': 'text/html', 'User-Agent': 'Portfolio-SEO-Check'})
    try:
        response = build_opener(NoRedirect).open(request, timeout=35)
    except HTTPError as response:
        return response.code, response.headers, response.read().decode()
    with response:
        body = response.read()
        text = '' if response.headers.get('Content-Type','').startswith('image/') else body.decode()
        return response.status, response.headers, text


def check(origin, www=False):
    canonical = 'https://rmarles.com'
    for path, language in [('/', 'es'), ('/index-en', 'en')]:
        status, _, html = fetch(origin + path)
        assert status == 200, (path, status)
        page = Page(); page.feed(html)
        assert page.language == language and page.h1s == 1, (path, page.language, page.h1s)
        links = [link for link in page.links if link.get('rel') == 'canonical']
        assert len(links) == 1 and links[0]['href'] == canonical + path, links
        alternates = {link['hreflang']:link['href'] for link in page.links if link.get('rel') == 'alternate' and 'hreflang' in link}
        assert alternates == {'es':canonical+'/', 'en':canonical+'/index-en', 'x-default':canonical+'/'}, alternates
        meta = {tag.get('name',tag.get('property')):tag.get('content') for tag in page.meta}
        for key in ['description','og:title','og:description','og:image','twitter:title','twitter:image']:
            assert meta.get(key), (path,key)
        assert meta['og:url'] == canonical + path
        assert len(page.schemas) == 1
        graph = {node['@type']:node for node in page.schemas[0]['@graph']}
        assert graph['ProfilePage']['mainEntity']['@id'] == graph['Person']['@id']
        assert graph['Person']['name'] == 'Richard Marles'
        assert graph['Person']['worksFor']['name'] == 'MAGAPOR'
        assert graph['ProfilePage']['url'] == canonical + path
        assert 'Richard Marles' in html and 'NuviaMy' in html and 'Wanapix' in html
        campaign = [a for a in page.anchors if a.get('href') == 'https://www.gofundme.com/f/help-nuviamy-grow-so-therapists-can-focus-on-care']
        assert campaign and campaign[0].get('target') == '_blank'
        assert 'noopener' in campaign[0].get('rel','') and 'id="support"' in html
        print(path, 'SSR metadata, language links and profile schema: OK')
    status, _, xml = fetch(origin+'/sitemap.xml'); assert status == 200
    root = ElementTree.fromstring(xml)
    ns = {'s':'http://www.sitemaps.org/schemas/sitemap/0.9','x':'http://www.w3.org/1999/xhtml'}
    urls = root.findall('s:url',ns)
    assert {url.find('s:loc',ns).text for url in urls} == {canonical+'/',canonical+'/index-en'}
    for url in urls:
        assert {item.attrib['hreflang']:item.attrib['href'] for item in url.findall('x:link',ns)} == alternates
    status, _, robots = fetch(origin+'/robots.txt')
    assert status == 200 and 'Sitemap: https://rmarles.com/sitemap.xml' in robots
    status, _, html = fetch(origin+'/seo-check-missing-page')
    assert status == 404, ('missing-page',status)
    error = Page(); error.feed(html)
    assert any(tag.get('name') == 'robots' and 'noindex' in tag.get('content','') for tag in error.meta)
    assert not error.schemas
    status, headers, _ = fetch(origin+'/index-en/?source=seo-check')
    assert status == 301 and urljoin(origin,headers['Location']) == origin+'/index-en?source=seo-check', (status,headers.get('Location'))
    status, headers, _ = fetch(origin+'/mia.jpeg')
    assert status == 200 and 'image/' in headers.get('Content-Type','')
    if www:
        for scheme in ['http','https']:
            status, headers, _ = fetch(f'{scheme}://www.rmarles.com/index-en?source=seo-check')
            assert status == 301 and headers['Location'] == canonical+'/index-en?source=seo-check', (status,headers.get('Location'))
    print('Sitemap, robots, real 404/noindex, image and canonical redirects: OK')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('origin',nargs='?',default='http://127.0.0.1:3011')
    parser.add_argument('--www',action='store_true')
    args = parser.parse_args()
    check(args.origin.rstrip('/'),args.www)
