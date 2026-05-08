# 🤖 AI-Powered Discord Assistant

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-FF4B4B.svg)](https://streamlit.io/)
[![LangGraph](https://img.shields.io/badge/Framework-LangGraph-green.svg)](https://python.langchain.com/)

An advanced, multi-modal autonomous agent capable of engaging in conversational reasoning, searching the live internet for up-to-date facts, and dynamically generating images. The architecture is deployed across two distinct interfaces: a **Discord Bot** (Background Worker) and a **Streamlit Web Dashboard** (Web UI).

## ✨ Core Features
* 🧠 **Advanced Reasoning:** Powered by Google's `Gemini 2.5 Flash` for high-speed, intelligent text generation.
* 🌐 **Live Web Search:** Integrated with the `Tavily API` to bypass standard LLM training data cut-offs and fetch real-time internet data.
* 🎨 **Image Generation:** Utilizes OpenAI's `DALL-E 3` to seamlessly generate and return images natively within the chat or Discord channel.
* 🔀 **Smart Routing:** Uses `LangGraph` (`create_react_agent`) to autonomously decide *when* to search the web, *when* to generate an image, and *when* to converse normally.

## 🏗️ Architecture Stack
* **LLM Engine:** Google Gemini
* **Agent Framework:** LangChain / LangGraph
* **Search Engine:** Tavily API
* **Vision Model:** OpenAI DALL-E 3
* **Frontends:** Streamlit (Web) & `discord.py` (Server)

## 🚀 Quick Start (Local Deployment)

### 1. Clone the repository
```bash
git clone [https://github.com/akshitgajera1013/AI-Powered-Discord-Assistant.git](https://github.com/akshitgajera1013/AI-Powered-Discord-Assistant.git)

cd AI-Powered-Discord-Assistant

2. Install Dependencies
pip install -r requirements.txt

3. Environment Variables
DISCORD_API_KEY="your_discord_bot_token"
GEMINI_API_KEY="your_google_gemini_key"
OPENAI_API_KEY="your_openai_api_key"
TAVILY_API_KEY="your_tavily_api_key"