# Agent Instructions

## Repository State
- Python + aiogram Telegram diagnostics bot.
- Railway worker deployment via Nixpacks.
- Keep product docs concise, source-backed, and implementation-ready.

## Package Manager
- Use **uv**: `uv sync --extra dev`, `uv run getid-bot`, `uv run pytest`.

## Core Product
- Build a privacy-first Telegram bot for user, group, channel, topic, message and raw update diagnostics.
- Prefer "what Telegram exposes and why" over speculative enrichment.
- Never implement scraping, deanonymization, hidden member discovery, or bypasses of Telegram privacy controls.

## Source Of Truth
- Market/product direction: `MARKET_ANALYSIS.md`.
- Agent capabilities and workflows: `SKILLS.MD`.
- Build prompt: `CODEX_PROMPT.md`.
- Telegram Bot API: https://core.telegram.org/bots/api
- Telegram Bot Features: https://core.telegram.org/bots/features

## Engineering Defaults
- Store Telegram IDs safely; IDs may exceed 32 significant bits.
- Treat raw Telegram updates as sensitive data.
- Redact phone numbers, invite links, tokens, emails and long opaque identifiers in logs and shared output.
- Make every user-facing field copyable in final UX.
- Explain missing data as a platform limitation when Telegram does not expose it.

## File-Scoped Commands
| Task | Command |
| --- | --- |
| Run bot | `uv run getid-bot` |
| Test | `uv run pytest tests/test_file.py` |
| Lint | `uv run ruff check path/to/file.py` |
| Search files | `rg "term"` |
| List files | `rg --files` |

## Testing Expectations
- Cover ID formatting, redaction, forwarded-message parsing, topic IDs, privacy-mode explanations and Bot API errors.
- Keep parser/formatter/redaction tests isolated from real Telegram network calls.

## Commit Attribution
AI commits MUST include:
```
Co-Authored-By: (the agent model's name and attribution byline)
```
