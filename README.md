# slskd-message-bot

An automated leecher notification bot for **slskd** that monitors active uploads, evaluates users against your server's sharing policy, and sends a friendly one-time private message to users who don't meet your configured sharing requirements.

Designed to complement **slskd** transfer groups by explaining *why* downloads may be limited instead of silently throttling users.

---

# Features

- Automatic upload monitoring
- Configurable grace period
- Remote share browsing
- One-time private messages
- Customizable warning message templates
- Dynamic placeholders
  - `{username}`
  - `{files}`
  - `{directories}`
  - `{min_files}`
  - `{min_directories}`
- Automatically reads live sharing thresholds from slskd
- SQLite database prevents duplicate warnings
- Docker support

---

# Why?

slskd can already identify low-share users and place them into transfer groups with different upload limits.

What it doesn't do is explain those restrictions.

This bot automatically sends a one-time private message informing the user:

- why they were flagged
- what your minimum sharing requirements are
- how to become compliant

The result is a better user experience and fewer confused users asking why their downloads are slow.

---

# Screenshots

Coming soon.

---

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

The bot automatically reads the configured leecher thresholds directly from slskd, ensuring warning messages always match the server configuration.

If you're running an older version of slskd, check `/swagger` to verify the available endpoints.

---

# Installation

Clone the repository:

```bash
git clone https://github.com/illegitimatehumans/slskd-bot.git

cd slskd-bot
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
```

### Notes

The bot now reads the configured leecher thresholds directly from the running slskd server using:

```
GET /api/v0/options
```

This means warning messages automatically stay synchronized with your slskd configuration.

---

# Message Templates

The warning template supports the following placeholders:

- `{username}`
- `{files}`
- `{directories}`
- `{min_files}`
- `{min_directories}`

Example:

```text
Hello {username},

Your current Soulseek shares appear to be below this server's minimum sharing requirements.

Current shares

• {files} files
• {directories} folders

Minimum recommended

• {min_files} shared files
• {min_directories} shared folders

Thank you for contributing to the Soulseek community!
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
| SLSKD_URL | URL of your slskd instance |
| SLSKD_API_KEY | slskd API key |
| CHECK_INTERVAL | Seconds between upload scans |
| GRACE_PERIOD | Seconds before evaluating a new uploader |

---

# Roadmap

- [x] Customizable warning templates
- [x] Dynamic placeholders
- [x] Live slskd threshold detection
- [ ] Multiple warning templates
- [ ] Discord notifications
- [ ] Web dashboard
- [ ] Localization

---

# License

MIT
