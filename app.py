from graph import graph


config = {
    "configurable": {
        "thread_id": "customer_001"
    }
}


while True:

    query = input("\nCustomer: ")

    if query.lower() == "exit":
        break

    snapshot = graph.get_state(config)

    history = []

    if snapshot.values:

        history = snapshot.values.get(
            "conversation_history",
            []
        )

    state = {

        "customer_name": "David",

        "query": query,

        "intent": "",

        "department": "",

        "retrieved_context": "",

        "approval_required": False,

        "approved": False,

        "response": "",

        "conversation_history": history

    }

    result = graph.invoke(
        state,
        config=config
    )

    print("\n--------------------------------")

    print(result["response"])

    print("--------------------------------")