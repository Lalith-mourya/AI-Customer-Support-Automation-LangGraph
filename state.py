from typing import TypedDict


class SupportState(TypedDict):

    customer_name: str

    query: str

    intent: str

    department: str

    retrieved_context: str

    approval_required: bool

    approved: bool

    response: str

    conversation_history: list[str]