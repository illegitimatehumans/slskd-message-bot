# slskd-message-bot Roadmap

This roadmap outlines planned improvements and the long-term direction of **slskd-message-bot**.

The project follows **Semantic Versioning (SemVer)**, but priorities may change based on community feedback and future changes to the **slskd** API.

---

# v1.3.x — Uploader Evaluation
**Status:** ✅ Complete

The focus of the v1.3.x series was making uploader evaluation faster, smarter, and more reliable.

## Completed

- [x] Evaluate first-time uploaders immediately
- [x] Retry failed browse requests automatically
- [x] Configurable browse retry backoff
- [x] Smart browse caching
- [x] Reduce unnecessary browse requests
- [x] Dynamic threshold synchronization from the slskd API
- [x] Improved browse logging

---

# v1.4.0 — Statistics & Compliance Tracking

The next major milestone focuses on measuring how effective your sharing policy actually is.

## Statistics

- [ ] Users evaluated
- [ ] GOOD users
- [ ] LEECHERS detected
- [ ] Browse failures
- [ ] Warnings sent
- [ ] Browse success rate
- [ ] Average browse time

## Compliance Tracking

One of the primary goals of the bot is encouraging users to share.

Future releases will measure whether users improve after receiving a warning.

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
- [ ] Additional runtime configuration options
- [ ] Runtime configuration validation

---

# Logging

Improve diagnostics and troubleshooting.

- [ ] Better warning summaries
- [ ] Debug logging mode
- [ ] Log rotation support
- [ ] Performance timing logs

---

# Message Templates

## Current Placeholders

- [x] `{username}`
- [x] `{files}`
- [x] `{directories}`
- [x] `{min_files}`
- [x] `{min_directories}`

## Planned Placeholders

- [ ] `{speed_limit}`
- [ ] `{daily_limit}`
- [ ] `{weekly_limit}`
- [ ] `{server_name}`
- [ ] `{warning_count}`
- [ ] `{date}`

---

# Web Dashboard

An optional dashboard for monitoring server activity.

## Users

- [ ] GOOD
- [ ] LEECHER
- [ ] UNKNOWN
- [ ] WARNED
- [ ] COMPLIANT

## Statistics

- [ ] Charts
- [ ] Compliance graphs
- [ ] Browse failures
- [ ] Historical activity
- [ ] Upload activity timeline

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

- [ ] Cancel uploads immediately after a leecher is detected (if supported by the slskd API)
- [ ] Automatic thank-you message when a warned user becomes compliant
- [ ] Support future slskd API changes

---

# Long-Term Goals

## Web UI

- [ ] Dashboard
- [ ] User browser
- [ ] Configuration editor
- [ ] Live activity monitor

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

Future releases will focus on:

- Encouraging healthy sharing habits.
- Providing clear, friendly communication with users.
- Reducing administrative overhead.
- Measuring the effectiveness of sharing policies.
- Providing meaningful statistics and insights.
- Integrating with existing self-hosted tools.
- Remaining lightweight, easy to configure, and Docker-first.
- Maintaining compatibility with future versions of **slskd**.

---

# Guiding Principles

The goal of this project is **not** to punish users.

The goal is to encourage sharing by:

- Explaining server policies.
- Providing clear guidance.
- Recognizing users who become compliant.
- Reducing confusion around transfer restrictions.

The bot should remain:

- Lightweight
- Easy to configure
- Docker-first
- Reliable
- Fully compatible with current and future versions of **slskd**
