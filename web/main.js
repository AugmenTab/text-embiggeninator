const button = document.getElementById("button");
const message = document.getElementById("message");
const data = document.getElementById("data");

function display() {
    message.classList.add("unhide");
    setTimeout(undisplay, 2000);
}

function undisplay() {
    message.classList.remove("unhide");
}

function embiggeninateText() {
    eel.embiggeninate_text(data.value)(function(ret) {console.log(ret)})
}

button.addEventListener("click", display)