print("=" * 50)
print("      Welcome to the Rule-Based Chatbot")
print("=" * 50)

while True:
    user = input("\nYou: ").lower()

    if user == "hello":
        print("Bot: Hello! Welcome.")

    elif user == "hi":
        print("Bot: Hi! How can I help you?")

    elif user == "how are you":
        print("Bot: I am doing great. Thanks for asking!")

    elif user == "your name":
        print("Bot: My name is RuleBot.")

    elif user == "what is ai":
        print("Bot: AI stands for Artificial Intelligence.")

    elif user == "who created you":
        print("Bot: I was created using Python.")

    elif user == "thank you":
        print("Bot: You're welcome!")

    elif user == "help":
        print("Bot: You can ask me about AI, my name, or greet me.")

    elif user == "bye":
        print("Bot: Goodbye! Have a wonderful day.")
        break

    else:
        print("Bot: Sorry, I don't understand that question.")