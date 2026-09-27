"""Build the small, data-driven pages for the N4M 2027 edition.

Update content.json, then run: python 2027/build.py
"""

import html
import json
import textwrap
from pathlib import Path


ROOT = Path(__file__).parent


def write_page(name, content):
  (ROOT / name).write_text(textwrap.dedent(content).strip() + "\n", encoding="utf-8")


def esc(value):
    return html.escape(str(value))


def sponsor_markup(item):
  logo = ""
  if item.get("logo"):
    logo = f'<img src="{esc(item["logo"])}" alt="{esc(item["name"])}">'
  return (
    f'<div class="sponsor-group sponsor-{esc(item["level"]).lower()}">'
    f'<span class="sponsor-level">{esc(item["level"])}</span>'
    f'{logo}<span class="sponsor-name">{esc(item["name"])}</span></div>'
  )


def organiser_markup():
  return "".join(
    f'<a class="organiser {esc(item.get("class", ""))}" href="{esc(item["href"])}" target="_blank" rel="noopener noreferrer">'
    f'<img src="{esc(item["logo"])}" alt="{esc(item["name"])}"></a>'
    for item in DATA["organisers"]
  )


def layout(content, active, private=False):
    suffix = "_tmp" if private else ""
    links = [
    ("2027", f"index{suffix}.html", "home"),
        ("Overview", f"overview{suffix}.html", "overview"),
        ("Venue", f"venue{suffix}.html", "venue"),
        ("Speakers", f"speakers{suffix}.html", "speakers"),
        ("Programme", f"program{suffix}.html", "program"),
        ("Registration", f"registration{suffix}.html", "registration"),
    ]
    navigation = "".join(
        f'<a class="{("active" if key == active else "")}" href="{url}">{label}</a>'
        for label, url, key in links
    )
    organisers = organiser_markup()
    sponsor_groups = "".join(sponsor_markup(item) for item in DATA["sponsors"] if item.get("level") != "Gold")
    institutional_groups = "".join(
      f'<div class="institutional-group">'
      f'{(f'<img src="{esc(item["logo"])}" alt="{esc(item["name"])}">' if item.get("logo") else "")}'
      f'<span>{esc(item["name"])}</span></div>'
      for item in DATA["institutional_supporters"]
    )
    if not institutional_groups:
        institutional_groups = '<div class="institutional-group institutional-placeholder">Institutional supporters to be announced</div>'
    sponsor_section = "" if active == "home" else f"""
    <section class="sponsor-strip" aria-labelledby="sponsors-heading">
      <div class="container">
        <p class="eyebrow" id="sponsors-heading">Institutional support</p>
        <div class="institutional-grid">{institutional_groups}</div>
        <p class="eyebrow commercial-heading">Meeting partners</p>
        <div class="sponsor-grid">{sponsor_groups}</div>
      </div>
    </section>
    """
    gold_sponsor = next((item for item in DATA["sponsors"] if item.get("level") == "Gold"), None)
    gold_banner = ""
    if active in {"overview", "venue", "speakers", "program"} and gold_sponsor:
        gold_banner = (
            f'<div class="page-gold-banner">{sponsor_markup(gold_sponsor)}</div>'
        )
    if gold_banner and active in {"overview", "venue", "speakers", "program"}:
        content = content.replace("<h1>", '<div class="page-top-shell"><div class="page-header-copy"><h1>', 1)
        content = content.replace("</h1>", '</h1></div>' + gold_banner + '</div><div class="page-divider"></div>', 1)
    main_content = content if active != "home" else content
    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="{esc(DATA['title'])}">
    <title>{esc(DATA['title'])} - {esc(active.title())}</title>
    <link href="../css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="theme.css">
  </head>
  <body>
    <header class="site-header">
      <div class="container header-inner">
        <a class="brand" href="index{suffix}.html"><img src="../img/n4m_k.svg" alt="Nanoengineering for Mechanobiology"></a>
        <nav aria-label="Edition navigation">
          {navigation}
          <a href="../index.html">N4M home</a>
        </nav>
      </div>
    </header>
    <main class="container page-content">
      {main_content}
    </main>
    {sponsor_section}
    <footer class="site-footer">
      <div class="container footer-inner"><span>Organised by</span><div class="organiser-list">{organisers}</div></div>
    </footer>
  </body>
