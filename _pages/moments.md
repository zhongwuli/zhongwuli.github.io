---
layout: page
title: Moments
permalink: /moments/
description: Travel, gatherings, photographs and moments beyond the laboratory.
nav: true
nav_order: 7
---

Research is an important part of my life, but so are the places I visit and the people I meet along the way. This page is a personal photo journal for **travel, gatherings, daily life and memories beyond research**.

## Photo journal

{% assign moments = site.static_files | where_exp: "file", "file.path contains '/assets/img/moments/'" %}
{% assign photo_count = 0 %}
<div class="row row-cols-2 row-cols-md-3 g-3">
{% for photo in moments %}
  {% assign suffix = photo.extname | downcase %}
  {% if suffix == '.jpg' or suffix == '.jpeg' or suffix == '.png' or suffix == '.webp' %}
    {% assign photo_count = photo_count | plus: 1 %}
    <div class="col mb-3"><a href="{{ photo.path | relative_url }}"><img src="{{ photo.path | relative_url }}" class="img-fluid rounded" alt="Personal photo {{ photo_count }}" loading="lazy"></a></div>
  {% endif %}
{% endfor %}
</div>

{% if photo_count == 0 %}
*Photos are coming soon.* I will share moments from travels, conferences, dinners and everyday life here.
{% endif %}

To add photos, upload JPG, PNG or WebP files into `assets/img/moments/`. They will appear here automatically after the website is rebuilt.
