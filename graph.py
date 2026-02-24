from langgraph.graph import StateGraph, START, END
from state import AgentState
from nodes import plan_node, researcher_node, generation_node


# Initiate graph
workflow = StateGraph(AgentState)


# Add nodes and edges
workflow.add_node("planner", plan_node)
workflow.add_node("researcher", researcher_node)
workflow.add_node("generator", generation_node)

workflow.add_edge(START, "planner")
workflow.add_edge("planner", "researcher")
workflow.add_edge("researcher", "generator")
workflow.add_edge("generator", END)

app = workflow.compile()
