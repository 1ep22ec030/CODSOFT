# CODSOFT Task 1: Rule-Based Chatbot

This repository contains **Task 1** of the CODSOFT Artificial Intelligence Internship: a simple chatbot that responds to user messages using predefined rules and pattern matching.

## Project Overview

The chatbot is a console-based Python application. It reads the user's input, checks for matching keywords or patterns, and returns an appropriate response.

This project demonstrates the basic idea of conversation flow and rule-based Artificial Intelligence.

## Features

- Responds to greetings like `hello`, `hi`, and `hey`
- Answers simple questions about Artificial Intelligence
- Explains Machine Learning
- Tells the current date and time
- Tells a simple joke
- Handles unknown questions with a fallback response
- Ends the chat when the user types `bye`, `exit`, or `quit`

## Technologies Used

- Python
- Regular expressions
- Python standard library

## Concepts Used

- Rule-based AI
- Pattern matching
- Basic Natural Language Processing idea
- Conditional response generation
- Conversation loop

## Project Structure

```text
task1_chatbot/
|-- README.md
|-- chatbot.py
```

## Requirements

- Python 3.10 or newer
- No external libraries required

## How to Run

Open PowerShell or Command Prompt inside this folder and run:

```bash
python chatbot.py
```

If you are running from the main `codsoft` folder, use:

```bash
python task1_chatbot/chatbot.py
```

On Windows PowerShell, this also works:

```powershell
python task1_chatbot\chatbot.py
```

## Sample Output

```text
CodBot: Hello! Type 'bye' to end the chat.
You: hello
CodBot: Hello! I am a simple rule-based chatbot. How can I help you?
You: what is artificial intelligence
CodBot: Artificial Intelligence is a field of computer science where machines perform tasks that usually need human intelligence.
You: tell me a joke
CodBot: Why did the computer go to the doctor? Because it had a virus.
You: bye
CodBot: Goodbye! Thanks for chatting.
```

## How It Works

1. The program takes input from the user.
2. The input is converted to lowercase.
3. The chatbot checks the input against predefined regular expression patterns.
4. If a matching pattern is found, the chatbot returns the related response.
5. If no pattern matches, the chatbot returns a fallback message.
6. The chat continues until the user types an exit command.

## Test Cases

| Input | Expected Output |
| --- | --- |
| `hello` | Greeting response |
| `what is artificial intelligence` | AI explanation |
| `machine learning` | Machine Learning explanation |
| `tell me a joke` | Joke response |
| `time` | Current date and time |
| `bye` | Chatbot exits |
| Random unknown input | Fallback response |

## Internship Task Requirement

**Task:** Build a simple chatbot that responds to user inputs based on predefined rules. Use if-else statements or pattern matching techniques to identify user queries and provide appropriate responses.

This implementation satisfies the requirement by using pattern matching with regular expressions and predefined responses.

## Author

Created by **Deiva** for the CODSOFT Artificial Intelligence Internship.
