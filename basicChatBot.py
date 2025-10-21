# Simple Rule-Based Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hi there! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "your name" in user_input:
        return "I'm ChatBot, your friendly assistant!"
    elif "thank" in user_input:
        return "You're welcome!"
    else:
        return "I'm not sure I understand. Can you say that differently?"

def main():
    print("ChatBot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("ChatBot: Goodbye! 👋")
            break
        response = chatbot_response(user_input)
        print("ChatBot:", response)

# Run the chatbot
if __name__ == "__main__":
    main()