</html>
"""


def build_overview(private=False):
    topics = "".join(f"<li>{esc(topic)}</li>" for topic in DATA["topics"])
    content = f"""
      <p class="eyebrow">{esc(DATA['date'])} · {esc(DATA['location'])}</p>
      <h1>{esc(DATA['theme'])}</h1>
      <p class="lead">{esc(DATA['description'])}</p>
      <section>
        <h2>Focus areas</h2>
        <ul class="topic-list">{topics}</ul>
      </section>
    """
    return layout(content, "overview", private=private)


def build_venue(private=False):
    venue = DATA["venue"]
    content = f"""
      <p class="eyebrow">{esc(DATA['date'])} · {esc(venue['location'])}</p>
      <h1>{esc(venue['name'])}</h1>
      <div class="venue-layout">
        <div>
          <p class="lead">{esc(venue['description'])}</p>
          <p><a class="venue-link" href="{esc(venue['url'])}" target="_blank" rel="noopener noreferrer">Visit the hotel website</a></p>
          <p><a class="venue-link" href="{esc(venue['gallery_url'])}" target="_blank" rel="noopener noreferrer">View the hotel gallery</a></p>
          <p><a class="venue-link" href="{esc(venue['maps_url'])}" target="_blank" rel="noopener noreferrer">Open in Google Maps</a></p>
        </div>
        <figure class="venue-media">
          <img src="{esc(venue['image'])}" alt="{esc(venue['image_alt'])}">
          <figcaption>Hotel Cenobio dei Dogi, Camogli</figcaption>
        </figure>
      </div>
    """
    return layout(content, "venue", private=private)


def registration_action(url, label):
    if url:
        return f'<a class="registration-action" href="{esc(url)}" target="_blank" rel="noopener noreferrer">{label}</a>'
    return f'<span class="registration-action is-pending">{label} · Link to be announced</span>'


def build_registration(private=False):
    dates = DATA["important_dates"]
    registration = DATA["registration"]
    content = f"""
      <p class="eyebrow">N4M 2027</p>
      <h1>Registration</h1>
      <p class="lead">Registration and abstract submission will be managed from this page as the 2027 meeting opens.</p>
      <section class="date-list" aria-labelledby="dates-heading">
        <h2 id="dates-heading">Important dates</h2>
        <dl>
          <div><dt>Abstract submission deadline</dt><dd>{esc(dates['abstract_deadline'])}</dd></div>
          <div><dt>Early-bird registration deadline</dt><dd>{esc(dates['early_bird_deadline'])}</dd></div>
        </dl>
      </section>
      <div class="registration-grid">
        <section>
          <p class="eyebrow">Attendance</p>
          <h2>Register for N4M 2027</h2>
          <p>{esc(registration['registration_note'])}</p>
          {registration_action(registration['registration_url'], 'Registration form')}
        </section>
        <section>
          <p class="eyebrow">Contributions</p>
          <h2>Submit an abstract</h2>
          <p>{esc(registration['abstract_note'])}</p>
          {registration_action(registration['abstract_url'], 'Abstract submission form')}
        </section>
      </div>
    """
    return layout(content, "registration", private=private)


def build_home(private=False):
    sponsors = "".join(sponsor_markup(item) for item in DATA["sponsors"])
    topics = "".join(
        f"<li>{esc(topic)}</li>" for topic in DATA["topics"]
    )
    dates = DATA["important_dates"]
    gold_sponsor = next((item for item in DATA["sponsors"] if item.get("level") == "Gold"), None)
    remaining_sponsors = [item for item in DATA["sponsors"] if item.get("level") != "Gold"]
    sponsor_stack = "".join(sponsor_markup(item) for item in remaining_sponsors)
    gold_banner = ""
    if gold_sponsor:
        gold_banner = (
            f'<div class="home-sponsor-banner" aria-label="Gold sponsor">'
            f'<p class="eyebrow">Gold sponsor</p>'
            f'{sponsor_markup(gold_sponsor)}'
            f'</div>'
        )
    home_links = "".join(
        f'<a href="{("overview" if not private else "overview_tmp")}.html">Overview</a>'
        f'<a href="{("venue" if not private else "venue_tmp")}.html">Venue</a>'
        f'<a href="{("speakers" if not private else "speakers_tmp")}.html">Speakers</a>'
        f'<a href="{("program" if not private else "program_tmp")}.html">Programme</a>'
        for _ in [0]
    )
    organisers_html = ""
    if private:
        organisers_html = f"""
          <section class="organiser-section">
            <h2>Organisers</h2>
            <div class="speaker-grid">
              <article class="speaker-card speaker-card--compact">
                <div class="speaker-card__body">
                  <span class="speaker-tag">Organiser</span>
                  <h3>Daniel Müller</h3>
                  <div class="speaker-meta">Full Professor, Department of Biosystems Science and Engineering, ETH Zurich, Basel</div>
                  <a href="https://bsse.ethz.ch/people/detail-person.MTcwMTk1.TGlzdC8yNjY5LC0xMDExNjczNjI=.html" target="_blank" rel="noopener noreferrer" class="speaker-link">visit website</a>
                </div>
                <div class="speaker-card__media">
                  <img src="speakers/daniel-muller.jpg" alt="Daniel Müller" class="speaker-card__image">
                </div>
              </article>
              <article class="speaker-card speaker-card--compact">
                <div class="speaker-card__body">
                  <span class="speaker-tag">Organiser</span>
                  <h3>Massimo Vassalli</h3>
                  <div class="speaker-meta">University of Glasgow, James Watt School of Engineering</div>
                  <a href="https://www.gla.ac.uk/schools/engineering/staff/massimovassalli/" target="_blank" rel="noopener noreferrer" class="speaker-link">visit website</a>
                </div>
                <div class="speaker-card__media">
                  <img src="speakers/massimo-vassalli.png" alt="Massimo Vassalli" class="speaker-card__image">
                </div>
              </article>
            </div>
          </section>
        """
    content = f"""
      <div class="home-hero row g-5 align-items-start">
        <div class="col-lg-8">
          <p class="eyebrow">{esc(DATA['date'])} · {esc(DATA['location'])}</p>
          <h1>{esc(DATA['title'])}</h1>
          <h2 class="home-theme">{esc(DATA['theme'])}</h2>
          <div class="home-links">
            <a href="{('overview.html' if not private else 'overview_tmp.html')}">Overview</a>
            <a href="{('venue.html' if not private else 'venue_tmp.html')}">Venue</a>
            <a href="{('speakers.html' if not private else 'speakers_tmp.html')}">Speakers</a>
            <a href="{('program.html' if not private else 'program_tmp.html')}">Programme</a>
            <a href="mailto:massimo.vassalli@glasgow.ac.uk">Contact</a>
          </div>
          <section class="home-details">
            <h2>At a glance</h2>
            <ul class="topic-list">{topics}</ul>
            <h2>Important dates</h2>
            <ul class="topic-list">
              <li>Abstract submission deadline: {esc(dates['abstract_deadline'])}</li>
              <li>Early-bird registration deadline: {esc(dates['early_bird_deadline'])}</li>
            </ul>
          </section>
          {organisers_html}
        </div>
        <aside class="col-lg-4 sponsor-rail" aria-labelledby="home-sponsors-heading">
          <div class="sponsor-header-row">
            <p class="eyebrow" id="home-sponsors-heading">Sponsors</p>
          </div>
          {gold_banner}
          <div class="sponsor-stack">{sponsor_stack}</div>
        </aside>
      </div>
    """
    return layout(content, "home", private=private)


def build_teaser():
    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="{esc(DATA['title'])}">
    <title>{esc(DATA['title'])} - Private preview</title>
    <link href="../css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="theme.css">
  </head>
  <body>
    <header class="site-header">
      <div class="container header-inner">
        <a class="brand" href="index.html"><img src="../img/n4m_k.svg" alt="Nanoengineering for Mechanobiology"></a>
      </div>
    </header>
    <main class="container page-content">
      <p class="eyebrow">N4M 2027</p>
      <h1>Preview coming soon</h1>
      <p class="lead">This site is currently in private preview mode. Please use the direct invitation link to access the full programme and speaker information.</p>
      <p><a class="registration-action" href="index_tmp.html">Open the private preview</a></p>
    </main>
    <footer class="site-footer">
      <div class="container footer-inner"><span>Organised by</span><div class="organiser-list">{organiser_markup()}</div></div>
    </footer>
  </body>
</html>
"""


