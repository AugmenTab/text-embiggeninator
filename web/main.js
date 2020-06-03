button = document.getElementById("button")
message = document.getElementById("message")

function display() {
    message.classList.add("unhide")
    setTimeout(undisplay, 2000)
}

function undisplay() {
    message.classList.remove("unhide")
}

button.addEventListener("click", display)