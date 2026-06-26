from config import llm
from state import SupportState


SYSTEM_PROMPT = """
You are an Intent Classification Agent.

Classify the customer query into EXACTLY ONE of these categories:

Sales
Technical
Billing
Account

Return ONLY the category name.
"""


def classify_intent(state: SupportState):

    query = state["query"].lower()

    memory_keywords = [
        "previous",
        "last",
        "earlier",
        "before",
        "history",
        "conversation"
    ]

    if any(keyword in query for keyword in memory_keywords):
        state["intent"] = "Memory"
        print("Detected Intent: Memory")
        return state

    response = llm.invoke(
        [
            ("system", SYSTEM_PROMPT),
            ("human", state["query"])
        ]
    )

    intent = response.content.strip()

    valid = [
        "Sales",
        "Technical",
        "Billing",
        "Account"
    ]

    for item in valid:
        if item.lower() in intent.lower():
            state["intent"] = item
            print("Detected Intent:", item)
            return state

    raise ValueError(f"Invalid intent returned: {intent}")