import random
import re


class ChatBot:
    def __init__(self):
        self.name = "Nova"

        self.responses = {
            "greeting": [
                "Hello! 👋 I'm Nova. How are you feeling today?",
                "Hi there! 😊 What would you like to talk about?",
                "Hey! I'm Nova, your text and speech analysis assistant."
            ],

            "how_are_you": [
                "I'm doing great! Thanks for asking. 😊",
                "I'm ready to chat and analyze your messages!",
                "I'm doing well. What is on your mind?"
            ],

            "thanks": [
                "You're welcome! 😊",
                "Anytime!",
                "Glad I could help!"
            ],

            "goodbye": [
                "Goodbye! 👋 Have a wonderful day!",
                "See you later! 😊",
                "Take care!"
            ],

            "help": [
                "You can tell me how you feel, ask me a question, or type a sentence for analysis.",
                "Try saying: 'I am happy today' or 'I am feeling stressed.'"
            ]
        }

        self.keywords = {
            "greeting": [
                "hello", "hi", "hey", "hai", "good morning",
                "good afternoon", "good evening"
            ],

            "how_are_you": [
                "how are you", "how are u", "how do you feel",
                "are you okay"
            ],

            "thanks": [
                "thank you", "thanks", "thank", "thx"
            ],

            "goodbye": [
                "bye", "goodbye", "see you", "good night"
            ],

            "help": [
                "help", "what can you do", "how can you help"
            ]
        }

    def clean_text(self, text):
        text = text.lower()
        text = re.sub(r"[^\w\s]", "", text)
        return text.strip()

    def get_response(self, user_input):

        cleaned = self.clean_text(user_input)

        if not cleaned:
            return "Please say or type something. 😊"

        # Check predefined intents
        for intent, keywords in self.keywords.items():

            for keyword in keywords:

                if keyword in cleaned:
                    return random.choice(self.responses[intent])

        # Simple question detection
        if cleaned.endswith("?"):
            return self.answer_question(cleaned)

        # Emotion-based responses
        if any(word in cleaned for word in [
            "happy", "great", "excited", "wonderful",
            "good", "awesome", "joy"
        ]):
            return "That's wonderful to hear! 😊 What made you feel this way?"

        if any(word in cleaned for word in [
            "sad", "unhappy", "depressed", "cry",
            "upset", "lonely"
        ]):
            return "I'm sorry you're feeling this way. 💙 Talking about it can sometimes help."

        if any(word in cleaned for word in [
            "angry", "mad", "furious", "annoyed"
        ]):
            return "It sounds like something is frustrating you. Take a breath and tell me what happened."

        if any(word in cleaned for word in [
            "stress", "stressed", "anxious", "anxiety",
            "worried", "nervous"
        ]):
            return "It sounds like you may be under some pressure. 🌱 Try taking a short break and tell me what's worrying you."

        if any(word in cleaned for word in [
            "tired", "exhausted", "sleepy"
        ]):
            return "You sound tired. 😴 Getting some rest might help."

        # Default response
        return self.default_response(cleaned)

    def answer_question(self, text):

        if "your name" in text:
            return f"My name is {self.name}. 🤖"

        if "who are you" in text:
            return "I'm Nova, a Python chatbot created for text and speech analysis."

        if "what can you do" in text:
            return "I can chat with you, analyze sentiment, detect emotions, and process speech."

        if "python" in text:
            return "Python is a great language for AI, NLP, automation and data science."

        return "That's an interesting question! I don't have a predefined answer yet, but you can analyze the text using the analysis panel."

    def default_response(self, text):

        responses = [
            "I understand. Tell me more about that.",
            "Interesting! What made you think about that?",
            "I see. Can you explain a little more?",
            "Thanks for sharing that with me.",
            "That's interesting. How do you feel about it?"
        ]

        return random.choice(responses)