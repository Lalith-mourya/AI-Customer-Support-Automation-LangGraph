from state import SupportState


HIGH_RISK_REQUESTS = [

    "refund",

    "cancel subscription",

    "subscription cancellation",

    "account closure",

    "close account",

    "compensation",

    "escalate",

    "management"

]


def check_approval(state: SupportState):

    query = state["query"].lower()

    state["approval_required"] = any(

        keyword in query

        for keyword in HIGH_RISK_REQUESTS

    )

    return state


def approval_router(state: SupportState):

    if state["approval_required"]:

        return "human"

    return "supervisor"