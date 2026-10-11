# 🤖 NLP Intent-Based Chatbot

An intent-based chatbot built using **Python, Natural Language Processing (NLP), TensorFlow/Keras, and Flask**. The chatbot classifies user messages into predefined intents using a trained neural network and returns an appropriate response through a web-based chat interface.

## 🚀 Features

- **Intent Classification:** Predicts user intent using a trained neural network.
- **Text Preprocessing:** Cleans and lemmatizes user input.
- **Bag-of-Words Representation:** Converts text into numerical features for model prediction.
- **Predefined Responses:** Selects responses based on the predicted intent.
- **Web Interface:** Interactive chatbot frontend built with HTML, CSS, and JavaScript.
- **Flask Backend:** Processes chat messages and returns responses through a REST endpoint.
- **Model Persistence:** Loads the trained model and saved vocabulary and class labels.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| TensorFlow / Keras | Neural network training and inference |
| NLTK | Text preprocessing and lemmatization |
| NumPy | Numerical operations |
| Flask | Backend web application |
| HTML, CSS, JavaScript | Chat interface |
| Git & GitHub | Version control and project hosting |
| Render | Web application deployment |

## 📂 Project Structure

```text
Chatbot/
├── app.py                 # Flask application
├── chat.py                # Chatbot prediction and response logic
├── new.py                 # Model training script
├── intents.json           # Intent patterns and predefined responses
├── chatbot.keras          # Trained neural network model
├── words.pkl              # Saved vocabulary
├── classes.pkl            # Saved intent classes
├── requirements.txt       # Python dependencies
├── .python-version        # Python runtime version
├── .gitignore             # Files excluded from Git
├── templates/
│   └── index.html         # Chat interface
└── static/
    ├── style.css          # Interface styling
    └── script.js          # Frontend chat functionality
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Chatbot.git
cd Chatbot
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a virtual environment

Python 3.11 is recommended for this project.

```bash
python -m venv chatbot
```

Activate the environment on Windows:

```cmd
chatbot\Scripts\activate
```

On macOS or Linux:

```bash
source chatbot/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Download NLTK resources

If these resources are not already installed, run:

```bash
python -c "import nltk; nltk.download('wordnet'); nltk.download('punkt'); nltk.download('punkt_tab')"
```

### 5. Run the application

```bash
python app.py
```

Open the following URL in your browser:

**http://127.0.0.1:5000**

The trained model and supporting files must be present in the project root for inference to work.

## 🧠 How It Works

1. **User Input:** The user enters a message through the web interface.
2. **Preprocessing:** The input is converted into tokens and lemmatized.
3. **Feature Extraction:** A bag-of-words vector is created using the saved vocabulary.
4. **Intent Prediction:** The trained neural network predicts the most likely intent.
5. **Response Selection:** The application selects an appropriate response from `intents.json`.
6. **Response Display:** Flask returns the response, and JavaScript displays it in the chat interface.

## 📊 Model Training

The model is trained using predefined intent patterns stored in `intents.json`.

The training process includes:

- Loading intent patterns and their corresponding labels.
- Tokenizing and lemmatizing text.
- Building a vocabulary and intent class list.
- Converting sentences into bag-of-words features.
- Training a neural network for intent classification.
- Saving the trained model and preprocessing artifacts for inference.

To retrain the model, activate the virtual environment and run:

```bash
python new.py
```

Retraining may overwrite the existing model and vocabulary files.

6. Deploy the service and open the generated URL.

Ensure that `.python-version` specifies a compatible Python version and that `requirements.txt` includes all required runtime dependencies, including Flask, TensorFlow, NumPy, NLTK, and Gunicorn.

## 🔮 Future Improvements

- Expand the dataset with more diverse intent patterns.
- Improve generalization through additional training data and validation.
- Add confidence thresholds and a fallback response for unknown intents.
- Introduce conversation history and contextual responses.
- Add automated tests for prediction and API endpoints.
- Improve accessibility and mobile responsiveness.
- Add CI/CD and model performance monitoring.

## 👨‍💻 Author

**Kanhu Mishra**

- GitHub: [YOUR_USERNAME](https://github.com/YOUR_USERNAME)
- LinkedIn: [YOUR_LINKEDIN_PROFILE](https://www.linkedin.com/)

## 📄 License

This project is available for educational and portfolio purposes. Add a license file if you intend to distribute it under a specific open-source license.
