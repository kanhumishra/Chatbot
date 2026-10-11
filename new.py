
import random
import json
import pickle
import numpy as np
import tensorflow as tf
import nltk

from nltk.stem import WordNetLemmatizer

# Download the required NLTK resources (if needed)
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("wordnet")

lemmatizer = WordNetLemmatizer()

# Load intents
with open("intents.json", "r", encoding="utf-8") as file:
    intents = json.load(file)

words = []
classes = []
documents = []
ignore_chars = ["?", "!", ".", ","]

# 1. Tokenization and collecting vocabulary
for intent in intents["intents"]:
    for pattern in intent["patterns"]:

        word_list = nltk.word_tokenize(pattern.lower())

        # Remove punctuation
        word_list = [
            word for word in word_list
            if word not in ignore_chars
        ]

        words.extend(word_list)
        documents.append((word_list, intent["tag"]))

        if intent["tag"] not in classes:
            classes.append(intent["tag"])

# 2. Clean and sort vocabulary and classes
words = [
    lemmatizer.lemmatize(word)
    for word in words
]

words = sorted(set(words))
classes = sorted(set(classes))

# Save vocabulary and classes
with open("words.pkl", "wb") as file:
    pickle.dump(words, file)

with open("classes.pkl", "wb") as file:
    pickle.dump(classes, file)

# 3. Create training data
training = []

for word_patterns, tag in documents:

    # Create bag-of-words vector
    bag = [0] * len(words)

    for word in word_patterns:
        word = lemmatizer.lemmatize(word.lower())

        if word in words:
            bag[words.index(word)] = 1

    # One-hot encode the target intent
    output_row = [0] * len(classes)
    output_row[classes.index(tag)] = 1

    training.append((bag, output_row))

# Shuffle the training data
random.shuffle(training)

# Convert features and labels into NumPy arrays
trainX = np.array(
    [item[0] for item in training],
    dtype=np.float32
)

trainY = np.array(
    [item[1] for item in training],
    dtype=np.float32
)

print("Input shape:", trainX.shape)
print("Output shape:", trainY.shape)

# 4. Build the neural network
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(len(words),)),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dense(
        len(classes),
        activation="softmax"
    )
])

# 5. Configure optimizer and loss
sgd = tf.keras.optimizers.SGD(
    learning_rate=0.01,
    momentum=0.9,
    nesterov=True
)

model.compile(
    loss="categorical_crossentropy",
    optimizer=sgd,
    metrics=["accuracy"]
)

# 6. Train the model
history = model.fit(
    trainX,
    trainY,
    epochs=200,
    batch_size=5,
    verbose=1
)

# 7. Save the trained model
model.save("chatbot.keras")

print("successful")
