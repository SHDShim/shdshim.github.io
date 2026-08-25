---
layout: default
title: Dan Shim
description: Section landing page for S.-H. Dan Shim.
nav_key: dan-shim
permalink: /dan-shim.html
---
{% include dan-shim-hero.html %}

{% assign research_profile = site.data.dan_shim.overview_sections | where: "title", "Research profile" | first %}
{% assign teaching_intro = site.data.dan_shim.overview_sections | where: "title", "Teaching and mentoring" | first %}
{% assign affiliations = site.data.dan_shim.overview_sections | where: "title", "Affiliations" | first %}

<section id="overview" class="section-block">
  <details class="card card-wide foldable" open>
    <summary class="foldable-summary">
      <h2>Overview</h2>
    </summary>
    <div class="foldable-body">
      <h3>{{ research_profile.title }}</h3>
      <p>{{ research_profile.text }}</p>
      <h3>{{ affiliations.title }}</h3>
      <p>{{ affiliations.html }}</p>
    </div>
  </details>
</section>

<section id="professional-background" class="section-block">
  <details class="card card-wide foldable">
    <summary class="foldable-summary">
      <h2>Professional Background</h2>
    </summary>
    <div class="foldable-body">
      <div class="topic-cluster">
        <details class="subpage-item foldable" open>
          <summary class="foldable-summary"><h3>Positions held</h3></summary>
          <ul class="foldable-body list-plain">
            {% for item in site.data.dan_shim.cv.positions %}
            <li>{{ item }}</li>
            {% endfor %}
          </ul>
        </details>
        <details class="subpage-item foldable">
          <summary class="foldable-summary"><h3>Education</h3></summary>
          <ul class="foldable-body list-plain">
            {% for item in site.data.dan_shim.cv.education %}
            <li>{{ item }}</li>
            {% endfor %}
          </ul>
        </details>
        <details class="subpage-item foldable">
          <summary class="foldable-summary"><h3>Contact</h3></summary>
          <div class="foldable-body contact-block">
            {% for line in site.data.dan_shim.cv.contact %}<p>{{ line }}</p>{% endfor %}
          </div>
        </details>
        <details class="subpage-item foldable">
          <summary class="foldable-summary"><h3>Personal info</h3></summary>
          <ul class="foldable-body list-plain">
            {% for link in site.data.dan_shim.cv.personal_links %}
            <li><a class="text-link" href="{{ link.url }}"{% if link.url contains 'http' %} target="_blank" rel="noreferrer"{% endif %}>{{ link.label }}</a></li>
            {% endfor %}
          </ul>
        </details>
      </div>
    </div>
  </details>
</section>

<section id="teaching" class="section-block">
  <details class="card card-wide foldable">
    <summary class="foldable-summary">
      <h2>Teaching</h2>
    </summary>
    <div class="foldable-body">
      <p>{{ teaching_intro.text }}</p>
      <div class="topic-cluster">
        {% for topic in site.data.dan_shim.teaching.topics %}
        <details class="subpage-item foldable">
          <summary class="foldable-summary">
            <h3>{{ topic.title }}</h3>
          </summary>
          <div class="foldable-body">
            <p>{{ topic.text }}</p>
          </div>
        </details>
        {% endfor %}
      </div>
    </div>
  </details>
</section>

<section id="talks" class="section-block">
  <details class="card card-wide foldable">
    <summary class="foldable-summary">
      <h2>Talks</h2>
    </summary>
    <ul class="foldable-body list-plain">
      {% for link in site.data.dan_shim.talks.links %}
      <li><a class="text-link" href="{{ link.url }}" target="_blank" rel="noreferrer">{{ link.label }}</a></li>
      {% endfor %}
    </ul>
  </details>
</section>
