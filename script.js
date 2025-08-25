const chatBox = document.getElementById("chat-box");
const inputField = document.getElementById("user-input");

function addMessage(text, sender) {
    const msg = document.createElement("div");
    msg.classList.add("message", sender);
    msg.innerText = text;
    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight; // auto scroll
}

async function sendMessage() {
    const text = inputField.value.trim();
    if (!text) return;

    addMessage(text, "user");
    inputField.value = "";

    try {
        const res = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: text
            }),
        });

        const data = await res.json();
        addMessage("👻 Ghost: " + data.reply, "ghost");
    } catch (err) {
        addMessage("⚠️ Error: Cannot connect to Ghost server.", "ghost");
        console.error(err);
    }
}