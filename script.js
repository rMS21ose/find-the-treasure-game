let step = 1;

function submitChoice() {
    const input = document.getElementById("user-input").value;
    if (!input && step !== 1) return;

    fetch('/play', {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ step: step, choice: input })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("game-text").innerText = data.result;

        const questionBox = document.getElementById("question-box");
        if (data.question && data.choices) {
            questionBox.innerHTML = `<strong>${data.question}</strong><br>Choices: ${data.choices.join(" / ")}`;
        } else {
            questionBox.innerHTML = ""; // clear if no further questions
        }

        if (!data.gameOver) {
            step++;
        } else {
            document.getElementById("user-input").disabled = true;
        }

        if (data.win) {
            step++;
        }

        document.getElementById("user-input").value = "";
        document.getElementById("user-input").focus();
    });
}
