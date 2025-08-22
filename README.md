# 💬 Gemma Chat Agent

Gemma Chat Agent is an **AI-powered conversational assistant** built on top of the **LangChain framework** and deployed through a **Gradio web interface**.  
It integrates the **Gemma model via Ollama** as its core large language model (LLM), while extending its intelligence with practical tools like:

- 🔍 **DuckDuckGo Search** → fetches the latest web information in real-time.  
- 📖 **Wikipedia Lookup** → provides factual, structured knowledge from Wikipedia.  
- ➗ **Calculator** → evaluates math expressions on the fly.  

Unlike a basic chatbot, this agent can **combine reasoning with external tools**, making it capable of answering both conversational queries (“Who is Ada Lovelace?”) and dynamic ones (“What is 23*89?” or “What’s trending in AI news?”).  

## ✨ Features
- AgentType: **OPENAI_FUNCTIONS** for reliable tool-calling
- Tools: DuckDuckGo search, Wikipedia, Calculator
- Simple memory (chat history)
- Gradio UI (`ChatInterface`) with browser auto-open

The system is built with:
- **LangChain Agents** (using `AgentType.OPENAI_FUNCTIONS`) to seamlessly decide when to call which tool.  
- **Custom memory handling** to keep track of ongoing conversations.  
- **Gradio’s ChatInterface**, offering a clean browser-based UI that launches instantly.  

This makes it an ideal **starter project** for experimenting with:
- 🤖 Tool-augmented LLM agents  
- 🧱 Building LangChain applications  
- 🌐 Local inference with Ollama + Gemma  
- 🎨 Deploying quick ML apps with Gradio  

> Think of it as a lightweight research assistant: it can talk, look things up, calculate, and explain — all in one chat window.

## 🚀 Quickstart

### 1) Requirements
- Python 3.9+
- [Ollama](https://ollama.ai) installed locally
- Gemma model downloaded:
  ```bash
  ollama pull gemma
