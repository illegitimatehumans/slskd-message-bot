# slskd-message-bot Roadmap

This roadmap outlines the planned direction of **slskd-message-bot**.

The project follows **Semantic Versioning (SemVer)**. Priorities may evolve based on community feedback and future changes to the **slskd** API.

---

# v1.3.x — Uploader Evaluation
**Status:** ✅ Complete

Focused on making uploader evaluation faster, smarter, and more reliable.

## Completed

- [x] Immediate evaluation of new uploaders
- [x] Automatic browse retries
- [x] Configurable browse retry backoff
- [x] Smart browse caching
- [x] Reduced unnecessary browse requests
- [x] Improved browse logging

---

# v1.4.x — Dynamic slskd Integration
**Status:** ✅ Complete

Focused on eliminating duplicated configuration by reading the active server configuration directly from slskd.

## Completed

- [x] Live leecher threshold synchronization
- [x] Dynamic transfer group synchronization
- [x] Automatic transfer limit placeholders
- [x] Dynamic message generation
- [x] Runtime message template creation
- [x] Improved warning logging
- [x] Local timezone support
- [x] Run container as a configurable non-root user (`PUID` / `PGID`)
- [x] Docker hardening
- [x] GitHub Container Registry releases

---

# v1.5.0 — Statistics & Compliance Tracking

The next major milestone focuses on measuring how effective your sharing policy actually is.

## Statistics

- [ ] Users evaluated
- [ ] GOOD users
- [ ] LEECHERS detected
- [ ] UNKNOWN evaluations
- [ ] Browse failures
- [ ] Browse success rate
- [ ] Average browse duration
- [ ] Total warnings sent
- [ ] Duplicate warnings skipped
- [ ] Session cache hits
- [ ] Database cache hits

## Compliance Tracking

One of the primary goals of the bot is encouraging users to share.

Future releases will measure whether users become compliant after receiving a warning.

Example:

```
Users Evaluated:          2,384

GOOD Users:               1,947

LEECHERS:                   437

Warnings Sent:              412

Users Became Compliant:     156

Compliance Rate:          37.9%

Average Time to Comply:   3.2 days
```

### Planned Metrics

- [ ] Total warnings sent
- [ ] Users who became compliant
- [ ] Compliance rate
- [ ] Average time until compliance
- [ ] Historical trends
- [ ] Warning effectiveness

---

# Configuration

Future configuration improvements.

- [ ] Move whitelist to `data/whitelist.txt`
- [ ] Configurable blacklist file
- [ ] Runtime configuration validation
- [ ] Live configuration reload

---

# Logging

Improve diagnostics and troubleshooting.

- [ ] Debug logging mode
- [ ] Log rotation support
- [ ] Performance timing logs
- [ ] Statistics summary output

---

# Message Templates

## Current Placeholders

- [x] `{username}`
- [x] `{files}`
- [x] `{directories}`
- [x] `{min_files}`
- [x] `{min_directories}`
- [x] `{upload_slots}`
- [x] `{speed_limit}`
- [x] `{queue_files}`
- [x] `{queue_size}`
- [x] `{daily_files}`
- [x] `{daily_size}`
- [x] `{daily_failures}`
- [x] `{weekly_files}`
- [x] `{weekly_size}`
- [x] `{weekly_failures}`

## Planned Placeholders

- [ ] `{server_name}`
- [ ] `{warning_count}`
- [ ] `{date}`

---

# Discord Integration

Optional Discord notifications for server operators.

- [ ] Warning notifications
- [ ] User became compliant notification
- [ ] Daily statistics summary
- [ ] Rich Discord embeds

---

# Administration

Administrative utilities.

- [ ] Manual user recheck
- [ ] Clear warning history
- [ ] Export database
- [ ] Import database
- [ ] Search users

---

# slskd Integration

Future improvements based on new slskd features.

- [ ] Cancel uploads immediately after a leecher is detected (if supported by the API)
- [ ] Automatic thank-you message when a warned user becomes compliant
- [ ] Support future slskd API changes

---

# v2.x — Optional Dashboard

## Dashboard

- [ ] Live activity monitor
- [ ] User browser
- [ ] Compliance dashboard
- [ ] Historical statistics
- [ ] Configuration editor

## REST API

- [ ] Statistics endpoint
- [ ] User lookup
- [ ] Warning history
- [ ] Manual recheck endpoint

## Integrations

- [ ] Discord
- [ ] Grafana
- [ ] Prometheus
- [ ] Home Assistant

---

# Future Vision

The long-term goal of **slskd-message-bot** is to become the companion application for managing sharing policies on **slskd** servers.

The project is built around one core principle:

> **Avoid duplicated configuration whenever possible.**

Whenever practical, the bot should automatically read configuration directly from **slskd** rather than requiring administrators to maintain the same settings in multiple places.

Future releases will continue focusing on:

- Encouraging healthy sharing habits.
- Providing friendly communication with users.
- Reducing administrative overhead.
- Measuring policy effectiveness.
- Providing meaningful statistics.
- Remaining lightweight.
- Remaining Docker-first.
- Maintaining compatibility with future versions of **slskd**.

---

# Guiding Principles

The goal of this project is **not** to punish users.

The goal is to encourage sharing by:

- Explaining server policies.
- Providing clear guidance.
- Encouraging users to become compliant.
- Reducing confusion around transfer restrictions.

The project should remain:

- Lightweight
- Docker-first
- Easy to configure
- Secure by default
- Reliable
- Compatible with current and future versions of **slskd**
