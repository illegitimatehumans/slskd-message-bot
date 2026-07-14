# slskd-message-bot
![Docker](https://img.shields.io/badge/Container-GHCR-blue)
![Python](https://img.shields.io/badge/Python-3.13-blue)
![License](https://img.shields.io/github/license/illegitimatehumans/slskd-message-bot)
![Release](https://img.shields.io/github/v/release/illegitimatehumans/slskd-message-bot)
Automatically synchronizes with your live **slskd** transfer group configuration—no duplicated settings to maintain.

An automated sharing policy bot for slskd that monitors active uploads, automatically evaluates uploaders against the active slskd transfer group, retries temporary browse failures, and sends a one-time customizable private message to users who don't meet your server's sharing policy.

Designed to complement **slskd** transfer groups by explaining *why* downloads may be limited instead of silently throttling users.

---

# Features

- Automatic upload monitoring
- Configurable grace period
- Automatic sharing policy evaluation
- Dynamic synchronization with Slskd transfer groups
- Intelligent browse retry backoff
- One-time customizable private messages
- Dynamic message placeholders
- Whitelist support
- SQLite database to prevent duplicate messages
- Docker and GitHub Container Registry support

---

# Why This Exists
slskd can already identify low-share users and place them into transfer groups with different upload limits.
What it doesn't do is explain those restrictions.
This bot automatically sends a one-time private message informing the user:
- why they were flagged
- what your minimum sharing requirements are
- how to become compliant
The result is a better user experience and fewer confused users asking why their downloads are slow.
---

# Screenshots

## Upload Evaluation

The bot automatically monitors active uploads, evaluates users against your sharing policy, and logs the results.

![Upload Evaluation](assets/assets-upload-evaluation.png)

## Warning Detection

The bot automatically evaluates uploaders against the active slskd transfer group. If a user doesn't meet the configured sharing requirements, a customizable private message is sent and recorded to prevent duplicate notifications.

![Warning Detection](assets/warning-detection.png)

## Example Warning Message

When a user doesn't meet your configured sharing policy, the bot automatically sends a customizable private message.

![Warning message](assets/warning-message.png)
---

# How It Works

1. Monitor active uploads.
2. Wait for the configured grace period.
3. Browse the user's shared files.
4. Compare their shares against the active slskd transfer group.
5. Send a one-time customizable warning if they don't meet the configured requirements.
6. Cache the result to avoid repeated browsing and duplicate messages.


# Requirements
- Docker
- Docker Compose
- Python 3.13
- slskd 0.25+
---

# slskd Compatibility
This project uses the current documented slskd REST API.
### Private Messages
```
POST /api/v0/conversations/{username}
```
### Live Configuration
```
GET /api/v0/options
```
The bot automatically synchronizes its warning messages with the active slskd transfer group configuration, including sharing thresholds and transfer limits.
---

# Installation
Clone the repository:
```bash
git clone https://github.com/illegitimatehumans/slskd-message-bot.git
cd slskd-message-bot
```
Copy the example environment:
```bash
cp .env.example .env
```
Edit `.env` with your own slskd settings.
Build and start:
```bash
docker compose up -d --build
```
---

## Docker Image

Prebuilt images are published to GitHub Container Registry.

```yaml
services:
  slskd-bot:
    image: ghcr.io/illegitimatehumans/slskd-message-bot:latest
```

# First Run
On first startup the bot automatically creates:
```
data/message.txt
```
from:
```
message.txt.example
```
You can edit `data/message.txt` at any time without rebuilding the container.
---

# Configuration
Example:
```env
SLSKD_URL=http://slskd:5030
SLSKD_API_KEY=YOUR_API_KEY
CHECK_INTERVAL=60
GRACE_PERIOD=120
GOOD_RECHECK_MINUTES=1440
LEECHER_RECHECK_MINUTES=60
# Browse retry delays (seconds)
BROWSE_RETRY_DELAYS=2,5,10
```
### Notes
The bot now reads the configured leecher thresholds directly from the running slskd server using:
```
GET /api/v0/options
```
This means warning messages automatically stay synchronized with your slskd configuration.
## Browse Retry
Some users may not respond to an initial browse request immediately.
The bot retries failed browse requests before marking a user as `UNKNOWN`.
Configure the delay between retries using:
```env
BROWSE_RETRY_DELAYS=2,5,10
```
The example above behaves as follows:
| Attempt | Action |
|---------|--------|
| 1 | Browse immediately |
| 2 | Retry after 2 seconds |
| 3 | Retry after 5 seconds |
| 4 | Retry after 10 seconds |

The number of retries is determined automatically from the configured delay list.
---

# Message Templates

The warning template supports the following placeholders:

- `{username}`
- `{files}`
- `{directories}`
- `{min_files}`
- `{min_directories}`
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


Example:

```text
Hello {username},

Your current Soulseek shares appear to be below this server's minimum sharing requirements.

Current shares:

• {files} files
• {directories} folders

Minimum recommended:

• {min_files} shared files
• {min_directories} shared folders

Until these requirements are met, your downloads are placed in a limited transfer group.

Current limits:

- {upload_slots} upload slot(s)
- {speed_limit} KB/s maximum transfer speed
- {queue_files} queued download(s)
- Queue size: {queue_size} MB
- Daily: {daily_files} files or {daily_size} MB
- Weekly: {weekly_files} files or {weekly_size} MB

Once you meet the sharing requirements, these restrictions are removed automatically.

Sharing helps keep the Soulseek community healthy for everyone.

Thanks for understanding and for helping keep Soulseek a sharing community!

```

---

# Warning Policy

A user must satisfy **both** configured sharing requirements.
A warning is sent when **either** condition is true:
- shared files are below the configured minimum
- shared directories are below the configured minimum
The bot **does not** enforce upload restrictions.
Upload limits, priorities, bandwidth limits, and queue restrictions remain entirely managed by slskd transfer groups.

---

# Project Structure
```
app/
├── api/
├── database/
├── services/
├── utils/
└── main.py
```
---

# Environment Variables

| Variable | Description |
|-----------|-------------|
| SLSKD_URL | slskd API URL |
| SLSKD_API_KEY | slskd API key |
| CHECK_INTERVAL | Seconds between upload scans |
| GRACE_PERIOD | Seconds before evaluating a new uploader |
| GOOD_RECHECK_MINUTES | Recheck interval for compliant users |
| LEECHER_RECHECK_MINUTES | Recheck interval for users below sharing policy |
| BROWSE_RETRY_DELAYS | Retry delays (comma separated) |
| WHITELIST | Comma-separated usernames to ignore |

## Docker
### Production
Uses the latest image published to GitHub Container Registry.
No local build is required.

```bash
docker compose pull
docker compose up -d
```
### Development

Ideal for local development and testing.

```bash
docker compose -f docker-compose.dev.yml up -d --build

```
Builds the image locally for development.
---
## AI Disclosure

This project was developed by the project maintainer with assistance from AI coding tools.
AI was used to help:
- Brainstorm implementation ideas
- Review and refactor code
- Debug issues
- Improve documentation
- Draft release notes
All architecture, feature decisions, testing, and final code review were performed by the maintainer. Every change was reviewed and validated against a live `slskd` instance before being released.
AI assistance was used as a development tool, not as a replacement for human judgment.

## Community
Need help, want to report a bug, or have an idea for a new feature?
Join the Discord community!
[![Discord](https://img.shields.io/badge/Discord-Join%20Server-5865F2?logo=discord&logoColor=white)](https://discord.gg/VSztdkRYD)

# License

MIT
