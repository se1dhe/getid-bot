# Codex Prompt

You are Codex working in `/Users/se1dhe/projects/getid-bot`.

Build a privacy-first Telegram diagnostics bot that improves on @getmyidbot. The product should identify and explain Telegram users, chats, groups, supergroups, channels, forum topics, messages and raw updates using only information exposed by the official Telegram Bot API.

Use these local files as context:

- `MARKET_ANALYSIS.md` for market positioning and feature priorities.
- `AGENTS.MD` for repository instructions.
- `SKILLS.MD` for required project capabilities.

Product positioning:

"The Telegram diagnostics bot for builders and community operators."

Required MVP:

1. Private `/start`
   - Show the current user's Telegram ID, username, display name, language code and available public flags.
   - Include simple output and developer/raw output.
   - Make values easy to copy in Telegram.

2. Group and supergroup diagnostics
   - Show chat ID, chat type, title, username, message ID and topic/message_thread_id when present.
   - Explain privacy mode and why the bot may not see all messages.
   - Detect whether the chat is a forum where possible.

3. Channel and username lookup
   - Accept public `@username` inputs.
   - Use `getChat` where the Bot API allows it.
   - Clearly explain failures caused by private chats, missing permissions or unavailable data.

4. Forwarded message handling
   - Show the forwarded origin fields Telegram exposes.
   - Explain when origin information is hidden or incomplete.

5. Raw JSON mode
   - Provide sanitized raw update JSON.
   - Redact sensitive values by default.
   - Keep a deliberate command or option for full raw output if implemented.

6. Support card mode
   - Generate a compact identity card a user can send to support.
   - Include only minimal consent-based data.

7. Documentation responses
   - Add short explanations for common questions:
     - How to get Telegram user ID.
     - How to get group ID.
     - How to get channel ID.
     - How to get forum topic ID.
     - Why Telegram IDs can be negative.
     - Why bots cannot see some messages.

Engineering requirements:

- Use Python + aiogram + uv.
- Keep Railway deployment configs working.
- Store Telegram IDs without precision loss.
- Add tests for parsing, formatting, redaction and Bot API error handling.
- Keep code modular: update parsing, formatting, Telegram API client, redaction and command handlers should be separate.
- Do not implement scraping, member-list extraction, deanonymization, hidden-profile lookup or privacy bypasses.
- Use official Telegram Bot API documentation as the source of truth.

Deliverables:

- Working bot implementation.
- Environment sample file.
- README with setup, local run, deployment and BotFather configuration.
- Tests for the critical parser/formatter/redaction behavior.
- Updated `AGENTS.MD` with actual package manager and commands.
