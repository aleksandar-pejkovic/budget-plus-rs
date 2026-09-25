"""Semantic HTML rendering for the solution pages."""
import html
import json

from solution_content import DETAILS
from site_layout import header, footer


def esc(value):
    return html.escape(str(value), quote=True)


def list_items(values):
    return "".join(f"<li>{esc(value)}</li>" for value in values)


def render_image(item):
    compact = ' solution-media-compact' if item.get('compact') else ''
    return f'''<figure class="solution-media{compact}"><a class="zoom-image" href="../assets/img/{esc(item['file'])}"><img src="../assets/img/{esc(item['file'])}"
          alt="{esc(item['alt'])}" loading="lazy" width="{item['width']}" height="{item['height']}"></a>
          <figcaption>{esc(item['caption'])}</figcaption></figure>'''


def render_solution(page, base, lastmod, labels):
    slug, title, desc, kicker, h1, intro, benefits, related = page
    detail = DETAILS[slug]
    workflow_image = render_image(detail['workflow_image']) if detail.get('workflow_image') else ''
    canonical = f"{base}/{slug}/"
    schema = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebPage", "@id": canonical, "url": canonical, "name": title,
         "description": desc, "isPartOf": {"@id": f"{base}/#website"},
         "about": {"@id": f"{base}/#software"}, "inLanguage": "sr", "dateModified": lastmod},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Početna", "item": f"{base}/"},
            {"@type": "ListItem", "position": 2, "name": h1, "item": canonical}]},
    ]}
    workflow_link = ""
    if link := detail.get("workflow_link"):
        workflow_link = f'<p>{esc(link["text"])}</p><a class="text-link" href="../{esc(link["slug"])}/#postupak">{esc(link["label"])} &rarr;</a>'
    advance = ""
    if item := detail.get("advance"):
        image = render_image(item['image']) if 'image' in item else ''
        advance = f'<aside id="avansi" class="advance-summary"><h3>{esc(item["title"])}</h3><p>{esc(item["text"])}</p>{image}<a class="text-link" href="../{esc(item["slug"])}/#avansi">{esc(item["label"])} &rarr;</a></aside>'
    links = "".join(f'<a href="../{esc(s)}/">{esc(labels[s])} &rarr;</a>' for s in related)
    media = ""
    for item in detail.get("media", []):
        media += render_image(item)
    if video := detail.get("video"):
        media += f'''<figure class="solution-media"><video controls playsinline preload="none"
          aria-label="Pregled obračuna plate u nalogu" poster="../assets/img/{esc(video['poster'])}">
          <source src="../assets/media/{esc(video['file'])}" type="video/mp4">
          <a href="../assets/media/{esc(video['file'])}">Preuzmite video prikaz obračuna plate</a>
          </video><figcaption>{esc(video['caption'])}</figcaption></figure>'''
    if media:
        media = f'<section aria-labelledby="prikaz"><h2 id="prikaz">Pogledajte program</h2>{media}</section>'
    return f'''<!doctype html>
<html lang="sr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(desc)}">
  <link rel="canonical" href="{canonical}">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(desc)}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta property="og:locale" content="sr_RS">
  <meta property="og:image" content="{base}/assets/img/budzet-plus-share.png">
  <meta property="og:image:type" content="image/png">
  <meta property="og:image:width" content="3600">
  <meta property="og:image:height" content="982">
  <meta property="og:image:alt" content="Budžet+ logo">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc(title)}">
  <meta name="twitter:description" content="{esc(desc)}">
  <meta name="twitter:image" content="{base}/assets/img/budzet-plus-share.png">
  <script type="application/ld+json">{json.dumps(schema, ensure_ascii=False, separators=(',', ':'))}</script>
  <link rel="icon" href="../assets/img/budget_plus_logo.ico">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/styles.css">
</head>
<body class="landing-body">
  {header("../", slug)}
  <main id="main-content">
    <nav class="container breadcrumbs" aria-label="Putanja"><ol>
      <li><a href="../">Početna</a></li><li aria-hidden="true">/</li><li aria-current="page">{esc(h1)}</li>
    </ol></nav>
    <section class="landing-hero"><div class="container landing-hero-grid">
      <div><p class="landing-kicker">{esc(kicker)}</p><h1>{esc(h1)}</h1><p class="lede">{esc(intro)}</p><a class="btn primary" href="../?tema={esc(slug)}#kontakt">Prijavite se za prezentaciju ↗</a></div>
      <aside class="landing-summary"><h2>Šta dobijate</h2><ul>{list_items(benefits)}</ul></aside>
    </div></section>
    <div class="container solution-layout"><div class="solution-content">
      <section aria-labelledby="postupak"><h2 id="postupak">Kako radi</h2>
        <p>{esc(detail['how'])}</p>{workflow_image}{advance}{workflow_link}
      </section>
{media}
      <div class="landing-cta"><h2>Pogledajte Budžet+ u radu</h2>
        <p>Pogledajte kako Budžet+ pojednostavljuje ovaj posao.</p>
        <a class="btn primary" href="../?tema={esc(slug)}#kontakt">Prijavite se za prezentaciju</a>
      </div>
      <section aria-labelledby="povezano"><h2 id="povezano">Povezana rešenja</h2><div class="related-links">{links}</div></section>
    </div></div>
  </main>
  {footer("../")}
</body>
</html>
'''
