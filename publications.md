---
layout: default
title: Publications
description: Publication list for the Dan Shim Lab.
nav_key: publications
permalink: /publications.html
---
{% assign publications_data = site.data.publications_generated %}
<section class="page-hero profile-hero text-only-hero">
  <div class="profile-hero-copy">
    <h1>{{ publications_data.hero.title }}</h1>
    <p class="hero-metadata">{{ publications_data.hero.note_html }}</p>
  </div>
</section>

{% for period in publications_data.periods %}
<section class="section-block publication-period-section">
  <details class="card card-wide foldable publication-year"{% if period.open %} open{% endif %}>
    <summary class="foldable-summary">
      <h2>{{ period.label }}</h2>
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
</section>
{% endfor %}
