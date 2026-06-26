from sqlite3 import connect

from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.sqlite import SqliteSaver

from state import SupportState

from nodes.classifier import classify_intent
from nodes.router import route_department

from nodes.sales_agent import sales_agent
from nodes.technical import technical_agent
from nodes.billing_agent import billing_agent
from nodes.account_agent import account_agent
from nodes.memory import memory_agent

from nodes.approval import (
    check_approval,
    approval_router
)

from nodes.human_review import human_review
from nodes.supervisor import supervisor
from nodes.final_response import save_history


builder = StateGraph(SupportState)


builder.add_node("classifier", classify_intent)

builder.add_node("sales", sales_agent)
builder.add_node("technical", technical_agent)
builder.add_node("billing", billing_agent)
builder.add_node("account", account_agent)
builder.add_node("memory", memory_agent)

builder.add_node("approval", check_approval)
builder.add_node("human", human_review)

builder.add_node("supervisor", supervisor)

builder.add_node("save", save_history)


builder.add_edge(START, "classifier")


builder.add_conditional_edges(
    "classifier",
    route_department,
    {
        "Sales": "sales",
        "Technical": "technical",
        "Billing": "billing",
        "Account": "account",
        "Memory": "memory"
    }
)


builder.add_edge("sales", "approval")
builder.add_edge("technical", "approval")
builder.add_edge("billing", "approval")
builder.add_edge("account", "approval")


builder.add_conditional_edges(
    "approval",
    approval_router,
    {
        "human": "human",
        "supervisor": "supervisor"
    }
)


builder.add_edge("human", "supervisor")

builder.add_edge("memory", "save")

builder.add_edge("supervisor", "save")

builder.add_edge("save", END)


connection = connect(
    "memory.db",
    check_same_thread=False
)

memory = SqliteSaver(connection)

graph = builder.compile(
    checkpointer=memory
)