
import datetime

# Function to get time-based greeting
def get_time_greeting():
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        return "Good morning"
    elif 12 <= current_hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"

# Function to generate response
def get_bot_response(user_input):
    user_input = user_input.lower()
    responses = {
        "hello": "Hi there!",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "what is your name": "I am ChatBot, your virtual assistant.",
        "who made you": "I was created by a Python programmer as part of the CodeAlpha internship.",
        "bye": "Goodbye! Talk to you later.",
        "exit": "Session ended. See you!"
    }
    return responses.get(user_input, "I'm not sure how to respond to that.")

# Function to start chatbot
def chatbot():
    print("🤖 Welcome to ChatBot!")
    name = input("What's your name? ")
    print(f"{get_time_greeting()}, {name}! Let's chat. (Type 'exit' or 'bye' to end.)\n")

    chat_history = []  # Track conversation

    while True:
        user_input = input(f"{name}: ")
        chat_history.append(f"{name}: {user_input}")

        response = get_bot_response(user_input)
        chat_history.append(f"ChatBot: {response}")
        print(f"ChatBot: {response}")

        if user_input.lower() in ["bye", "exit"]:
            break

    # Optional: Save chat history to file
    with open("chat_history.txt", "w") as f:
        for line in chat_history:
            f.write(line + "\n")
    print("📝 Chat history saved to 'chat_history.txt'.")

# Run the bot
chatbot()
