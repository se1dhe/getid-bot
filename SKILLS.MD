# Skills For This Project

## Market Intelligence
- Track direct competitors: @userinfobot, @getmyidbot, @myidbot, @username_to_id_bot, @RawDataBot, @getidsbot.
- Monitor Telegram bot pages for monthly-user changes.
- Watch Bot API changelog and @BotNews for new accessible fields or privacy changes.
- Maintain `MARKET_ANALYSIS.md` with dated sources.

## Telegram Bot API
- Implement update parsing for private messages, groups, supergroups, channels, forum topics, forwards and replies.
- Use `getChat`, `getChatMember`, `getChatAdministrators` and `getChatMemberCount` only where allowed.
- Handle privacy mode, admin rights, channel membership and username lookup failures explicitly.
- Preserve large numeric IDs without precision loss.

## Privacy And Safety
- Minimize collection and retention by default.
- Redact sensitive fields in raw JSON unless the user explicitly requests full output.
- Avoid features that infer private identity, scrape member lists or bypass platform limits.
- Keep logs free of bot tokens, invite links, phone numbers and private payloads.

## Product UX
- Prioritize instant answers, copy buttons, plain labels and concise explanations.
- Provide output modes: simple, developer, raw JSON and support card.
- Localize first for English, Ukrainian and Russian.
- Make "why this field is unavailable" a first-class response.

## Developer Experience
- Provide snippets for aiogram, python-telegram-bot, Telegraf and grammY.
- Include curl examples for Bot API calls.
- Build framework-agnostic docs for user ID, chat ID, channel ID, topic ID and privacy mode.
- Prefer small, testable parser/formatter modules.

## Operations
- Add structured logging with redaction.
- Track Bot API error rates, latency and command usage.
- Support a staging bot token and Telegram test environment when needed.
- Prepare graceful degradation for Telegram API failures and rate limits.

