# Launch Notes

## BotFather Description

```text
Open-source Telegram diagnostics bot for user IDs, chat IDs, channel IDs, forum topic IDs, forwarded origins and raw Bot API update debugging.
```

## BotFather About Text

```text
Inspect Telegram IDs, forwarded origins, chat metadata and sanitized raw updates. Privacy-first and open source: https://github.com/se1dhe/getid-bot
```

## BotFather Commands

```text
start - Show your Telegram identity and quick actions
id - Show current chat, message and topic IDs
contact - Inspect a forwarded user, chat or channel
raw - Show sanitized raw Telegram update JSON
raw_full - Show unredacted raw JSON after confirmation
diagnose - Explain permissions and privacy mode
support_card - Create a minimal support identity card
help - Show all bot capabilities
help_user_id - How to get Telegram user ID
help_group_id - How to get Telegram group ID
help_channel_id - How to get Telegram channel ID
help_topic_id - How to get forum topic ID
help_privacy - Why bots cannot see some messages
```

## Launch Post Draft

```text
I launched getid-bot: an open-source Telegram diagnostics bot for developers, admins and support teams.

It can show your Telegram ID, inspect group/channel/topic IDs, explain privacy-mode limits, parse forwarded user/chat/channel origins and return sanitized raw Bot API JSON.

Source: https://github.com/se1dhe/getid-bot
```

## Pre-Launch Checklist

- Set BotFather description.
- Set BotFather about text.
- Set BotFather commands.
- Add repository link to bot profile text.
- Confirm Railway variables: `BOT_TOKEN`, `LOG_LEVEL`, `BOT_PARSE_MODE`.
- Send `/start`, `/help`, `/diagnose`, `/raw`, `/contact`.
- Forward a user message, hidden user message, public channel post and group message.

