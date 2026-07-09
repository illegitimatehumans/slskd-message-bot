# slskd-bot

A Python bot for slskd that monitors active uploads and sends a one-time private message to users who don't meet the configured sharing requirements.

This project was built for my own Soulseek server running as part of the OwlTV media stack. The goal isn't to punish users, but to encourage sharing and help keep the Soulseek community healthy.

## What it does

- Monitors active uploads through the slskd API
- Waits for a configurable grace period before checking a user
- Browses the user's shared library
- Counts shared files and shared folders
- Compares those totals against configurable minimums
- Sends a single private message if both thresholds are below the configured limits
- Stores results in SQLite so users are not messaged repeatedly
- Supports a whitelist for users that should never be checked

## Requirements

- Docker
- Docker Compose
- slskd 0.25 or newer
- Python 3.13

## Configuration

Configuration is provided through the `.env` file.

Example:

```env
SLSKD_URL=http://gluetun_slskd:5030
SLSKD_API_KEY=YOUR_API_KEY

CHECK_INTERVAL=60
GRACE_PERIOD=120

MIN_FILES=1000
MIN_DIRECTORIES=20
```

The warning message is stored separately in `message.txt` so it can be changed without modifying the source code.

## How it works

When a download starts, the bot waits for the configured grace period before evaluating the user.

The bot then:

1. Browses the user's shared library.
2. Counts the total number of shared files and folders.
3. Compares those totals against the configured minimums.
4. Sends a private message only if both values are below the limits.
5. Records the result in the database so the same user isn't warned multiple times.

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

This project was written for my own server, but it should work with any recent slskd installation with minimal configuration.

Contributions, bug reports, and suggestions are welcome.

## License

MIT
