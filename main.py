import spacy
import random
import re

# Loading spaCy English model with vectors
nlp = spacy.load("en_core_web_md")

# Possible User Intents
intents = {
    "greeting": [
        "hello", "hi", "hey there", "good morning", "good evening"
    ],
    "goodbye": [
        "bye", "goodbye", "see you later", "talk to you later"
    ],
    "thanks": [
        "thanks", "thank you", "much appreciated", "thank you very much"
    ],
    "name": [
        "what is your name", "who are you", "tell me your name"
    ],
    "age": [
        "how old are you", "what is your age", "tell me your age"
    ],
    "help": [
        "i need help", "can you help me", "assist me", "i want support"
    ],
    "math": [
        "what is 2 + 2", "calculate 5 * 3", "how much is 9 minus 4", "evaluate 10 / 2"
    ]
}

# Dictionary of Responses
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey!"],
    "goodbye": ["Goodbye!", "See you!", "Take care!"],
    "thanks": ["You're welcome!", "No problem!", "Glad to help!"],
    "name": ["I'm Chatty, your friendly NLP chatbot."],
    "age": ["I'm just a bunch of Python code — age doesn't apply!"],
    "help": ["Sure, ask me anything.", "I'm here to help!"],
    "unknown": ["I'm not sure what you mean. Can you rephrase?"],
}

# Function to detect if user asked for a math operation
def detect_math_expression(user_input):
    # Trying to extract and evaluate simple math operations
    pattern = r"([-+]?\d+(\.\d+)?)\s*([\+\-\*/])\s*([-+]?\d+(\.\d+)?)"
    match = re.search(pattern, user_input.replace("x", "*").replace("X", "*"))
    if match:
        try:
            expression = match.group(0)
            result = eval(expression)
            return f"The result is {result}"
        except:
            return "Sorry, I couldn't compute that."
    return None

# Detecting User intent using similarity
def detect_intent(user_input):
    user_doc = nlp(user_input)
    best_intent = "unknown"
    max_similarity = 0.65  # Here I have declared the Threshold value

    for intent, examples in intents.items():
        for example in examples:
            example_doc = nlp(example)
            similarity = user_doc.similarity(example_doc)
            if similarity > max_similarity:
                max_similarity = similarity
                best_intent = intent

    return best_intent

# Main chatbot loop and the function to handle user input
def chatbot():
    print("Chatbot: Hello! I'm Chatty. Ask me anything, or type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Chatbot:", random.choice(responses["goodbye"]))
            break

        # Check for math expression
        math_result = detect_math_expression(user_input)
        if math_result:
            print("Chatbot:", math_result)
            continue

        # Else, use NLP intent detection
        intent = detect_intent(user_input)
        response = random.choice(responses.get(intent, responses["unknown"]))
        print("Chatbot:", response)

# Run the chatbot if this script is executed directly
if __name__ == "__main__":  
    chatbot()