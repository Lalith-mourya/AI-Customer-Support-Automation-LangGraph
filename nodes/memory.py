from state import SupportState


def memory_agent(state: SupportState):

    history = state.get("conversation_history", [])

    if not history:
        state["response"] = (
            "I couldn't find any previous customer interactions."
        )
        return state

    previous_issue = history[-1]

    state["response"] = (
        f"Your previous support issue was:\n\n{previous_issue}"
    )

    return state