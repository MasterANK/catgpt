#<py-script src="/catgpt.py"></py-script>

from pyodide import create_proxy


def on_add_click(event):
    input_new_item = document.querySelector("#new-item")

    if input_new_item.value:
        child = document.createElement("li")
        child.innerText = input_new_item.value

        parent = document.querySelector("#shopping-list ul")
        parent.appendChild(child)

        input_new_item.value = ""

button = document.querySelector("button")
button.addEventListener("click", create_proxy(on_add_click))