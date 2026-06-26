from config import llm
from state import SupportState


SYSTEM_PROMPT = """
You are the Customer Support Supervisor.

Your job is to review the draft response and produce the FINAL response that will be sent to the customer.

Rules:
1. Return ONLY the final customer response.
2. Do NOT explain your review.
3. Do NOT say things like:
   - "The response is correct"
   - "The response is professional"
   - "I suggest"
   - "The generated response..."
4. Improve grammar, clarity, and professionalism if needed.
5. Do not add information that is not present in the retrieved context.
"""


def supervisor(state: SupportState):

    response = llm.invoke(
        [
            ("system", SYSTEM_PROMPT),
            (
                "human",
                f"""
Customer Query:

{state["query"]}

Retrieved Context:

{state["retrieved_context"]}

Draft Response:

{state["response"]}

Return ONLY the final customer response.
"""
            )
        ]
    )

    state["response"] = response.content

    return state