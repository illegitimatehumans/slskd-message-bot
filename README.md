# slskd-message-bot

slskd-message-bot is a companion service for slskd that monitors active uploads and sends a one-time private message to users who don't meet your configured sharing requirements.

It is designed to complement slskd's built-in transfer groups by informing users why their downloads may be limited instead of silently throttling or restricting them.

## Why?

slskd can already identify users with low share counts and apply different transfer limits through transfer groups. What it doesn't do is explain those restrictions to the user.

This bot fills that gap by automatically sending a friendly one-time message that explains your server's sharing policy.

## Features

- Monitors active uploads through the slskd REST API
- Configurable grace period before evaluating users
- Browses remote user shares
- Counts shared files and folders
- Evaluates users against configurable thresholds
- Sends a one-time private message
- SQLite database to prevent duplicate messages
- Automatically creates a customizable message template on first run
- Whitelist support
- Docker support

## Requirements

- Docker
- Docker Compose
- slskd 0.25 or newer
- Python 3.13

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

## Warning Policy

The bot only sends a warning when **both** of these conditions are true:

- Shared files are below the configured minimum (`MIN_FILES`)
- Shared folders are below the configured minimum (`MIN_DIRECTORIES`)

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

## Notes

The bot uses the slskd REST API and stores its data in a local SQLite database.

The warning message is stored in `message.txt`, so it can be edited without changing the source code.

## License

MIT
