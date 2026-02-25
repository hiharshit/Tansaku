# Tansaku (探索)

An autonomous AI research agent built with LangGraph that performs real-time web retrieval and synthesizes findings into structured responses.

## Overview

Tansaku takes a research question, breaks it down into search queries, gathers relevant information from the web using Tavily, and synthesizes the results into a coherent answer using Ollama (Llama 3).

## How It Works

1. **Analyze** - Decomposes your research question into actionable search queries
2. **Gather** - Retrieves relevant information from the web
3. **Synthesize** - Produces a well-structured response based on gathered content

## Tech Stack

- **LangGraph** - Orchestrates the agent workflow with state management and node-based execution
- **LangChain Ollama** - Provides integration with Ollama for local LLM inference
- **Tavily** - Delivers real-time web search results for research
- **python-dotenv** - Loads environment variables from `.env` files

## Requirements

- Python 3.11+
- Ollama running locally with Llama 3 model
- Tavily API key

## Setup

1. Install dependencies:

   ```bash
   uv sync
   ```

2. Copy `.env.example` to `.env` and add your API key:

   ```bash
   cp .env.example .env
   # Edit .env and add your TAVILY_API_KEY
   ```

3. Ensure Ollama is running with Llama 3:
   ```bash
   ollama run llama3
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
