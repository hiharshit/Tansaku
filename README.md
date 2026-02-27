# Tansaku (探索)

Tansaku (探索) means "explore" or "search" in Japanese - reflecting the agent's purpose of autonomously researching and gathering information.

## Overview

Tansaku takes a research question, breaks it down into search queries, gathers relevant information from the web using Tavily, and synthesizes the results into a coherent answer using Ollama.

## How It Works

1. **Analyze** - Decomposes your research question into actionable search queries
2. **Gather** - Retrieves relevant information from the web
3. **Synthesize** - Produces a well-structured response based on gathered content

## Tech Stack

- **LangGraph** - Orchestrates the agent workflow with state management and node-based execution
- **LangChain Ollama** - Provides integration with Ollama for local LLM inference (gemma3:1b)
- **Tavily** - Delivers real-time web search results for research
- **python-dotenv** - Loads environment variables from `.env` files

## Prerequisites

- [Python 3.11+](https://www.python.org/downloads/)
- [Ollama](https://ollama.com/) - Get the gemma3:1b model: `ollama pull gemma3:1b`
- [Tavily API Key](https://app.tavily.com/) - Sign up for free API access

## Requirements

- Python 3.11+
- Ollama with gemma3:1b model
- Tavily API key

## Setup

1. Install dependencies:

   ```bash
   uv sync
   ```

2. Rename `.env.example` to `.env` and add your API key:

   ```bash
   cp .env.example .env
   # Edit .env and add your TAVILY_API_KEY
   ```

3. Pull the gemma3:1b model and start Ollama:
   ```bash
   ollama pull gemma3:1b
   ollama run gemma3:1b
   ```

## Usage

Run the agent:

```bash
python main.py
```

Enter your research question when prompted. The agent will analyze the task, gather information, and produce a synthesized response.

## Project Structure

- `main.py` - Entry point
- `graph.py` - LangGraph workflow definition
- `nodes.py` - Agent nodes (planner, researcher, generator)
- `state.py` - State schema for the agent
- `.env.example` - Environment variable template
- `pyproject.toml` - Project dependencies
