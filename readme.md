🚀 AI-Powered Discord Assistant

An intelligent AI-powered Discord bot built using Python, Discord.py, LangChain, Google Gemini, OpenAI Image Generation, and Tavily Search API.

This assistant can:

    💬 Chat naturally with users
    🌐 Search the internet for latest information
    🎨 Generate AI images from prompts
    ⚡ Respond in real-time inside Discord servers
    📌 Features
    
    ✅ AI-powered conversational assistant
    ✅ Internet search using Tavily API
    ✅ AI image generation support
    ✅ Real-time Discord integration
    ✅ Typing indicator while generating responses
    ✅ Clean and modular project structure
    ✅ Async support for smooth performance

🛠️ Tech Stack
    Python
    Discord.py
    LangChain
    Google Gemini API
    OpenAI API
    Tavily Search API
    dotenv

📂 Project Structure

    AI-Powered-Discord-Assistant/
    ├── bot.py
    ├── agent.py
    ├── .env
    ├── requirements.txt
    └── README.md


⚙️ Installation
1️⃣ Clone Repository

    git clone https://github.com/akshitgajera1013/AI-Powered-Discord-Assistant.git
    cd AI-Powered-Discord-Assistant

2️⃣ Create Virtual Environment

Windows

    python -m venv venv
    venv\Scripts\activate

Mac/Linux

    python3 -m venv venv
    source venv/bin/activate

3️⃣ Install Dependencies

    pip install -r requirements.txt

🔑 Environment Variables

Create a .env file in the root directory.

    DISCORD_API_KEY=your_discord_bot_token
    TAVILY_API_KEY=your_tavily_api_key
    GOOGLE_API_KEY=your_google_gemini_api_key
    OPENAI_API_KEY=your_openai_api_key


🤖 Discord Bot Setup
Step 1 — Create Discord Application

Go to:

    👉 https://discord.com/developers/applications

Create a new application
Open the Bot section
Click Add Bot

Step 2 — Enable Privileged Gateway Intents

Enable:

✅ Message Content Intent

Step 3 — Invite Bot to Server

Go to:

OAuth2 → URL Generator

Select:

bot

Bot Permissions:

Administrator

Then copy generated URL and invite bot to your server.


▶️ Run The Bot
python bot.py

If everything is configured correctly:

Bot is online 🚀
🧠 How It Works
Internet Search Tool

Uses Tavily API to fetch latest real-time information.

@tool
def surfInternet(query:str):
AI Image Generation Tool

Generates images using OpenAI image generation tools and sends directly to Discord.

@tool
def generateAndSendImage(prompt:str,runTime:ToolRuntime):
Agent System

The bot uses LangChain agents to intelligently decide:

When to search the web
When to generate images
How to answer users naturally

📸 Example Commands
Chat with AI
What is Machine Learning?
Search Internet
Latest AI news
Generate Image
Generate image of futuristic cyberpunk city


👨‍💻 Author
Akshit Gajera
Data Science & Machine Learning Enthusiast
Python Developer
AI & LLM Projects Builder

GitHub:

akshitgajera1013 GitHub
