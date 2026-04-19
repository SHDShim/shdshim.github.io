---
layout: default
title: Dan Shim Talks
description: Talks and media for S.-H. Dan Shim.
nav_key: dan-shim
permalink: /dan-shim-talks.html
---
<section class="page-hero">
  <h1>Talks and Media</h1>
  <nav class="section-nav" aria-label="Dan Shim section">
    <a href="dan-shim.html">Overview</a>
    <a href="dan-shim-cv.html">CV</a>
    <a href="dan-shim-teaching.html">Teaching</a>
    <a class="is-active" href="dan-shim-talks.html">Talks</a>
  </nav>
</section>

<section class="section-block">
  <ul class="list-plain">
    {% for link in site.data.dan_shim.talks.links %}
    <li><a class="text-link" href="{{ link.url }}">{{ link.label }}</a></li>
    {% endfor %}
  </ul>
</section>
