# slskd-message-bot Roadmap

This roadmap outlines planned improvements and future ideas for **slskd-message-bot**.

The project follows semantic versioning, but priorities may change based on user feedback and changes to the slskd API.

---

# v1.3.x

## Improve uploader evaluation

- [x] Evaluate first-time uploaders immediately
- [x] Retry browse requests after short delays when they fail
- [ ] Configurable retry/backoff timing
- [ ] Smart browse caching
- [ ] Reduce unnecessary browse requests

## Configuration

- [ ] Move whitelist to `data/whitelist.txt`
- [ ] Configurable blacklist file
- [ ] Additional runtime configuration options

## Logging
- [x] Imporved browse attempt logging
- [ ] Better warning summaries
- [ ] Debug logging mode
- [ ] Log rotation support

---

# v1.4.0

## Statistics

- [ ] Users evaluated
- [ ] GOOD users
- [ ] LEECHERS detected
- [ ] Browse failures
- [ ] Warnings sent
- [ ] Average browse time

## Compliance Tracking

One of the primary goals of the bot is encouraging users to share.

Future releases will track whether warned users later become compliant.

Example statistics:

```
Users Evaluated:          2,384

GOOD Users:               1,947

LEECHERS:                   437

Warnings Sent:              412

Users Became Compliant:     156

Compliance Rate:          37.9%

Average Time to Comply:   3.2 days
```

Planned metrics:

- [ ] Total warnings sent
- [ ] Users who became compliant
- [ ] Compliance rate
- [ ] Average time until compliance
- [ ] Historical trends
- [ ] Warning effectiveness
---

# Discord Integration

- [ ] Warning notifications
- [ ] User became compliant notification
- [ ] Daily statistics summary
- [ ] Rich Discord embeds

---

# Message Templates

## Current placeholders

- [x] `{username}`
- [x] `{files}`
- [x] `{directories}`
- [x] `{min_files}`
- [x] `{min_directories}`

## Planned placeholders

- [ ] `{speed_limit}`
- [ ] `{daily_limit}`
- [ ] `{weekly_limit}`
- [ ] `{server_name}`
- [ ] `{warning_count}`
- [ ] `{date}`

---

# Dashboard

Possible future web dashboard.

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

# Administration

- [ ] Manual user recheck
- [ ] Clear warning history
- [ ] Export database
- [ ] Import database
- [ ] Search users

---

# slskd Integration

Potential improvements:

- [ ] Cancel uploads immediately after a leecher is detected (if supported by the slskd API)
- [ ] Automatic thank-you message when a warned user becomes compliant
- [x] Automatic threshold synchronization from the slskd API
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

- [ ] Grafana
- [ ] Prometheus
- [ ] Home Assistant
- [ ] Discord

---
# Future Vision

The long-term goal is to make **slskd-message-bot** the companion application for slskd sharing policy management.

Future releases will focus on:

- Encouraging healthy sharing
- Providing meaningful analytics
- Integrating with existing self-hosted tools
- Remaining lightweight and easy to deploy

# Guiding Principles

The goal of this project is **not** to punish users.

The goal is to encourage sharing by:

- Explaining server policies.
- Providing clear guidance.
- Recognizing users who become compliant.
- Reducing confusion around transfer restrictions.

The bot should remain lightweight, easy to configure, and fully compatible with current versions of **slskd**.