def speaker_card_markup(speaker):
    initials = "".join(part[0].upper() for part in speaker["name"].split()[:2])
    image = speaker.get("image")
    if image:
        media = f'<img src="{esc(image)}" alt="{esc(speaker["name"])}" class="speaker-card__image">'
    else:
        media = f'<div class="speaker-card__placeholder" aria-hidden="true">{esc(initials)}</div>'

    url = speaker.get("url")
    website_link = ""
    if url:
        website_link = (
            f'<a href="{esc(url)}" target="_blank" rel="noopener noreferrer" class="speaker-link">'
            f'visit the website</a>'
        )

    field = speaker.get("field") or "Mechanobiology"
    summary = speaker.get("summary") or ""
    summary_html = f'<p>{esc(summary)}</p>' if summary else ""

    return (
        f'<article class="speaker-card">'
        f'<div class="speaker-card__body">'
        f'<span class="speaker-tag">{esc(field)}</span>'
        f'<h3>{esc(speaker["name"])}</h3>'
        f'<div class="speaker-meta">{esc(speaker.get("affiliation", ""))}</div>'
        f'{summary_html}'
        f'{website_link}'
        f'</div>'
        f'<div class="speaker-card__media">{media}</div>'
        f'</article>'
    )


def build_speakers(private=False):
    if DATA["speakers"]:
        rows = []
        for index in range(0, len(DATA["speakers"]), 2):
            pair = DATA["speakers"][index:index + 2]
            cards = "".join(speaker_card_markup(speaker) for speaker in pair)
            rows.append(f'<div class="speaker-row">{cards}</div>')
        speakers = "".join(rows)
    else:
        speakers = '<div class="speaker-row"><article class="speaker-card speaker-card--empty"><div class="speaker-card__body"><p>Invited speakers will be announced soon.</p></div></article></div>'
    content = f'<p class="eyebrow">N4M 2027</p><h1>Invited Speakers</h1><div class="speaker-grid">{speakers}</div>'
    return layout(content, "speakers", private=private)


