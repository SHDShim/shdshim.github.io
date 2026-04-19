---
layout: default
title: Dan Shim
description: Section landing page for S.-H. Dan Shim.
nav_key: dan-shim
permalink: /dan-shim.html
---
<section class="page-hero profile-hero">
  <div class="profile-hero-copy">
    <h1>{{ site.data.dan_shim.hero.name_html }}</h1>
    <p class="lead">{{ site.data.dan_shim.hero.lead }}</p>
    <nav class="section-nav" aria-label="Dan Shim section">
      <a class="is-active" href="dan-shim.html">Overview</a>
      <a href="dan-shim-cv.html">CV</a>
      <a href="dan-shim-teaching.html">Teaching</a>
      <a href="dan-shim-talks.html">Talks</a>
    </nav>
  </div>
  <div class="profile-hero-photo">
    <div class="profile-photo-ring">
      <img src="{{ site.data.dan_shim.hero.image_url }}" alt="{{ site.data.dan_shim.hero.image_alt }}">
    </div>
  </div>
</section>

<section class="section-block">
  <div class="section-index">
    {% for section in site.data.dan_shim.overview_sections %}
    <details class="section-index-item foldable"{% if section.open %} open{% endif %}>
      <summary class="foldable-summary">
        <h3>{{ section.title }}</h3>
      </summary>
      <div class="foldable-body">
        {% if section.text %}<p>{{ section.text }}</p>{% endif %}
        {% if section.html %}<p>{{ section.html }}</p>{% endif %}
        {% if section.link %}<a class="text-link" href="{{ section.link.url }}">{{ section.link.label }}</a>{% endif %}
      </div>
    </details>
    {% endfor %}
  </div>
</section>

<section class="section-block">
  <div class="grid two-up">
    {% for card in site.data.dan_shim.overview_cards %}
    <details class="card foldable">
      <summary class="foldable-summary"><h3>{{ card.title }}</h3></summary>
      <div class="foldable-body">
        <p>{{ card.text }}</p>
        <a class="text-link" href="{{ card.link.url }}">{{ card.link.label }}</a>
      </div>
    </details>
    {% endfor %}
  </div>
</section>
