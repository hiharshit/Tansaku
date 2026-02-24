import os
import json
from langchain_ollama import ChatOllama
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

# Model setup
model_json = ChatOllama(model="llama3", format="json")

model_text = ChatOllama(model="llama3", temperature=0)

tavily = TavilySearchResults(max_results=3)


# Planner node
def plan_node(state):
    print("---ANALYZING TASK---")
    task = state["task"]

    steps = [task]

    prompt = f"""
    You are a Research Analyst.
    Your task is to decompose the user's request into actionable search queries.
    
    USER REQUEST: {task}
    
    Return a JSON object with a single key 'steps' which is a list of strings.
    Example: {{ "steps": ["search query 1", "search query 2"] }}
    """

    try:
        response = model_json.invoke([HumanMessage(content=prompt)])
        content = response.content.strip()

        if "```" in content:
            content = content.split("```")[1].replace("json", "").strip()

        plan_data = json.loads(content)
        steps = plan_data.get("steps", [task])

    except Exception as e:
        print(f"JSON Parsing Error: {e}")

    print(f"Execution steps: {steps}")
    return {"plan": steps}


# Researcher node
def researcher_node(state):
    print("---GATHERING INFO---")
    plan = state["plan"]
    content = []

    for query in plan:
        print(f"Querying: {query}")
        try:
            results = tavily.invoke(query)
            for result in results:
                content.append(result["content"])
        except Exception as e:
            print(f"Search error for {query}: {e}")

    return {"content": content}


# Generator node
def generation_node(state):
    print("---SYNTHESIZING---")
    content = "\n\n".join(state["content"])
    task = state["task"]

    prompt = f"""
You are a Content Synthesizer.
Write a detailed response to the user's question based ONLY on the provided context.

CONTEXT : {content}

QUESTION : {task}
"""

    response = model_text.invoke([HumanMessage(content=prompt)])
    return {"draft": response.content}
