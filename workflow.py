from state import AgentState
from langgraph.graph import StateGraph, START, END
from agents import retrieval_agent, validation_agent, answer_agent

def build_workflow():
    graph = StateGraph(AgentState)

    graph.add_node("retrieve", retrieval_agent)
    graph.add_node("validate", validation_agent)
    graph.add_node("answer", answer_agent)

    graph.add_edge(START, "retrieve")
    graph.add_edge("retrieve", "validate")
    graph.add_edge("validate", "answer")
    graph.add_edge("answer", END)
   
    return graph.compile()
