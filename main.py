from agent import create_agent
from db import get_database
from rag import get_retriever

def setup():
    # Build vector DB on first run
    db = get_database()
    print("Building vector database (first time only)...")
    get_retriever(db, rebuild=True)

def main():
    # setup()  # uncomment this to rebuild the vector DB

    agent = create_agent()

    print("🛒 Supermarket AI Assistant Ready!")
    print("Type 'exit' to quit\n")

    while True:
        try:
            query = input("User: ")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if query.lower() == "exit":
            break

        try:
            response = agent.run(query)
            print(f"Bot: {response}\n")
        except Exception as e:
            print(f"Bot: Sorry, I encountered an error: {e}\n")

if __name__ == "__main__":
    main()