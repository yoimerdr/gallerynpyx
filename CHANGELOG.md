# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 2.0.0 - 2026-03-28

This release introduces breaking API changes around gallery-scoped handlers,
configurations, and some action access patterns. The version was bumped to
`2.0.0` because code that relied on singleton-only access is no longer fully
compatible with the new multi-gallery model.

### Added

- New gallery system with local handlers and local configurations.
- Managers for shared and named gallery handlers/configurations, allowing access from anywhere.

### Changed

- Existing screens were adapted to work with whichever handler is passed to them.
- Animation statement extraction was improved.
- Predict support was added for some actions.

### Fixed

- Unexpected calculations under Python 2.7.
- Unexpected calculations caused by early Ren'Py config imports.

### Removed

- Assumptions that some classes, including some actions, are always accessed as singletons.

## 1.0.0 - 2025-05-08

Initial public release.

### Added

- Strict resources.
- Size compatibility for any resource.
- Improved slide labeling.
- Style-based configuration.
- Screen customization.
- Python 2.7 and 3.x support.
- Modularized library.

