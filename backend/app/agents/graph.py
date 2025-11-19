from typing import TypedDict, List, Annotated
import operator
from langgraph.graph import StateGraph, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from app.core.config import settings
from app.agents.prompts import (
    LOGIC_REVIEWER_PROMPT,
    SECURITY_SPECIALIST_PROMPT,
    PERFORMANCE_SPECIALIST_PROMPT,
    SYNTHESIZER_PROMPT
)


class AgentState(TypedDict):
    diff: str
    reviews: Annotated[List[str], operator.add]


llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", google_api_key=settings.GOOGLE_API_KEY)


def logic_reviewer(state: AgentState):
    response = llm.invoke([
        SystemMessage(content=LOGIC_REVIEWER_PROMPT.format(diff=state['diff'])),
        HumanMessage(content="Review the code.")
    ])
    return {"reviews": [f"**Logic Review**:\n{response.content}"]}

def security_specialist(state: AgentState):
    response = llm.invoke([
        SystemMessage(content=SECURITY_SPECIALIST_PROMPT.format(diff=state['diff'])),
        HumanMessage(content="Review the code.")
    ])
    return {"reviews": [f"**Security Review**:\n{response.content}"]}

def performance_specialist(state: AgentState):
    response = llm.invoke([
        SystemMessage(content=PERFORMANCE_SPECIALIST_PROMPT.format(diff=state['diff'])),
        HumanMessage(content="Review the code.")
    ])
    return {"reviews": [f"**Performance Review**:\n{response.content}"]}

def synthesizer(state: AgentState):
    reviews_text = "\n\n".join(state['reviews'])
    response = llm.invoke([
        SystemMessage(content=SYNTHESIZER_PROMPT.format(reviews=reviews_text)),
        HumanMessage(content="Synthesize the review.")
    ])
    return {"reviews": [response.content]}


workflow = StateGraph(AgentState)


workflow.add_node("logic_reviewer", logic_reviewer)
workflow.add_node("security_specialist", security_specialist)
workflow.add_node("performance_specialist", performance_specialist)
workflow.add_node("synthesizer", synthesizer)



workflow.set_entry_point("logic_reviewer") 


workflow.add_edge("logic_reviewer", "security_specialist")
workflow.add_edge("security_specialist", "performance_specialist")
workflow.add_edge("performance_specialist", "synthesizer")
workflow.add_edge("synthesizer", END)


app_graph = workflow.compile()
