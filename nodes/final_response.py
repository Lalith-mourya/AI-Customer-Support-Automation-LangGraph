from state import SupportState


def save_history(state: SupportState):

    history = state.get(

        "conversation_history",

        []

    )

    history.append(

        state["query"]

    )

    state["conversation_history"] = history

    return state