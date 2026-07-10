# Changelog

All notable changes to this project will be documented in this file.

# v1.2.0

## Added

- Customizable warning message templates.
- Support for dynamic placeholders:
  - `{username}`
  - `{files}`
  - `{directories}`
  - `{min_files}`
  - `{min_directories}`

## Improved

- Automatically substitutes placeholder values before sending messages.
- Added a project changelog.
- Updated the example warning message template.


## v1.1.0

### Fixed

- Updated private messaging to use the documented Conversations API.
- Replaced the legacy messaging endpoint with:
  `POST /api/v0/conversations/{username}`
- Improved message delivery logging.

### Documentation

- Added slskd compatibility notes.
- Documented the required Conversations API endpoint.

## Roadmap

- [x] One-time warning messages
- [x] SQLite persistence
- [x] Configurable message templates
- [ ] Discord webhook notifications
- [ ] Multiple warning templates
- [ ] Placeholder for upload filename
- [ ] Automatic stale user cleanup
- [ ] Unit tests