def build_program(private=False):
    sessions = []
    for session in DATA["sessions"]:
        items = "".join(
            f"<li><strong>{esc(item['time'])}</strong> · {esc(item['type'])}<br>{esc(item['title'])}</li>"
            for item in session["items"]
        )
        sessions.append(
            f"<article><p class=\"eyebrow\">{esc(session['time'])}</p>"
            f"<h2>{esc(session['title'])}</h2><p>Chair: {esc(session['chair'])}</p>"
            f"<ul class=\"program-list\">{items}</ul></article>"
        )
    content = f"<p class=\"eyebrow\">N4M 2027</p><h1>Programme</h1>{''.join(sessions)}"
    return layout(content, "program", private=private)


with (ROOT / "content.json").open(encoding="utf-8") as source:
    DATA = json.load(source)

write_page("index.html", build_teaser())
write_page("index_tmp.html", build_home(private=True))
write_page("overview_tmp.html", build_overview(private=True))
write_page("venue_tmp.html", build_venue(private=True))
write_page("speakers_tmp.html", build_speakers(private=True))
write_page("program_tmp.html", build_program(private=True))
write_page("registration_tmp.html", build_registration(private=True))
print("Built 2027 teaser index.html and private preview pages index_tmp.html, overview_tmp.html, venue_tmp.html, speakers_tmp.html, program_tmp.html, and registration_tmp.html")