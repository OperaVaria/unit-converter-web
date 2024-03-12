# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.3.0] - 2024.03.12

## Added

- SEO files (robots.txt, sitemap.xml).
- humans.txt.

## Changed

- HTML restructured for accessibility and SEO.
- Simple footer for mobile screens instead of buttons.
- Smaller header on desktop.
- Slow loading "current year" JS swapped for Jinja/Python variable.
- CSS tweaks.

### Fixed

- About page Flask extension lists' display problems.
- Hyphenation problems with Hungarian texts.
- Code formating.
- Typos.

## [1.2.0] - 2024.03.09

## Added

- Implemented minification with Flask-Minify.
- Implemented HTTP security headers with Flask-Talisman.
- Unit systems added: Pressburg, Eger, Kassa, Nagyszombat liquid volume units.

### Changed

- Eliminated inline JavaScript.
- Updated docs and about.

### Fixed

- Typos in database.
- Code formatting.
- Fixed further soft refresh imperfections.
- All links open in new tab.

## [1.1.1] - 2024.03.07

## Added

- Choices.js css added locally for easier styling.
- Choices.js licence file attached.

### Changed

- Choices.js menu further customized, simple animation added.

### Fixed

- Some comments clarified.

## [1.1.0] - 2024.03.06

### Added

- Choices.js select menus implemented.
- New unit systems: Austrian fortification area, length, Austro-Hungarian sailor's.

### Changed

- New favicon.
- Style tweaks.
- Spacing tweaks.
- Docs updated.

### Fixed

- Database typos.

## [1.0.1] - 2024.02.25

### Added

- Html lang changes with locale.
- Warning at the end of "settings.py" if file run by accident.

### Changed

- Revamped about page and source list.
- Amended README.md.
- Version number updates automatically on the index page.

### Fixed

- Small adjustments to the database.
- Safeguard if "request.accept_languages.best_match()" fails.
- CSV files formatted to properly display on GitHub.
- Minor aesthetic tweaks in HTML and CSS files.
- Better look on smaller mobile screens.

## [1.0.0] - 2024.02.24

### Added

- Initial "release".
