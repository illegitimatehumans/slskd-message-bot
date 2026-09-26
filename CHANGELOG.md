# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog and this project adheres to Semantic Versioning.

---

## v1.5.0

### Added

- Compliance tracking for users who become compliant after receiving a warning.
- Compliance statistics including:
  - Unique warned users.
  - Unique compliant users.
  - Compliance rate.
  - Average time to compliance.
- Statistics summary output showing:
  - Users evaluated.
  - GOOD users.
  - LEECHERS detected.
  - UNKNOWN evaluations.
  - Browse successes.
  - Browse failures.
  - Average browse duration.
  - Warnings sent.
  - Session cache hits.
  - Database cache hits.
- Compliance achievement logging when a warned user becomes `GOOD`.

### Changed

- Reduced the default `LEECHER_RECHECK_MINUTES` interval from 60 minutes to 20 minutes.
- Compliance statistics are no longer printed every monitoring cycle and are instead logged at a reduced frequency.
- Updated `README.md` to document the 20-minute leecher recheck interval.
- Updated `message.txt.example` to reflect the current message template.
- Updated the upload evaluation screenshot.

### Improved

- Compliance tracking now records the time between a warning and the user's subsequent compliant evaluation.
- Statistics now distinguish unique warned users from unique compliant users.
- Added protection against recording the same compliance event multiple times for the same warning.

---

## v1.4.2

### Added

- Automatic synchronization of transfer group limits from slskd.
- New message placeholders:
  - `{upload_slots}`
  - `{speed_limit}`
  - `{queue_files}`
  - `{queue_size}`
  - `{daily_files}`
  - `{daily_size}`
  - `{daily_failures}`
  - `{weekly_files}`
  - `{weekly_size}`
  - `{weekly_failures}`

### Changed

- Warning messages now reflect the active slskd transfer group instead of requiring manually maintained values.

## [1.4.1] - 2026-07-13

### Added

- Automated Docker image publishing with GitHub Actions.
- GitHub Container Registry (GHCR) support.
- Production Docker Compose configuration using published container images.
- Development Docker Compose configuration for local image builds.

### Changed

- Split Docker Compose into production and development configurations.
- Updated deployment workflow to support image-based installs from GHCR.
- Improved browse retry logging to reduce unnecessary log messages.

### Fixed

- Corrected retry logic to properly retry failed browse requests before returning `UNKNOWN`.
- Fixed variable name typos affecting the browse retry path.
- Corrected README screenshot paths and Docker documentation.

## [1.3.3] - 2026-07-12

### Added

- Smart browse caching.
- Separate cache lifetimes for GOOD and LEECHER users.
- `GOOD_RECHECK_MINUTES` configuration.
- `LEECHER_RECHECK_MINUTES` configuration.

### Improved

- Reduced unnecessary browse requests.
- Status-aware cache expiration.

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
