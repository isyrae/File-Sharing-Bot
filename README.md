📁 File Sharing Token Bot – Clean Guide

A powerful Telegram bot that stores posts and documents, and makes them accessible through tokenized special links.

------------------------------------------------------------
🚀 Features

- ✅ Store Telegram posts and documents
- 🔗 Access content via token-based special links
- ⏳ Token verification with expiry (optional)
- 🧼 Auto-deletion of shared files (optional)
- 🔐 Forward protection (optional)
- 🔄 Shortlink integration (optional)
- 👥 Force subscription support (optional)
- 👨‍💻 Admin commands and statistics

------------------------------------------------------------
🛠️ Setup Steps (for VPS)

1. Clone the Repository:
   git clone https://github.com/isyrae/File-Sharing-Bot
   cd File-Sharing-Bot

2. Install Requirements:
   pip3 install -r requirements.txt

------------------------------------------------------------
📦 Configuration (config.py or .env)

Set these mandatory environment variables or fill them in directly in config.py.

🔑 Required Variables:

| Variable         | Description                                                  |
|------------------|--------------------------------------------------------------|
| API_HASH         | From https://my.telegram.org                                 |
| APP_ID           | From https://my.telegram.org                                 |
| TG_BOT_TOKEN     | Bot token from https://t.me/BotFather                        |
| OWNER_ID         | Your Telegram user ID (numeric)                              |
| CHANNEL_ID       | Your database channel ID (bot must be admin)                 |
| DB_URI           | MongoDB URI (e.g., mongodb://127.0.0.1:27017)                |
| DB_NAME          | MongoDB DB name (e.g., filebot)                              |

⚙️ Optional Variables:

| Variable                  | Description |
|---------------------------|-------------|
| ADMINS                   | Space-separated user IDs |
| FORCE_SUB_CHANNEL        | Channel ID for force sub (use 0 to disable) |
| START_MESSAGE            | Custom /start message (HTML allowed) |
| FORCE_SUB_MESSAGE        | Message for unsubscribed users |
| PROTECT_CONTENT          | True/False – prevent file forwarding |
| CUSTOM_CAPTION           | HTML caption format for documents |
| DISABLE_CHANNEL_BUTTON   | True/False – hide share button |
| BOT_STATS_TEXT           | Custom text for /stats command |
| USER_REPLY_TEXT          | Default reply text |

🔐 Token Configs:

| Variable        | Description |
|-----------------|-------------|
| IS_VERIFY       | True to enable token verification |
| VERIFY_EXPIRE   | Token expiry in seconds (e.g., 86400) |
| SHORTLINK_URL   | Shortener API base URL |
| SHORTLINK_API   | Shortener API key |

------------------------------------------------------------
▶️ Running the Bot

python3 main.py

------------------------------------------------------------
🔧 Admin Commands

| Command         | Description |
|------------------|-------------|
| /start          | Start or get files |
| /batch          | Generate links for multiple posts |
| /genlink        | Generate link for one post |
| /users          | View user count |
| /broadcast      | Broadcast a message |
| /stats          | Show uptime and bot stats |

------------------------------------------------------------
🧪 Text Template Fillings

Use these placeholders in your messages:

- {first}, {last}, {id}, {mention}, {username}
- {filename}, {previouscaption} (for document captions)
- {uptime} (for /stats)

------------------------------------------------------------
🛡 License
This project is licensed under the MIT License.
You are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software — with attribution.

------------------------------------------------------------
💬 Support & Community

- 💬 Developer: https://t.me/isyrae
- 📢 Channel: https://t.me/isyraeprojects
