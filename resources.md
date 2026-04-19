---
layout: default
title: Resources
description: Resources and transition notes for the Dan Shim Lab site migration.
body_class: resources-page
nav_key: resources
permalink: /resources.html
---
<section class="page-hero profile-hero resources-hero">
  <div class="profile-hero-copy">
    <h1>{{ site.data.resources.hero.title }}</h1>
    <p class="lead">{{ site.data.resources.hero.lead }}</p>
    <nav class="section-nav" aria-label="Resources section">
      <a class="is-active" href="resources.html">Overview</a>
      <a href="#resources-software">Software</a>
      <a href="#resources-gists">Gists</a>
      <a href="#resources-video-tutorials">Tutorials</a>
      <a href="#resources-members-only">Members only</a>
      <a href="#resources-gallery">Gallery</a>
      <a href="#resources-links">Links</a>
    </nav>
  </div>
  <div class="profile-hero-photo resources-hero-photo">
    <img class="hero-title-image resources-hero-image" src="{{ site.data.resources.hero.image }}" alt="{{ site.data.resources.hero.image_alt }}">
  </div>
</section>

<section id="resources-software" class="section-block">
  <details class="card card-wide foldable" open>
    <summary class="foldable-summary"><h2>Software</h2></summary>
    <div class="foldable-body">
      <p class="lead">{{ site.data.resources.software.lead }}</p>
      <div class="mini-links"><a href="{{ site.data.resources.software.github_home }}" target="_blank" rel="noreferrer">GitHub homepage</a></div>
      <div class="grid three-up">
        {% for item in site.data.resources.software.items %}
        <details class="card foldable">
          <summary class="foldable-summary"><h3>{{ item.title }}</h3></summary>
          <div class="foldable-body">
            <p>{{ item.description }}</p>
            <div class="mini-links">
              {% for link in item.links %}
              <a href="{{ link.url }}" target="_blank" rel="noreferrer">{{ link.label }}</a>
              {% endfor %}
            </div>
          </div>
        </details>
        {% endfor %}
      </div>
    </div>
  </details>
</section>

<section id="resources-gists" class="section-block">
  <details class="card card-wide foldable">
    <summary class="foldable-summary"><h2>Gist documents</h2></summary>
    <div class="foldable-body">
      <p class="lead">{{ site.data.resources.gists.lead }}</p>
      <div class="mini-links">
        {% for link in site.data.resources.gists.links %}
        <a href="{{ link.url }}" target="_blank" rel="noreferrer">{{ link.label }}</a>
        {% endfor %}
      </div>
    </div>
  </details>
</section>

<section id="resources-video-tutorials" class="section-block">
  <details class="card card-wide foldable">
    <summary class="foldable-summary"><h2>Video tutorials</h2></summary>
    <div class="foldable-body">
      <div class="grid three-up">
        {% for item in site.data.resources.tutorials.items %}
        <details class="card foldable">
          <summary class="foldable-summary"><h3>{{ item.title }}</h3></summary>
          <div class="foldable-body">
            {% if item.links %}
            <ul class="detail-list">
              {% for link in item.links %}
              <li><a class="text-link" href="{{ link.url }}" target="_blank" rel="noreferrer">{{ link.label }}</a></li>
              {% endfor %}
            </ul>
            {% endif %}
            {% if item.text %}<p>{{ item.text }}</p>{% endif %}
          </div>
        </details>
        {% endfor %}
      </div>
    </div>
  </details>
</section>

<section id="resources-members-only" class="section-block">
  <details class="card card-wide foldable">
    <summary class="foldable-summary"><h2>Members only</h2></summary>
    <div class="foldable-body">
      <p class="lead">{{ site.data.resources.members_only.lead }}</p>
      <div class="grid three-up">
        {% for card in site.data.resources.members_only.cards %}
        <details class="card foldable">
          <summary class="foldable-summary"><h3>{{ card.title }}</h3></summary>
          <div class="foldable-body">
            {% if card.text %}<p>{{ card.text }}</p>{% endif %}
            {% if card.links %}
            <div class="mini-links">
              {% for link in card.links %}
              <a href="{{ link.url }}" target="_blank" rel="noreferrer">{{ link.label }}</a>
              {% endfor %}
            </div>
            {% endif %}
          </div>
        </details>
        {% endfor %}
      </div>
    </div>
  </details>
</section>

<section id="resources-gallery" class="section-block">
  <details class="card card-wide foldable">
    <summary class="foldable-summary"><h2>Gallery</h2></summary>
    <div class="foldable-body">
      <div class="grid two-up resource-gallery-grid">
        {% for item in site.data.resources.gallery.items %}
        <details class="card card-wide foldable">
          <summary class="foldable-summary"><h3>{{ item.title }}</h3></summary>
          <div class="foldable-body">
            <div class="resource-embed-frame">
              <iframe src="{{ item.iframe_src }}" title="{{ item.iframe_title }}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
            </div>
            <div class="mini-links">
              <a href="{{ item.open_link.url }}" target="_blank" rel="noreferrer">{{ item.open_link.label }}</a>
            </div>
          </div>
        </details>
        {% endfor %}
      </div>
    </div>
  </details>
</section>

<section id="resources-links" class="section-block">
  <details class="card card-wide foldable">
    <summary class="foldable-summary"><h2>Links</h2></summary>
    <div class="foldable-body">
      <details class="subpage-item foldable">
        <summary class="foldable-summary"><h3>Resources link</h3></summary>
        <div class="foldable-body mini-links link-stack">
          {% for link in site.data.resources.links.resources_links %}
          <a href="{{ link.url }}"{% if link.url contains 'http' %} target="_blank" rel="noreferrer"{% endif %}>{{ link.label }}</a>
          {% endfor %}
        </div>
      </details>
    </div>
  </details>
</section>
