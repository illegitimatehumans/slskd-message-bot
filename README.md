# slskd-message-bot

An automated sharing policy bot for slskd that monitors active uploads, evaluates users against configurable sharing thresholds, and sends a one-time customizable private message to users who don't meet your server's sharing policy.

Designed to complement slskd's built-in transfer groups by explaining *why* a user's downloads may be limited.

## Screenshots

Coming soon.

## Why?

slskd can already identify users with low share counts and apply different transfer limits through transfer groups. What it doesn't do is explain those restrictions to the user.

This bot fills that gap by automatically sending a friendly one-time message that explains your server's sharing policy. Instead of silently throttling users, the bot tells them what your server expects and how to resolve the issue.

## Features

- Automatic upload monitoring
- Configurable grace period
- Remote share browsing
- Share threshold evaluation
- One-time private messages
- Customizable message templates
- Dynamic placeholders
- Whitelist support
- SQLite database to prevent duplicate messages
- Docker support

## Requirements

- Docker
- Docker Compose
- slskd 0.25 or newer
- Python 3.13

## slskd Compatibility

This bot uses the Conversations API available in current versions of slskd.

Private messages are sent using:

POST /api/v0/conversations/{username}

If you're running an older version of slskd, check the built-in Swagger documentation (`/swagger`) to verify the messaging endpoint before using the bot.

## Installation

## First Run

On first startup the bot automatically creates:

```
data/message.txt
```

from:

```
message.txt.example
```

You can edit `data/message.txt` at any time without rebuilding the container.

Clone the repository:

```bash
git clone https://github.com/illegitimatehumans/slskd-bot.git
cd slskd-bot
```
Copy the example environment file:

```bash
cp .env.example .env
```

Edit `.env` with your own settings.

On first startup, the bot automatically creates `data/message.txt` from `message.txt.example` if it doesn't already exist. You can edit `data/message.txt` at any time without rebuilding the container.

Edit both files as needed before starting the bot.

Edit `.env` with your own slskd settings.

Build and start the container:

```bash
docker compose up -d --build
```

## Configuration

Configuration is handled through the `.env` file.

Example:

```env
# URL of your slskd instance

# Docker Compose
# SLSKD_URL=http://slskd:5030

# Local installation
# SLSKD_URL=http://localhost:5030

# Remote server
# SLSKD_URL=http://192.168.1.100:5030

SLSKD_URL=http://slskd:5030

# slskd API key
SLSKD_API_KEY=YOUR_API_KEY

# How often to check for uploads (seconds)
CHECK_INTERVAL=60

# Seconds to wait before evaluating a user
GRACE_PERIOD=120

# Minimum sharing requirements
MIN_FILES=1000
MIN_DIRECTORIES=20
```

## Message Placeholders

The warning template supports:

- `{username}`
- `{files}`
- `{directories}`
- `{min_files}`
- `{min_directories}`

## Warning Policy

The bot sends a warning if either of the following conditions is true:

-Shared files are below the configured minimum (MIN_FILES)
-Shared folders are below the configured minimum (MIN_DIRECTORIES)

A user must meet both configured minimums to be considered compliant.

By default:

```env
MIN_FILES=1000
MIN_DIRECTORIES=20
```

These values should match the thresholds configured in your `slskd.yml` if you're using slskd's transfer groups.

Example:

```yaml
transfers:
  groups:
    leechers:
      thresholds:
        files: 1000
        directories: 20
      upload:
        priority: 999
        strategy: roundrobin
        slots: 1
        speed_limit: 100
        limits:
          queued:
            files: 15
            megabytes: 150
          daily:
            files: 30
            megabytes: 300
            failures: 10
          weekly:
            files: 150
            megabytes: 1500
            failures: 30
```

The bot does **not** enforce upload restrictions. It simply checks whether a user falls below the configured sharing thresholds and sends a one-time private message.

Any upload limits, queue limits, or bandwidth restrictions are handled entirely by slskd through its transfer group configuration.

## Project Structure

```
app/
├── api/
├── database/
├── services/
├── utils/
└── main.py
```

## Environment Variables

| Variable | Description |
|----------|-------------|
| SLSKD_URL | URL of your slskd instance |
| SLSKD_API_KEY | slskd API key |
| POLL_INTERVAL | Monitoring interval |
| GRACE_PERIOD | Seconds before evaluating uploads |

## Notes

The bot uses the slskd REST API and stores its data in a local SQLite database.

The warning message is stored in `message.txt`, so it can be edited without changing the source code.

## Roadmap

- [x] Customizable warning templates
- [x] Dynamic placeholders
- [ ] Multiple warning templates
- [ ] Web dashboard
- [ ] Optional Discord notifications
- [ ] Localization

## License

MIT
