from typing import TypedDict, Annotated, List
import operator


class AgentState(TypedDict):
    task: str
    plan: List[str]
    draft: str
    critique: str

    content: Annotated[List[str], operator.add]
    revision_number: int
    max_revisions: int
