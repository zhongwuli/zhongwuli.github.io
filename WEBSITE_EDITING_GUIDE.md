# Website editing guide

The website is powered by [al-folio](https://github.com/alshedivat/al-folio) and GitHub Pages.

## Where to edit

- Personal biography and research interests: `_pages/about.md`
- Research descriptions: `_pages/projects.md`
- Selected publications: `_pages/publications.md`
- CV entries: `_data/cv.yml`
- Social links: `_data/socials.yml`
- Journal cover names and ordering: `_data/covers.yml`
- Journal cover gallery layout: `_pages/covers.md`

## Journal covers

Upload each cover image into `assets/img/covers/`. Filenames must match `_data/covers.yml`. The gallery automatically shows images that are present and omits missing-image placeholders.

The homepage shows covers with `featured: true`. All entries appear on the Journal Covers page.

## Profile photo

Upload a portrait as `assets/img/prof_pic.jpg`. In `_pages/about.md`, change the profile configuration from `image:` to `image: prof_pic.jpg` to display it.

## Publishing

Commit changes to `main` or merge a Pull Request. The existing Deploy site workflow builds the `gh-pages` branch. The Pages source should be **Deploy from a branch → gh-pages → /(root)**.

Do not upload sensitive personal information or unpublished work without checking permissions.
