# Website editing guide

The website is powered by [al-folio](https://github.com/alshedivat/al-folio) and GitHub Pages.

## Where to edit

- Personal biography and research interests: `_pages/about.md`
- Research descriptions: `_pages/research.md`
- Selected publications: `_pages/publications.md`
- CV entries: `_data/cv.yml`
- Social links: `_data/socials.yml`
- Journal cover names and ordering: `_data/covers.yml`
- Journal cover gallery layout: `_pages/covers.md`

## Journal covers

Upload each cover image into `assets/img/book_covers/`. Filenames must match `_data/covers.yml`. The gallery automatically shows images that are present and omits missing-image placeholders.

The homepage shows covers with `featured: true`. All entries appear on the Journal Covers page.

## Profile photo

Upload a portrait as `assets/img/prof_pic.jpg`. In `_pages/about.md`, the profile is configured as `image: prof_pic.jpg` to display it.

## Publishing

Commit changes to `main` or merge a Pull Request. The existing Deploy site workflow builds the `gh-pages` branch. The Pages source should be **Deploy from a branch → gh-pages → /(root)**.

Do not upload sensitive personal information or unpublished work without checking permissions.

## New site sections

- People (biography, appointments, education, future team members): `_pages/profiles.md`
- Conferences (selected talks): `_pages/conferences.md`
- Professional Activities (organization, awards, editorial/review service): `_pages/professional-activities.md`
- Life & Moments (personal photo album): `_pages/moments.md`; upload images into `assets/img/moments/`
- Journal Covers (only on its own page): `_pages/covers.md` and `_data/covers.yml`
- The CV page is hidden from the navigation; background is kept on People instead.
