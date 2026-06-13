HELP_OVERVIEW = (
    "<b>getid-bot help</b>\n"
    "Use this bot to inspect Telegram IDs and Bot API-visible metadata.\n\n"
    "<b>Main flows</b>\n"
    "/start - your Telegram identity and quick actions\n"
    "/id - current chat, message and forum topic IDs\n"
    "/contact - forward a message to inspect its origin\n"
    "/raw - sanitized raw Telegram update JSON\n"
    "/diagnose - permissions, member count and privacy-mode clues\n"
    "/support_card - minimal card for support teams\n\n"
    "<b>Lookups</b>\n"
    "Send @channel_username or @group_username to run a public getChat lookup.\n"
    "Forward a user, group or channel message to inspect what Telegram exposes.\n\n"
    "<b>Privacy</b>\n"
    "The bot cannot reveal hidden forwarded users, scrape members or bypass Telegram limits."
)

MAIN_MENU_TEXT = (
    "<b>getid-bot menu</b>\n"
    "Choose what you want to inspect.\n\n"
    "<b>Fast paths</b>\n"
    "My Telegram ID - your user ID and public user fields.\n"
    "Chat ID - how to get group, channel and topic IDs.\n"
    "Forwarded contact - inspect forwarded user/chat/channel origins.\n"
    "Raw update JSON - debug Telegram update payloads safely.\n"
    "Diagnostics - check bot permissions and privacy-mode blockers."
)

CHAT_ID_MENU = (
    "<b>Chat ID</b>\n"
    "Use /id in any chat where the bot can receive messages.\n\n"
    "In groups and supergroups, the bot shows chat ID, chat type, message ID and topic ID "
    "when Telegram includes message_thread_id.\n\n"
    "For public channels or groups, send @username here to run a getChat lookup."
)

RAW_MENU = (
    "<b>Raw update JSON</b>\n"
    "Use /raw on any message to inspect sanitized Telegram update JSON.\n\n"
    "The bot redacts text, captions, callback data, tokens, invite links, phone numbers, "
    "emails, payment data and file identifiers by default.\n\n"
    "Use /raw_full confirm only when unredacted output is deliberately needed."
)

DIAGNOSTICS_MENU = (
    "<b>Diagnostics</b>\n"
    "Use /diagnose to inspect the current chat.\n\n"
    "The bot attempts getChat, getChatMemberCount and getChatMember for its own account, "
    "then reports bot status, visible member count, topic ID and unavailable checks."
)

CONTACT_HELP = (
    "<b>Contact lookup</b>\n"
    "Forward me a message from a user, group or channel. I will show every origin field "
    "Telegram exposes to bots.\n\n"
    "For hidden forwarded users, Telegram may expose only a display name. I will say that "
    "clearly instead of guessing."
)

RAW_FULL_WARNING = (
    "<b>Raw full output</b>\n"
    "This can include private message text and Telegram identifiers. Prefer /raw for normal "
    "debugging.\n\n"
    "To continue, send:\n"
    "<code>/raw_full confirm</code>"
)

HELP_TEXTS = {
    "help_user_id": (
        "<b>How to get Telegram user ID</b>\n"
        "Open this bot in a private chat and press /start. Your user ID is the stable numeric "
        "identifier Telegram exposes to bots."
    ),
    "help_group_id": (
        "<b>How to get Telegram group ID</b>\n"
        "Add this bot to the group and send /id. Supergroup IDs are usually negative and may "
        "start with -100."
    ),
    "help_channel_id": (
        "<b>How to get Telegram channel ID</b>\n"
        "For public channels, send @channel_username here. For private channels, the bot must "
        "have access before Telegram exposes channel data."
    ),
    "help_topic_id": (
        "<b>How to get forum topic ID</b>\n"
        "Send /id inside the forum topic. Telegram includes message_thread_id only when the "
        "message belongs to a topic."
    ),
    "help_privacy": (
        "<b>Why bots cannot see some messages</b>\n"
        "Group bots use BotFather privacy mode by default. They normally receive commands, "
        "replies to the bot and service messages, unless privacy is disabled or the bot has "
        "the right admin setup."
    ),
}
