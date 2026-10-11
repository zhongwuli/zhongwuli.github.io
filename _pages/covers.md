---
layout: page
title: Covers
permalink: /covers/
description:
nav: true
nav_order: 4
---

A collection of covers associated with my published research. 

<div class="row row-cols-2 row-cols-md-3 g-3">
{% for cover in site.data.covers %}
  {% assign cover_path = '/assets/img/book_covers/' | append: cover.file %}
  {% assign cover_file = site.static_files | where: "path", cover_path | first %}
  <div class="col mb-4">
    {% if cover_file %}
      <img src="{{ cover_path | relative_url }}" alt="{{ cover.title | escape }} cover, {{ cover.year }}" class="img-fluid rounded" loading="lazy">
    {% endif %}
    <p class="mt-2"><strong>{{ cover.title }}</strong> · {{ cover.year }}</p>
  </div>
{% endfor %}
</div>
