# Changelog

All notable changes to this project will be documented in this file.

## v1.3.0

### Added

- Warning message templates now support:
  - `{username}`
  - `{files}`
  - `{directories}`
  - `{min_files}`
  - `{min_directories}`

### Improved

- Leecher thresholds are now read directly from the live slskd API (`/api/v0/options`).
- Warning messages automatically reflect the current slskd configuration.
- Removed duplicate threshold configuration for message generation.

### Fixed

- Updated messaging to use the current Conversations API:
  `POST /api/v0/conversations/{username}`
- Improved compatibility with current versions of slskd.
- Improved logging and warning delivery.

---

## v1.2.0

### Added

- Customizable warning message templates.
- Support for dynamic placeholders:
  - `{username}`
  - `{files}`
  - `{directories}`
  - `{min_files}`
  - `{min_directories}`

### Improved

- Automatically substitutes placeholder values before sending messages.
- Added a project changelog.
- Updated the example warning message template.

---

## v1.1.0

### Fixed

- Updated private messaging to use the documented Conversations API.
- Replaced the legacy messaging endpoint with:
  `POST /api/v0/conversations/{username}`
- Improved message delivery logging.

### Documentation

- Added slskd compatibility notes.
- Documented the required Conversations API endpoint.
