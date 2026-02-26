import datetime
import random

print("🤖 Advanced ChatBot: Hello! I am your AI assistant.")
print("Type 'bye' to exit.\n")

user_name = ""

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs! 😄",
    "Why was the computer cold? Because it forgot to close Windows! 😂",
    "Why do Java developers wear glasses? Because they don't C#! 🤣"
]

while True:
    user_input = input("You: ").lower()

    # Greeting
    if "hello" in user_input or "hi" in user_input:
        print("🤖 ChatBot: Hello! Nice to meet you.")
    
    # Asking name
    elif "my name is" in user_input:
        user_name = user_input.replace("my name is", "").strip()
        print(f"🤖 ChatBot: Nice to meet you, {user_name.title()}!")
    
    elif "your name" in user_input:
        print("🤖 ChatBot: I am Advanced Python ChatBot 2.0 🚀")
    
    # Time
    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("🤖 ChatBot: Current time is", current_time)
    
    # Date
    elif "date" in user_input:
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        print("🤖 ChatBot: Today's date is", current_date)
    
    # Joke
    elif "joke" in user_input:
        print("🤖 ChatBot:", random.choice(jokes))
    
    # Simple Calculator
    elif "+" in user_input or "-" in user_input or "*" in user_input or "/" in user_input:
        try:
            result = eval(user_input)
            print("🤖 ChatBot: The answer is", result)
        except:
            print("🤖 ChatBot: Please enter a valid math expression.")
    
    # Personal response
    elif "how are you" in user_input:
        print("🤖 ChatBot: I'm doing great! Thanks for asking 😊")
    
    # If name already stored
    elif "who am i" in user_input:
        if user_name:
            print(f"🤖 ChatBot: You are {user_name.title()}!")
        else:
            print("🤖 ChatBot: I don't know your name yet. Tell me using 'My name is ___'")
    
    # Exit
    elif user_input == "bye":
        print("🤖 ChatBot: Goodbye! Have a productive day 🚀")
        break
    
    # Default response
    else:
        responses = [
            "Interesting! Tell me more.",
            "I'm not sure I understand.",
            "Can you explain that differently?",
            "That sounds cool!"
        ]
        print("🤖 ChatBot:", random.choice(responses))