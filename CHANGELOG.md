# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog and this project adheres to Semantic Versioning.

---

## [1.3.2] - 2026-07-12

### Added

- Configurable browse retry timing using `BROWSE_RETRY_DELAYS`.
- Support for custom retry schedules such as `2,5,10`.
- Automatic retry attempt count based on the configured delay list.

### Changed

- Browse retry behavior is now fully configurable through the `.env` file.
- Improved retry logging to reflect configured retry attempts and delays.
- Updated the README, `.env.example`, and roadmap documentation.

### Removed

- Removed hardcoded browse retry count.
- Removed hardcoded browse retry delay.

---

## [1.3.1] - 2026-07-12

### Added

- Automatic retry logic for failed user browse requests.
- Up to three browse attempts before marking a user as `UNKNOWN`.
- Detailed browse attempt logging.

### Improved

- More reliable evaluation of first-time uploaders.
- Reduced false `UNKNOWN` results caused by temporary browse failures.

### Fixed

- Temporary browse failures no longer immediately abort user evaluation.

---

## [1.3.0] - 2026-07-11

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

- Updated messaging to use the current Conversations API (`POST /api/v0/conversations/{username}`).
- Improved compatibility with current versions of slskd.
- Improved logging and warning delivery.

---

## [1.2.0] - 2026-07-11

### Added

- Initial public release.
- Automatic upload monitoring.
- Share threshold evaluation.
- One-time warning messages.
- Docker support.
- SQLite database for warning history.
- Configurable message templates.
