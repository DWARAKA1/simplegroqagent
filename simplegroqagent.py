import os
from groq import Groq

def main():
    # Get GROQ_API_KEY from environment
    if "GROQ_API_KEY" not in os.environ:
        print("Please set your GROQ_API_KEY environment variable")
        return

    # Initialize Groq client
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    print("🤖 Groq Assistant is ready! Type 'exit' to quit.")
    
    while True:
        # Get user input
        user_input = input("\nYou: ")
        
        if user_input.lower() == 'exit':
            print("Goodbye! 👋")
            break
        
        # Get assistant response
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful AI assistant."
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ],
            model="mixtral-8x7b-32768",
            temperature=0.7,
        )
        
        # Print the response
        print(f"\nAssistant: {chat_completion.choices[0].message.content}")

if __name__ == "__main__":
    main()
