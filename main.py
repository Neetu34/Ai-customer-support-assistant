import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from intent_classifier import classify_intent
from knowledge_base import knowledge_base
from prompts import SYSTEM_PROMPT


# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("OPENAI_API_KEY")


def main():

    if not api_key:
        print("Error: OPENAI_API_KEY is not configured.")
        print("Please add your API key to the .env file.")
        return

    try:

        llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0.3,
            api_key=api_key
        )

    except Exception as e:
        print(f"Error initializing the AI model: {e}")
        return

    conversation_history = []

    print("=" * 60)
    print("      AI CUSTOMER SUPPORT ASSISTANT")
    print("=" * 60)
    print("Type 'exit' to end the conversation.")
    print()

    while True:

        try:

            user_query = input("Customer: ").strip()

            # Handle empty input
            if not user_query:
                print("Assistant: Please enter a question.")
                continue

            # Exit condition
            if user_query.lower() in ["exit", "quit", "bye"]:
                print("Assistant: Thank you for contacting us. Goodbye!")
                break

            # Classify intent
            intent = classify_intent(user_query)

            # Get knowledge base information
            knowledge = knowledge_base.get(
                intent,
                knowledge_base["General Query"]
            )

            # Convert knowledge to text
            knowledge_text = "\n".join(
                f"{key}: {value}"
                for key, value in knowledge.items()
            )

            # Convert conversation history
            history_text = "\n".join(
                f"Customer: {customer}\nAssistant: {assistant}"
                for customer, assistant in conversation_history[-5:]
            )

            # Create prompt
            prompt = SYSTEM_PROMPT.format(
                intent=intent,
                knowledge=knowledge_text,
                history=history_text,
                query=user_query
            )

            # Get response from LLM
            response = llm.invoke(prompt)

            assistant_response = response.content

            print(f"\nIntent: {intent}")
            print(f"Assistant: {assistant_response}\n")

            # Save conversation
            conversation_history.append(
                (user_query, assistant_response)
            )

        except KeyboardInterrupt:
            print("\nAssistant: Goodbye!")
            break

        except Exception as e:
            print(
                "Assistant: Sorry, I encountered an error "
                "while processing your request."
            )
            print(f"Error details: {e}")


if __name__ == "__main__":
    main()