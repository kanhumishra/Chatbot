
import json
import pickle
import random
import string

import numpy as np
import tensorflow as tf
from nltk.stem import WordNetLemmatizer

# Load trained model and saved vocabulary
model = tf.keras.models.load_model("chatbot.keras")

with open("words.pkl", "rb") as file:
    words = pickle.load(file)

with open("classes.pkl", "rb") as file:
    classes = pickle.load(file)

with open("intents.json", "r", encoding="utf-8") as file:
    intents = json.load(file)

lemmatizer = WordNetLemmatizer()
ignore_chars = set(string.punctuation)


def clean_sentence(sentence):
    tokens = sentence.lower().split()

    cleaned = []
    for token in tokens:
        token = token.strip(string.punctuation)
        if token:
            cleaned.append(lemmatizer.lemmatize(token))

    return cleaned


def bag_of_words(sentence):
    sentence_words = clean_sentence(sentence)

    bag = [0] * len(words)

    for word in sentence_words:
        if word in words:
            bag[words.index(word)] = 1

    return np.array(bag, dtype=np.float32)


def get_response(message):
    if not message or not message.strip():
        return "Please enter a message."

    input_vector = bag_of_words(message)

    # Avoid predicting from an entirely unknown message
    if not np.any(input_vector):
        return "Sorry, I don't understand that yet. Try another message."

    predictions = model.predict(
        np.array([input_vector]), verbose=0
    )[0]

    predicted_index = int(np.argmax(predictions))
    confidence = float(predictions[predicted_index])

    # Basic confidence threshold
    if confidence < 0.50:
        return "Sorry, I'm not sure I understand. Could you rephrase?"

    predicted_tag = classes[predicted_index]

    for intent in intents["intents"]:
        if intent["tag"] == predicted_tag:
            return random.choice(intent["responses"])

    return "Sorry, I couldn't find a suitable response."


# Test the chatbot in the terminal
if __name__ == "__main__":
    print("Chatbot is ready! Type 'exit' to stop.")

    while True:
        message = input("You: ").strip()

        if message.lower() == "exit":
            print("Bot: Goodbye!")
            break

        print("Bot:", get_response(message))
