---
layout: default
title: People
description: People page for the Dan Shim Lab.
nav_key: people
permalink: /people.html
---
<section class="page-hero profile-hero people-hero">
  <div class="profile-hero-copy">
    <h1>{{ site.data.people.hero.title }}</h1>
    <p class="lead">
      {{ site.data.people.hero.lead }}
    </p>
    <nav class="section-nav" aria-label="People section">
      <a class="is-active" href="people.html">Overview</a>
      <a href="#current-members">Current members</a>
      <a href="#alumni">Alumni</a>
    </nav>
  </div>
  <div class="profile-hero-photo people-hero-photo">
    <div class="people-collage-frame">
      <img class="people-collage" src="assets/images/people-collage.png" alt="Collage of Dan Shim Lab people">
    </div>
  </div>
</section>

<section id="current-members" class="section-block">
  <details class="card card-wide foldable" open>
    <summary class="foldable-summary">
      <h2>Current members</h2>
    </summary>
    <div class="foldable-body">
      <div class="grid three-up">
        {% for person in site.data.people.current_members %}
        <article class="card member-card">
          <h3>{{ person.name }}</h3>
          <p>{{ person.role }}</p>
        </article>
        {% endfor %}
      </div>
    </div>
  </details>
</section>

<section id="alumni" class="section-block">
  <details class="card card-wide foldable">
    <summary class="foldable-summary">
      <h2>Alumni</h2>
    </summary>
    <div class="foldable-body subpage-stack">
      {% for person in site.data.people.alumni %}
      <article class="subpage-item">
        <p>
          {{ person.name }} ({{ person.years }}) {{ person.role }}.
          {% if person.current %} {{ person.current }}{% endif %}
        </p>
      </article>
      {% endfor %}
    </div>
  </details>
</section>
