# getid-bot

Privacy-first Telegram diagnostics bot for user IDs, group IDs, channel IDs, forum topic IDs, forwarded origins and raw update debugging.

## Features

- Private `/start` identity response.
- Group/supergroup diagnostics with chat ID, message ID and topic ID.
- Forwarded user, chat and channel origin lookup.
- `/raw` sanitized Telegram update JSON.
- `/support_card` minimal support identity card.
- `/diagnose` permission and privacy-mode guidance.
- Public `@username` lookup with `getChat`.
- Short help commands for common Telegram ID questions.

## Local Setup

```bash
uv sync --extra dev
cp .env.example .env
```

Set `BOT_TOKEN` in `.env`, then run:

```bash
uv run getid-bot
```

## Tests

```bash
uv run pytest
uv run ruff check .
```

## BotFather

Recommended commands:

```text
start - Show your Telegram identity
id - Show current chat and message IDs
contact - Inspect a forwarded user, chat or channel
raw - Show sanitized raw update JSON
diagnose - Explain permissions and privacy mode
support_card - Create a minimal support identity card
help_user_id - How to get Telegram user ID
help_group_id - How to get Telegram group ID
help_channel_id - How to get Telegram channel ID
help_topic_id - How to get forum topic ID
help_privacy - Why bots cannot see some messages
```

For broad group diagnostics, disable BotFather privacy mode only when you understand the privacy tradeoff.

## Railway

Create a Railway service from this repository and set:

```text
BOT_TOKEN=...
LOG_LEVEL=INFO
BOT_PARSE_MODE=HTML
```

Railway uses `railway.json` and starts the worker with:

```bash
uv run getid-bot
```

## Safety

This bot uses only official Telegram Bot API data. It must not scrape members, deanonymize users, discover hidden profiles or bypass Telegram privacy controls.
