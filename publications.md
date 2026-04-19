---
layout: default
title: Publications
description: Publication list for the Dan Shim Lab.
nav_key: publications
permalink: /publications.html
---
<section class="page-hero profile-hero publications-hero">
  <div class="profile-hero-copy">
    <h1>{{ site.data.publications.hero.title }}</h1>
    <p class="publication-note">{{ site.data.publications.hero.note_html }}</p>
  </div>
  <div class="profile-hero-photo publications-hero-photo">
    <img class="hero-title-image publications-hero-image" src="{{ site.data.publications.hero.image }}" alt="{{ site.data.publications.hero.image_alt }}">
  </div>
</section>

<section class="section-block">
  <div class="publication-stack">
    {% for period in site.data.publications.periods %}
    <details class="card foldable publication-year"{% if period.open %} open{% endif %}>
      <summary class="foldable-summary">
        <p class="time-label">{{ period.label }}</p>
      </summary>
      <div class="foldable-body">
        <div class="subpage-stack publication-list">
          {% for entry in period.entries_html %}
          <article class="subpage-item publication-item">
            <p>{{ entry }}</p>
          </article>
          {% endfor %}
        </div>
      </div>
    </details>
    {% endfor %}
  </div>
</section>
