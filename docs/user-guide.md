# User Guide

## Get Your Telegram User ID

Open the bot in a private chat and send:

```text
/start
```

The bot shows your Telegram user ID, username, display name, language code, bot flag and Premium status when Telegram exposes it.

If Premium is not present in the update, the bot shows:

```text
Premium: not exposed by Telegram
```

## Get A Group ID

Add the bot to a group or supergroup and send:

```text
/id
```

The bot shows the chat ID, chat type, title, username, current message ID and topic ID when present.

## Get A Channel ID

For a public channel, send its username to the bot:

```text
@channel_username
```

Telegram must allow the bot to resolve that public username through `getChat`.

For private channels, add the bot where Telegram allows access, then forward a message from the channel.

## Get A Forum Topic ID

Open the exact forum topic and send:

```text
/id
```

The bot shows `Topic ID` when Telegram includes `message_thread_id`.

## Inspect A Forwarded User, Chat Or Channel

Forward a message to the bot.

The bot will inspect:

- Public forwarded user origin.
- Hidden forwarded user origin.
- Forwarded chat origin.
- Forwarded channel origin.
- Legacy forward fields.

If Telegram hides the sender, the bot cannot reveal their ID or username.

## Debug Raw Telegram Updates

Use:

```text
/raw
```

This returns sanitized JSON with message text, captions, tokens, invite links, phone numbers and sensitive fields redacted.

Use unredacted output only when necessary:

```text
/raw_full confirm
```

## Diagnose Permissions

Use:

```text
/diagnose
```

The bot checks visible chat metadata, member count, its own membership/admin status and common privacy-mode blockers.

## Why Some Data Is Missing

Telegram Bot API uses optional fields and privacy boundaries. Missing data usually means Telegram did not expose it in that context.

The bot cannot:

- Reveal hidden forwarded users.
- Fetch arbitrary private users by ID.
- Scrape group members.
- Bypass privacy mode.
- Access private channels or groups where the bot is not allowed.

