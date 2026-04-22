const API = "http://127.0.0.1:5000";

function sendNotification() {
    const user = document.getElementById("user").value;
    const message = document.getElementById("message").value;

    fetch(`${API}/send`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user, message })
    })
    .then(res => res.json())
    .then(() => loadNotifications());
}

function loadNotifications() {
    fetch(`${API}/notifications`)
    .then(res => res.json())
    .then(data => {
        const list = document.getElementById("list");
        list.innerHTML = "";
        data.forEach(n => {
            const li = document.createElement("li");
            li.innerText = `${n.user}: ${n.message}`;
            list.appendChild(li);
        });
    });
}

window.onload = loadNotifications;
