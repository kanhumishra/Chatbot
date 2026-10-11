
const form = document.getElementById("chat-form");
const input = document.getElementById("message");
const chatBox = document.getElementById("chat-box");
const sendButton = document.getElementById("send-button");

function addMessage(text, sender) {
    const message = document.createElement("div");
    message.className = `message ${sender}`;

    // Use textContent to display text safely.
    message.textContent = text;

    chatBox.appendChild(message);
    chatBox.scrollTop = chatBox.scrollHeight;
}

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const message = input.value.trim();

    if (!message) return;

    addMessage(message, "user");
    input.value = "";
    sendButton.disabled = true;

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Request failed");
        }

        addMessage(data.response, "bot");
    } catch (error) {
        addMessage(
            "Sorry, I couldn't connect to the chatbot. Please try again.",
            "bot"
        );
        console.error(error);
    } finally {
        sendButton.disabled = false;
        input.focus();
    }
});
