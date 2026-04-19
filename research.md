---
layout: default
title: Research
description: Research areas for the Dan Shim Lab.
nav_key: research
permalink: /research.html
---
<section class="page-hero profile-hero research-hero">
  <div class="profile-hero-copy">
    <h1>{{ site.data.research.hero.title }}</h1>
    <p class="lead">
      {{ site.data.research.hero.lead }}
    </p>
    <nav class="section-nav" aria-label="Research section">
      <a class="is-active" href="research.html">Overview</a>
      <a href="#research-news">News</a>
      <a href="#scientific-topics">Topics</a>
      <a href="#research-methods">Methods</a>
      <a href="#research-links">Links</a>
    </nav>
  </div>
  <div class="profile-hero-photo research-hero-photo">
    <img
      class="hero-title-image research-hero-image"
      src="{{ site.data.research.hero.image }}"
      alt="{{ site.data.research.hero.image_alt }}"
    >
  </div>
</section>

<section id="research-news" class="section-block">
  <details class="card card-wide foldable" open>
    <summary class="foldable-summary">
      <h2>Our research in news</h2>
    </summary>
    <div class="foldable-body news-stack">
      <article class="subpage-item">
        <h3>Latest</h3>
        {% for item in site.data.research.news.latest limit: 2 %}
        <p class="inline-news-item">
          <span class="time-label">{{ item.date }}</span>
          <span>{{ item.text }}</span>
          <a class="text-link" href="{{ item.source_url }}" target="_blank" rel="noreferrer">{{ item.source_label }}</a>
        </p>
        {% endfor %}
      </article>
      <details class="subpage-item foldable">
        <summary class="foldable-summary">
          <h3>Earlier news</h3>
        </summary>
        <div class="foldable-body news-stack">
          {% for item in site.data.research.news.earlier %}
          <article class="subpage-item">
            <h3>{{ item.year }}</h3>
            <p>
              {{ item.text }}
              {% for link in item.links %}
              <a class="text-link" href="{{ link.url }}" target="_blank" rel="noreferrer">{{ link.label }}</a>{% unless forloop.last %},{% endunless %}
              {% endfor %}
            </p>
          </article>
          {% endfor %}
        </div>
      </details>
    </div>
  </details>
</section>

<section id="scientific-topics" class="section-block">
  <details class="card card-wide foldable">
    <summary class="foldable-summary">
      <h2>Scientific topics</h2>
    </summary>
    <div class="foldable-body">
      <div class="topic-cluster">
        {% for topic in site.data.research.topics %}
        <details class="subpage-item foldable">
          <summary class="foldable-summary">
            <h3>{{ topic.title }}</h3>
          </summary>
          <div class="foldable-body">
            {{ topic.content | markdownify }}
          </div>
        </details>
        {% endfor %}
      </div>
    </div>
  </details>
</section>

<section id="research-methods" class="section-block">
  <details class="card card-wide foldable">
    <summary class="foldable-summary">
      <h2>Methods</h2>
    </summary>
    <div class="foldable-body">
      <div class="topic-cluster">
        {% for method in site.data.research.methods %}
        <details class="subpage-item foldable">
          <summary class="foldable-summary">
            <h3>{{ method.title }}</h3>
          </summary>
          <div class="foldable-body">
            {{ method.content | markdownify }}
          </div>
        </details>
        {% endfor %}
      </div>
    </div>
  </details>
</section>

<section id="research-links" class="section-block">
  <details class="card card-wide foldable">
    <summary class="foldable-summary">
      <h2>Links</h2>
    </summary>
    <div class="foldable-body">
      <details class="subpage-item foldable">
        <summary class="foldable-summary">
          <h3>Research links</h3>
        </summary>
        <div class="foldable-body mini-links link-stack">
          {% for link in site.data.research.links.research_links %}
          <a href="{{ link.url }}" target="_blank" rel="noreferrer">{{ link.label }}</a>
          {% endfor %}
        </div>
      </details>
      <details class="subpage-item foldable">
        <summary class="foldable-summary">
          <h3>Support</h3>
        </summary>
        <div class="foldable-body">
          <img
            class="funding-logos"
            src="{{ site.data.research.links.support.image }}"
            alt="{{ site.data.research.links.support.image_alt }}"
          >
        </div>
      </details>
    </div>
  </details>
</section>
