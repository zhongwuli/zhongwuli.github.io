---
layout: about
title: about
permalink: /
subtitle: Postdoctoral Scientist, EIT Oxford · Visiting Researcher, University of Oxford
profile:
  align: right
  image:
  image_circular: false
  more_info: >
    <p>Materials & Devices for Life Sciences</p>
    <p>Oxford, United Kingdom</p>
selected_papers: false
social: true
announcements:
  enabled: false
latest_posts:
  enabled: false
---

I am **Zhongwu Li**, a **Postdoctoral Scientist** in **Materials & Devices for Life Sciences** at the **Ellison Institute of Technology Oxford (EIT Oxford)**, working with **Professor Hagan Bayley**. I am also a **Visiting Researcher** in the **Department of Chemistry, University of Oxford**.

My research lies at the intersection of **nanofluidics, bioiontronics, and neuromorphic ionic computing**. I investigate how water and ions behave under nanoscale confinement and translate these fundamental insights into biomimetic channels, soft ionic devices, and bioinspired systems for sensing and information processing.

Before joining EIT Oxford, I was a **Postdoctoral Researcher** in the **Materials Science Division at Lawrence Livermore National Laboratory (LLNL)** (April 2023–May 2026), working with **Dr. Aleksandr Noy**. During this appointment, I was also an **Affiliate Visiting Researcher** at the **Molecular Foundry, Lawrence Berkeley National Laboratory (LBNL)** (March 2025–May 2026).

Previously, I was an **Assistant Professor** at the **China University of Mining and Technology** (2021–2023). I received my doctorate in **Mechanical Engineering from Southeast University** (2021), including joint doctoral research training at LLNL (2018–2020).

## Research interests

**Nanofluidics.** Development of biomimetic nanochannels and experimental and computational studies of nanoscale transport, with an emphasis on interfacial, confinement, and quantum effects on the motion of water and ions.

**Bioiontronics.** Development of 3D droplet interface bilayer networks, engineered protein nanopores, and hydrogel- and ion-based memristors for bioinspired information processing and biological interfaces.

**Water, Energy & AI.** Translation of nanofluidic and bioiontronic principles into salinity-gradient energy conversion, molecular separation, intelligent nanopore sensing, and neuromorphic ionic computing.

## Selected journal covers

<div class="row row-cols-2 row-cols-md-3 g-3 mb-4">
{% assign featured_covers = site.data.covers | where: "featured", true %}
{% for cover in featured_covers %}
  {% assign cover_path = '/assets/img/covers/' | append: cover.file %}
  {% assign cover_file = site.static_files | where: "path", cover_path | first %}
  <div class="col mb-3">
    {% if cover_file %}
      <img src="{{ cover_path | relative_url }}" alt="{{ cover.title | escape }} journal cover" class="img-fluid rounded" loading="lazy">
    {% endif %}
    <div class="mt-1"><strong>{{ cover.title }}</strong> ({{ cover.year }})</div>
  </div>
{% endfor %}
</div>

[View all journal covers](/covers/) · [Selected publications](/publications/) · [Full academic CV](/cv/)

## Research journey

My long-term aim is to bridge **fundamental nanofluidic physics** and **functional soft-matter devices**, connecting molecular transport phenomena with technologies for energy, water, intelligent sensing, and biointerfaces. My work has progressed from understanding transport in carbon-based nanoconfinement to building adaptive ionic networks for neuromorphic computing.

For current publications and updates, visit my [Google Scholar](https://scholar.google.com/citations?user=8_mITz8AAAAJ) or [ORCID](https://orcid.org/0000-0001-8825-6307) profile.
