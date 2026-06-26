from config import llm
from nodes.rag import retrieve
from state import SupportState


SYSTEM_PROMPT = """
You are an Account Support Executive.

Answer the customer's question ONLY using the retrieved Company Policy and FAQ document.

If the answer is not available in the retrieved context, politely say that the information is unavailable.

Do not make up account procedures.
"""


def account_agent(state: SupportState):

    context = retrieve(state["query"])

    prompt = f"""
Retrieved Context:
{context}

Customer Query:
{state["query"]}
"""

    response = llm.invoke(
        [
            ("system", SYSTEM_PROMPT),
            ("human", prompt)
        ]
    )

    state["retrieved_context"] = context
    state["response"] = response.content

    return state