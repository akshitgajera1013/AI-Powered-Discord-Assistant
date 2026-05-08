<div align="center">

<!-- Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=5865F2&height=200&section=header&text=AI%20Discord%20Assistant&fontSize=48&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Intelligent%20%E2%80%A2%20Multimodal%20%E2%80%A2%20Real-time&descAlignY=58&descSize=18" width="100%"/>

<br/>

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Discord.py](https://img.shields.io/badge/Discord.py-2.x-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discordpy.readthedocs.io)
[![LangChain](https://img.shields.io/badge/LangChain-Agents-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)](https://langchain.com)
[![Google Gemini](https://img.shields.io/badge/Google-Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev)
[![OpenAI](https://img.shields.io/badge/OpenAI-Image%20Gen-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com)
[![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)](LICENSE)

<br/>

> **A production-ready Discord bot powered by LangChain agents, Google Gemini, OpenAI image generation, and real-time web search — all orchestrated intelligently in your server.**

<br/>

[Getting Started](#-quick-start) · [Features](#-features) · [Architecture](#-architecture) · [Contributing](#-contributing)

<br/>

</div>

---

## ✨ Features

| Capability | Description |
|---|---|
| 💬 **AI Conversations** | Natural, context-aware chat powered by Google Gemini via LangChain |
| 🌐 **Live Web Search** | Fetches real-time information using the Tavily Search API |
| 🎨 **Image Generation** | Creates AI images on demand and delivers them directly in Discord |
| ⚡ **Async Architecture** | Fully async — no blocking, no lag, smooth concurrent responses |
| ⌨️ **Typing Indicator** | Shows Discord's native typing animation while the bot is thinking |
| 🤖 **LangChain Agent** | Intelligently decides whether to chat, search, or generate an image |

---

## 🧠 How It Works

The bot uses a **LangChain Agent** backed by Google Gemini as its reasoning engine. On every message, the agent evaluates the user's intent and dynamically routes it to the right tool:

```
User Message
     │
     ▼
 LangChain Agent (Gemini)
     │
     ├──▶ 💬 Direct Response       → General knowledge questions
     ├──▶ 🌐 Tavily Web Search     → Current events, real-time data
     └──▶ 🎨 OpenAI Image Gen      → Image creation requests
```

---

## 📁 Project Structure

```
AI-Powered-Discord-Assistant/
│
├── bot.py               # Discord client, event listeners, message routing
├── agent.py             # LangChain agent setup, tools, Gemini integration
├── .env                 # API keys and secrets (never commit this)
├── requirements.txt     # Python dependencies
└── README.md
```

---

## ⚙️ Quick Start

### Prerequisites

- Python 3.10 or higher
- A Discord account and bot token
- API keys for: Tavily, Google Gemini, and OpenAI

---

### 1 · Clone the Repository

```bash
git clone https://github.com/akshitgajera1013/AI-Powered-Discord-Assistant.git
cd AI-Powered-Discord-Assistant
```

### 2 · Create a Virtual Environment

```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3 · Install Dependencies

```bash
pip install -r requirements.txt
```

### 4 · Configure Environment Variables

Create a `.env` file in the project root:

```env
DISCORD_API_KEY=your_discord_bot_token
TAVILY_API_KEY=your_tavily_api_key
GOOGLE_API_KEY=your_google_gemini_api_key
OPENAI_API_KEY=your_openai_api_key
```

> ⚠️ **Never commit your `.env` file.** Add it to `.gitignore` immediately.

---

## 🤖 Discord Bot Setup

**Step 1 — Create a Discord Application**

1. Visit the [Discord Developer Portal](https://discord.com/developers/applications)
2. Click **New Application** and give it a name
3. Navigate to the **Bot** section → click **Add Bot**
4. Copy your **Bot Token** and add it to `.env`

**Step 2 — Enable Required Intents**

Under **Bot → Privileged Gateway Intents**, enable:

- ✅ **Message Content Intent**

**Step 3 — Invite the Bot to Your Server**

1. Go to **OAuth2 → URL Generator**
2. Select scope: `bot`
3. Select permission: `Administrator`
4. Copy the generated URL and open it in your browser to invite the bot

---

### 5 · Run the Bot

```bash
python bot.py
```

You should see:

```
✅ Logged in as YourBot#1234
🚀 Bot is online and ready!
```

---

## 💡 Example Usage

| Intent | Example Prompt |
|---|---|
| 💬 General Chat | `What is the difference between ML and AI?` |
| 🌐 Web Search | `What are the latest news in AI today?` |
| 🎨 Image Generation | `Generate an image of a futuristic cyberpunk city at night` |

---

## 🛠️ Tech Stack

| Technology | Role |
|---|---|
| [Python 3.10+](https://python.org) | Core language |
| [Discord.py](https://discordpy.readthedocs.io) | Discord API integration |
| [LangChain](https://langchain.com) | Agent orchestration & tool routing |
| [Google Gemini](https://ai.google.dev) | Primary language model |
| [OpenAI API](https://platform.openai.com) | AI image generation (DALL·E) |
| [Tavily API](https://tavily.com) | Real-time web search |
| [python-dotenv](https://pypi.org/project/python-dotenv) | Environment variable management |

---

## 🔑 API Keys — Where to Get Them

| Service | Link |
|---|---|
| Discord Bot Token | [discord.com/developers/applications](https://discord.com/developers/applications) |
| Google Gemini API | [aistudio.google.com](https://aistudio.google.com) |
| OpenAI API | [platform.openai.com/api-keys](https://platform.openai.com/api-keys) |
| Tavily Search API | [tavily.com](https://tavily.com) |

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'feat: add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

Please follow [Conventional Commits](https://www.conventionalcommits.org/) for commit messages.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

<div align="center">

**Akshit Gajera**

*Data Science & Machine Learning Enthusiast · Python Developer · AI/LLM Builder*

[![GitHub](https://img.shields.io/badge/GitHub-akshitgajera1013-181717?style=for-the-badge&logo=github)](https://github.com/akshitgajera1013)

</div>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=5865F2&height=100&section=footer" width="100%"/>

*If this project helped you, consider giving it a ⭐ — it means a lot!*

</div>
