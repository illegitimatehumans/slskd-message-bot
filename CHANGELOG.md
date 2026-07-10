# Changelog

All notable changes to this project will be documented in this file.

## v1.1.0

### Fixed

- Updated private messaging to use the documented Conversations API.
- Replaced the legacy messaging endpoint with:
  `POST /api/v0/conversations/{username}`
- Improved message delivery logging.

### Documentation

- Added slskd compatibility notes.
- Documented the required Conversations API endpoint.
