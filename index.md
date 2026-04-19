---
layout: home
title: Dan Shim Lab
description: Dan Shim Lab at Arizona State University studying planetary materials and interiors under extreme conditions.
nav_key: home
permalink: /index.html
---
<main>
<section class="home-hero">
  <div class="home-hero-image" aria-hidden="true"></div>
  <nav class="home-nav" aria-label="Primary">
    <a class="is-active" href="index.html">Home</a>
    <a href="dan-shim.html">Dan Shim</a>
    <a href="people.html">People</a>
    <a href="research.html">Research</a>
    <a href="resources.html">Resources</a>
  </nav>
  <div class="home-hero-overlay">
    <div class="home-hero-copy">
      <h1>{{ site.data.home.hero.title }}</h1>
      <p class="home-subtitle">{{ site.data.home.hero.subtitle }}</p>
    </div>
    <a class="home-scroll" href="#intro" aria-label="Scroll to introduction">⌄</a>
  </div>
</section>

<section id="intro" class="section-block home-intro">
  <div class="home-copy">
    {% for paragraph in site.data.home.intro.paragraphs %}
    <p>{{ paragraph }}</p>
    {% endfor %}
    <p>
      {{ site.data.home.media.lead }}
      {% for link in site.data.home.media.links %}
      <a href="{{ link.url }}">{{ link.label }}</a>{% if forloop.last %}.{% else %},{% endif %}
      {% endfor %}
      {{ site.data.home.news.lead }}
      {% for link in site.data.home.news.links %}
      <a href="{{ link.url }}">{{ link.label }}</a>{% if forloop.last %},{% else %},{% endif %}
      {% endfor %}
      featured reports in Nature
      ({% for link in site.data.home.news.nature %}<a href="{{ link.url }}">{{ link.label }}</a>{% unless forloop.last %}; {% endunless %}{% endfor %}).
    </p>
    <p>
      <a href="{{ site.data.home.facility.url }}">{{ site.data.home.facility.text }}</a>.
    </p>
  </div>
</section>
</main>
