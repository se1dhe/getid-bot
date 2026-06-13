# getid-bot

Open-source, privacy-first Telegram diagnostics bot for IDs, chats, channels, forum topics, forwarded origins and raw update debugging.

Repository: https://github.com/se1dhe/getid-bot

## What The Bot Does

`getid-bot` helps Telegram users, bot developers, channel admins and support teams understand what Telegram Bot API exposes about a user, chat, group, channel or forwarded message.

It is not a scraping or deanonymization tool. If Telegram hides a field, the bot says that clearly instead of guessing.

## Current Features

- Private identity lookup via `/start`.
- Current chat diagnostics via `/id`.
- Forwarded contact lookup for users, hidden users, chats and channels.
- Public `@username` lookup through Telegram `getChat`.
- Forum topic detection through `message_thread_id`.
- Sanitized raw Telegram update output via `/raw`.
- Permission and privacy-mode explanation via `/diagnose`.
- Minimal support identity card via `/support_card`.
- Built-in help texts for common Telegram ID questions.
- Open-source notice and repository link in onboarding.
- Railway-ready worker deployment.

## User Identity Lookup

In a private chat, `/start` shows:

- Telegram user ID.
- Username.
- Display name.
- Language code when Telegram exposes it.
- Bot flag.
- Premium status when Telegram exposes it.
- `Premium: not exposed by Telegram` when the field is absent.

Important: Telegram Bot API does not provide a general `getUser(user_id)` method. The bot can only show user fields present in updates, forwarded origins or other official Bot API objects.

## Contact Lookup By Forwarded Message

Forward any message to the bot to inspect its origin.

For forwarded users, the bot can show:

- User ID.
- Username.
- Display name.
- Bot flag.
- Premium status or `not exposed by Telegram`.
- Other public user flags when Telegram includes them.

For hidden forwarded users, the bot shows:

- Sender display name.
- A clear note that Telegram hides user ID and username.

For forwarded channels, the bot can show:

- Channel ID.
- Chat type.
- Title.
- Username.
- Original channel message ID.
- Author signature when present.
- Extra `getChat` fields when Telegram allows access, such as description, active usernames, forum flag or linked chat ID.

For forwarded chats/groups, the bot can show:

- Chat ID.
- Chat type.
- Title.
- Username.
- Author signature when present.
- Extra `getChat` fields when available.

## Chat And Topic Diagnostics

Use `/id` in any chat where the bot can receive messages.

The bot shows:

- Chat ID.
- Chat type.
- Chat title.
- Chat username.
- Current message ID.
- Forum topic ID / `message_thread_id` when present.

Supergroup and channel IDs may be negative and often start with `-100`. Store Telegram IDs as 64-bit integers or strings to avoid precision loss.

## Raw Update Debugging

Use `/raw` to see the sanitized Telegram update JSON.

The bot redacts common sensitive values before sending raw output:

- Bot tokens.
- Invite links.
- Phone numbers.
- Email addresses.
- Sensitive Telegram file identifiers and direct URL fields.

Long raw responses are truncated to stay within Telegram message limits.

## Commands

Recommended BotFather command list:

```text
start - Show your Telegram identity and next steps
id - Show current chat, message and topic IDs
contact - Inspect a forwarded user, chat or channel
raw - Show sanitized raw Telegram update JSON
diagnose - Explain permissions and privacy mode
support_card - Create a minimal support identity card
help_user_id - How to get Telegram user ID
help_group_id - How to get Telegram group ID
help_channel_id - How to get Telegram channel ID
help_topic_id - How to get forum topic ID
help_privacy - Why bots cannot see some messages
```

## Telegram Privacy Boundaries

The bot only uses official Telegram Bot API data.

It cannot:

- Fetch arbitrary private users by ID.
- Reveal hidden forwarded sender IDs.
- Scrape group members.
- Discover hidden profiles.
- Bypass BotFather privacy mode.
- Access private channels or groups where the bot has no access.
- Guarantee that optional fields, such as Premium status, are always present.

## Local Setup

Install dependencies:

```bash
uv sync --extra dev
cp .env.example .env
```

Set `BOT_TOKEN` in `.env`:

```env
BOT_TOKEN=123456:replace-me
LOG_LEVEL=INFO
BOT_PARSE_MODE=HTML
```

Run the bot:

```bash
uv run getid-bot
```

## Tests And Lint

```bash
uv run pytest
uv run ruff check .
```

## Railway Deployment

Create a Railway service from this GitHub repository.

Required variable:

```text
BOT_TOKEN=...
```

Recommended variables:

```text
LOG_LEVEL=INFO
BOT_PARSE_MODE=HTML
```

Railway uses `railway.json` and starts the worker with:

```bash
uv run getid-bot
```

The app is a polling worker, not a web service. A public HTTP domain is not required for the current deployment mode.

## Project Structure

```text
src/getid_bot/
  bot.py          # aiogram bot startup
  config.py       # environment settings
  handlers.py     # Telegram command and message handlers
  formatters.py   # HTML response formatting
  help_texts.py   # short built-in docs
  redaction.py    # raw update redaction
tests/
  test_formatters.py
  test_redaction.py
```

## Safety Policy

Do not add features that scrape members, deanonymize users, bypass Telegram privacy controls, harvest hidden profile data or imply access Telegram does not provide.

The product promise is diagnostics, transparency and safe developer/admin workflows.

