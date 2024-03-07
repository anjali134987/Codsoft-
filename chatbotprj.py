print("Welcome to the Chat Bot!")

while True:
    user_input = input("You: ").lower()

    if "hello" in user_input:
        print("Bot: Hello! How can I assist you?")
    elif "how are you?" in user_input:
        print("bot: Iam fine ,what about you?")
    elif "what is your name" in user_input:
        print("bot: I am a chatbot")
    elif "goodbye" in user_input:
        print("Bot: Goodbye! Have a great day!")
        break
    else:
        print("Bot: I'm sorry, I didn't understand that.")
