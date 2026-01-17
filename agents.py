from state import AgentState
from llm import answer_with_context
from search import retrieve_context

def retrieval_agent(state: AgentState) -> AgentState:
    state["context"] = retrieve_context(state["question"])
    return state

def validation_agent(state: AgentState) -> AgentState:
    if not state["context"]:
        state["answer"] = "Insufficient data to answer this question."
    return state

def answer_agent(state: AgentState) -> AgentState:
    state["answer"] = answer_with_context(
        state["question"], state["context"]
    )
    return state
