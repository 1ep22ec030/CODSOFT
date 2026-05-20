from datetime import datetime
import re


RESPONSES = [
    (r"\b(hi|hello|hey)\b", "Hello! I am a simple rule-based chatbot. How can I help you?"),
    (r"\b(your name|who are you)\b", "I am CodBot, a beginner AI chatbot created for the CODSOFT internship task."),
    (r"\b(help|what can you do)\b", "I can answer simple questions about AI, tell the time, tell a joke, and chat with you."),
    (r"\b(ai|artificial intelligence)\b", "Artificial Intelligence is a field of computer science where machines perform tasks that usually need human intelligence."),
    (r"\b(machine learning|ml)\b", "Machine learning is a part of AI where computers learn patterns from data instead of being programmed with every rule."),
    (r"\b(joke|funny)\b", "Why did the computer go to the doctor? Because it had a virus."),
    (r"\b(thank you|thanks)\b", "You're welcome!"),
]


def get_response(user_input):
    text = user_input.lower().strip()

    if re.search(r"\b(time|date|today)\b", text):
        return f"The current date and time is {datetime.now().strftime('%d %B %Y, %I:%M %p')}."

    for pattern, response in RESPONSES:
        if re.search(pattern, text):
            return response

    return "I am not sure about that yet. Try asking about AI, machine learning, time, or jokes."


def main():
    print("CodBot: Hello! Type 'bye' to end the chat.")

    while True:
        user_input = input("You: ")

        if re.search(r"\b(bye|exit|quit)\b", user_input.lower()):
            print("CodBot: Goodbye! Thanks for chatting.")
            break

        print(f"CodBot: {get_response(user_input)}")


if __name__ == "__main__":
    main()

