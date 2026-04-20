from agent import create_agent
from db import get_database
from rag import get_retriever

def setup():
    # Build vector DB on first run
    db = get_database()
    print("Building vector database (first time only)...")
    get_retriever(db, rebuild=True)

def main():
    setup()  # comment this after first run

    agent = create_agent()

    print("🛒 Supermarket AI Assistant Ready!")
    print("Type 'exit' to quit\n")

    while True:
        query = input("User: ")

        if query.lower() == "exit":
            break

        response = agent.run(query)

        print(f"Bot: {response}\n")

if __name__ == "__main__":
    main()