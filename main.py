from graph import app
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    print("Initializing Agent...")

    user_task = input("What would you like to research? ")

    initial_state = {
        "task": user_task,
        "plan": [],
        "content": [],
        "revision_number": 0,
        "max_revisions": 2,
    }

    # run graph
    print(f"Executing: {initial_state['task']}")

    for output in app.stream(initial_state):
        for node_name, state_update in output.items():
            print(f"\n---Completed: {node_name} ---")

            if node_name == "planner":
                print(f"Queries: {state_update.get('plan')}")
            elif node_name == "generator":
                print(f"Output:\n{state_update.get('draft')}")
