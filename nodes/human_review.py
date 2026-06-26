from state import SupportState


def human_review(state: SupportState):

    print("\n ------------- HUMAN REVIEW ------------\n")

    print("Customer Query:\n")

    print(state["query"])

    print("\nGenerated Response:\n")

    print(state["response"])

    decision = input(

        "\nApprove this response? (yes/no): "

    ).strip().lower()

    if decision == "yes":

        state["approved"] = True

    else:

        state["approved"] = False

        state["response"] = (

            "Your request has been forwarded to a human support executive."

        )

    return state