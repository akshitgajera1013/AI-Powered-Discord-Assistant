# 🤖 AI-Powered Discord Assistant

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Discord.py](https://img.shields.io/badge/Discord-Bot-5865F2.svg)](https://discordpy.readthedocs.io/)
[![LangChain](https://img.shields.io/badge/Framework-LangChain-green.svg)](https://python.langchain.com/)

An advanced, multi-modal autonomous Discord bot. This assistant engages in conversational reasoning, searches the live internet for up-to-date facts, and dynamically generates images directly in your Discord server.

## ✨ Core Features
* 🧠 **Advanced Reasoning:** Powered by Google's `Gemini 2.5 Flash` for high-speed, intelligent text generation and conversation.
* 🌐 **Live Web Search:** Integrated with the `Tavily API` to bypass standard LLM training data cut-offs and fetch real-time internet data to answer questions accurately.
* 🎨 **Image Generation:** Utilizes OpenAI's `DALL-E 3` to seamlessly generate and send image files natively within the Discord channel.
* 🔀 **Smart Agentic Routing:** Uses `LangGraph` (`create_react_agent`) to autonomously decide *when* to search the web, *when* to generate an image, and *when* to simply converse.

## 🏗️ Architecture Stack
* **LLM Engine:** Google Gemini 2.5 Flash
* **Agent Framework:** LangChain / LangGraph
* **Search Engine:** Tavily API
* **Vision Model:** OpenAI DALL-E 3
* **Discord Wrapper:** `discord.py`

## 🚀 Quick Start (Local Setup)

### 1. Clone the repository

    git clone [https://github.com/akshitgajera1013/AI-Powered-Discord-Assistant.git](https://github.com/akshitgajera1013/AI-Powered-Discord-Assistant.git)
    
    cd AI-Powered-Discord-Assistant

2. Install Dependencies
   
Ensure you have Python 3.9+ installed, then run:

      pip install -r requirements.txt

3. Environment Variables
   
Create a .env file in the root directory and add your API keys. Never commit this file to GitHub

    DISCORD_API_KEY="your_discord_bot_token"
    GEMINI_API_KEY="your_google_gemini_key"
    OPENAI_API_KEY="your_openai_api_key"
    TAVILY_API_KEY="your_tavily_api_key"

4. Run the Bot
   
Start the background worker to bring your bot online:

    python bot.py

🎮 Usage
Once the bot is invited to your server and running, simply send a message in any channel the bot has access to.

Ask a question: "What is the weather like in Tokyo today?" (Triggers Tavily Search)

Generate art: "Generate an image of a futuristic cyberpunk city at night." (Triggers DALL-E 3)

Chat: "Write a short poem about coding." (Triggers Gemini)
