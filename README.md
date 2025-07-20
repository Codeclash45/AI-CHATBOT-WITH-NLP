COMPANY : CODTECH IT SOLUTIONS

NAME : Souvik Shomenath Dutta

INTERN I'D : CT06DH660

DOMAIN : Python Programming

DURATION : 4 WEEKS

MENTOR : NEELA SANTOSH

DESCRIPTION : 

# PROJECT TITLE : AI Chatbot With NLP

Project Overview
This project implements a rule-based and similarity-driven Natural Language Processing (NLP) chatbot named "Chatty." The primary goal of Chatty is to engage in basic conversations with users by understanding their intent and providing relevant responses. It leverages spaCy's en_core_web_md model for semantic similarity comparisons to detect user intentions and a regular expression-based approach for handling simple mathematical operations. The chatbot is designed to provide immediate, contextually appropriate answers for predefined intents like greetings, farewells, gratitude, and general inquiries about itself, while also attempting to perform basic calculations.

How It Works
Chatty's functionality is structured around several key components:

Intent Definitions and Responses: The chatbot is initialized with a predefined set of user intents (e.g., "greeting", "goodbye", "math", "help"). Each intent is associated with a list of example phrases that represent that intention. Correspondingly, a responses dictionary holds a variety of pre-scripted replies for each detected intent. This allows the chatbot to provide varied and natural-sounding responses.

Mathematical Expression Detection: Before performing NLP intent detection, the chatbot first attempts to identify if the user's input contains a simple mathematical expression. A regular expression (re module) is used to find patterns like "number operator number" (e.g., "2 + 2", "5 * 3"). If a match is found, the eval() function is used to compute the result, and this result is returned as the chatbot's response. This direct approach ensures quick and accurate handling of numerical queries without relying on semantic understanding.

NLP Intent Detection (Semantic Similarity): If no mathematical expression is detected, the chatbot proceeds to determine the user's intent using NLP.

spaCy Model Loading: The en_core_web_md model from spaCy is loaded. This model includes pre-trained word vectors, which are crucial for calculating semantic similarity between pieces of text.

User Input Processing: The user's input is processed by spaCy to create a Doc object, which contains tokenized words, linguistic features, and access to word vectors.

Similarity Comparison: The detect_intent function iterates through each predefined intent and its example phrases. For each example phrase, it calculates the semantic similarity between the user's input Doc object and the example phrase's Doc object using user_doc.similarity(example_doc).

Thresholding: A max_similarity threshold (set at 0.65) is used to determine if a detected similarity is strong enough to confidently assign an intent. If the highest similarity found is below this threshold, the intent defaults to "unknown."

Best Intent Selection: The intent with the highest similarity score above the threshold is chosen as the best_intent.

Response Generation: Once the best_intent is determined (either through math detection or NLP similarity), the chatbot retrieves a random response from the responses dictionary corresponding to that intent. If the intent is "unknown" (meaning no strong similarity was found), a generic "I'm not sure what you mean" response is provided.

Main Chatbot Loop: The chatbot() function initiates an interactive loop where it continuously prompts the user for input. It first checks for 'quit' commands to gracefully exit. For each user input, it first tries to detect a math expression, then falls back to NLP intent detection. The appropriate response is then printed to the console, allowing for a continuous conversation.

Conclusion

This "Chatty" chatbot project provides a foundational understanding of building interactive conversational agents using Python and NLP techniques. By combining rule-based pattern matching for numerical operations with spaCy's powerful semantic similarity for intent recognition, the chatbot can handle a variety of user queries. While simple, it demonstrates core concepts such as natural language understanding, response generation, and basic dialogue management. Future enhancements could involve expanding the intent library, incorporating more sophisticated dialogue flows, integrating external APIs for real-time information, and implementing machine learning models for more robust and scalable intent classification beyond just semantic similarity thresholds. This project serves as an excellent stepping stone for developing more complex and intelligent conversational AI systems.

