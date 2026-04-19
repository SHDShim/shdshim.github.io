---
layout: default
title: Dan Shim Teaching
description: Teaching information for S.-H. Dan Shim.
nav_key: dan-shim
permalink: /dan-shim-teaching.html
---
<section class="page-hero">
  <h1>Teaching</h1>
  <nav class="section-nav" aria-label="Dan Shim section">
    <a href="dan-shim.html">Overview</a>
    <a href="dan-shim-cv.html">CV</a>
    <a class="is-active" href="dan-shim-teaching.html">Teaching</a>
    <a href="dan-shim-talks.html">Talks</a>
  </nav>
</section>

<section class="section-block">
  <div class="subpage-stack">
    {% for topic in site.data.dan_shim.teaching.topics %}
    <article class="subpage-item">
      <h3>{{ topic.title }}</h3>
      <p>{{ topic.text }}</p>
    </article>
    {% endfor %}
  </div>
</section>
