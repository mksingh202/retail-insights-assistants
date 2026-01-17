from typing import TypedDict, List

class AgentState(TypedDict, total=False):
    question: str
    context: List[str]
    answer: str
