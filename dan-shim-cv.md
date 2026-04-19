---
layout: default
title: Dan Shim CV
description: Curriculum vitae for S.-H. Dan Shim.
nav_key: dan-shim
permalink: /dan-shim-cv.html
---
<section class="page-hero">
  <h1>Curriculum Vitae</h1>
  <nav class="section-nav" aria-label="Dan Shim section">
    <a href="dan-shim.html">Overview</a>
    <a class="is-active" href="dan-shim-cv.html">CV</a>
    <a href="dan-shim-teaching.html">Teaching</a>
    <a href="dan-shim-talks.html">Talks</a>
  </nav>
</section>

<section class="section-block">
  <h2>Positions held</h2>
  <div class="subpage-stack">
    {% for item in site.data.dan_shim.cv.positions %}
    <article class="subpage-item"><p>{{ item }}</p></article>
    {% endfor %}
  </div>
</section>

<section class="section-block">
  <h2>Education</h2>
  <div class="subpage-stack">
    {% for item in site.data.dan_shim.cv.education %}
    <article class="subpage-item"><p>{{ item }}</p></article>
    {% endfor %}
  </div>
</section>

<section class="section-block">
  <div class="grid two-up">
    <article class="card card-wide">
      <h2>Contact</h2>
      <div class="contact-block">
        {% for line in site.data.dan_shim.cv.contact %}<p>{{ line }}</p>{% endfor %}
      </div>
    </article>
    <article class="card card-wide">
      <h2>Personal info</h2>
      <ul class="list-plain">
        {% for link in site.data.dan_shim.cv.personal_links %}
        <li><a class="text-link" href="{{ link.url }}"{% if link.url contains 'http' %} target="_blank" rel="noreferrer"{% endif %}>{{ link.label }}</a></li>
        {% endfor %}
      </ul>
    </article>
  </div>
</section>
