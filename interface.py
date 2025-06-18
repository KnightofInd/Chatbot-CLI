from modal_loader import load_chatbot_model
from chat_memory import ChatMemory

def main():
    print("🤖 Welcome to Local CLI Chatbot! Type /exit to quit.\n")
    
    # Load the model pipeline
    chatbot = load_chatbot_model()
    
    # Initialize memory (e.g., 5 recent exchanges)
    memory = ChatMemory(max_turns=5)

    while True:
        user_input = input("User: ").strip()

        if user_input.lower() == "/exit":
            print("Bot: Exiting chatbot. Goodbye!")
            break

        # Combine memory context + current input
        context = memory.get_context() + f"User: {user_input}\nBot:"
        
        # Generate response
        response = chatbot(context, max_new_tokens=100, do_sample=True)[0]['generated_text']
        
        # Extract just the new bot response (after the last 'Bot:')
        bot_reply = response.split("Bot:")[-1].strip().split("User:")[0].strip()

        # Save the turn in memory
        memory.add_turn(user_input, bot_reply)

        # Print bot response
        print(f"Bot: {bot_reply}\n")

if __name__ == "__main__":
    main()
