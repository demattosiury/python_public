import flet as ft
from datetime import datetime as dt


strftime = "%d/%m/%Y %H:%M:%S"


def main(page):

    title_main_page = ft.Text("Flet Chat")

    # Chat
    chat_col = ft.Column(auto_scroll=True)

    def postMessage(message):
        chat_col.controls.append(message)
        page.update()

    # Websocket
    page.pubsub.subscribe(postMessage)

    def sendMessage(event):
        now = dt.now().strftime(strftime)
        text = ft.Text("{} {} : {}".format(nickname_input.value, now, send_input.value))
        page.pubsub.send_all(text)
        send_input.value = ""
        page.update()

    # Send message input
    send_input = ft.TextField(label="Send a menssage...", on_submit=sendMessage)

    def connect(event):
        page.remove(title_main_page)
        page.remove(call_dialog_button)
        dialog_connect.open = False

        page.add(chat_col)
        user = ft.Text("{} connected...".format(nickname_input.value))
        page.pubsub.send_all(user)
        page.add(send_input)

        page.update()

    # Dialog
    title_dialog = ft.Text("Connect Dialog")
    nickname_input = ft.TextField(label="Nickname")
    connect_button = ft.ElevatedButton("Connect", on_click=connect)
    dialog_connect = ft.AlertDialog(
        title=title_dialog,
        content=nickname_input,
        actions=[connect_button],
    )

    def callDialog(event):
        page.dialog = dialog_connect
        dialog_connect.open = True
        page.update()

    # Call dialog Button
    call_dialog_button = ft.ElevatedButton("Call dialog", on_click=callDialog)

    page.add(title_main_page)
    page.add(call_dialog_button)


ft.app(main, view=ft.WEB_BROWSER)
