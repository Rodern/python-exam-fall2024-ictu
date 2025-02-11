import flet as ft
from datetime import datetime
from db.crud import add_message, session
from db.dtos import MessageDto
from pydantic import BaseModel
import sys
sys.path.append('./db')
from db.models import User, Message, Status, Group

def Chat(page: ft.Page, name: str, avatar: str):
    page.title = "ChatMate - Instant Messaging"
    page.bgcolor = "#FFFFFF"

    # Header section
    header = ft.Row(
        [
            ft.IconButton(
                icon=ft.icons.ARROW_BACK,
                icon_color=ft.Colors.with_opacity(1, "#009c74"),
                bgcolor=ft.Colors.with_opacity(1, "#FFFFFF"),
                on_click=lambda e: page.go('/chats'),
            ),
            ft.CircleAvatar(
                foreground_image_url=avatar,
                radius=30,
                width=40,
                height=40,
            ),
            ft.Text(name, size=16, color=ft.Colors.with_opacity(1, "#2a2d2e"), weight=ft.FontWeight.BOLD),
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=10,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # Messages container
    messages_container = ft.Column(
        expand=True,
        scroll="auto",
        controls=[]
    )

    # Function to add a message to the chat
    def add_message_to_chat(content, sender, timestamp):
        message = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(content, size=16, color=ft.Colors.BLACK),
                    ft.Text(timestamp, size=12, color=ft.Colors.GREY, text_align=ft.TextAlign.LEFT),
                ],
                expand=False,
                alignment=ft.MainAxisAlignment.END if sender == "me" else ft.MainAxisAlignment.START,
            ),
            expand=False,
            padding=10,
            margin=ft.margin.symmetric(vertical=5),
            bgcolor=ft.Colors.LIGHT_GREEN_100 if sender == "me" else ft.Colors.LIGHT_BLUE_100,
            border_radius=ft.border_radius.all(10),
            alignment=ft.alignment.center_right if sender == "me" else ft.alignment.center_left,
        )
        messages_container.controls.append(message)
        page.update()

    # Function to load messages from the database
    def load_messages():
        sender_id = page.user_id
        receiver = session.query(User).filter(User.user_name == name).first()
        if receiver:
            receiver_id = receiver.user_id
            messages = session.query(Message).filter(
                ((Message.sender_id == sender_id) & (Message.receiver_id == receiver_id)) |
                ((Message.sender_id == receiver_id) & (Message.receiver_id == sender_id))
            ).order_by(Message.timestamp.asc()).all()
            for message in messages:
                sender = "me" if message.sender_id == page.user_id else "them"
                add_message_to_chat(message.content, sender, message.timestamp.strftime("%H:%M"))

    # Load messages when the chat page is opened
    load_messages()

    # Function to send a message
    def send_message(e):
        content = message_input.value.strip()
        if content:
            sender_id = page.user_id
            receiver = session.query(User).filter(User.user_name == name).first()
            if receiver:
                receiver_id = receiver.user_id
                message_dto = MessageDto(
                    content=content,
                    timestamp=datetime.now(),
                    sender_id=sender_id,
                    receiver_id=receiver_id,
                    group_id=0  # Ensure group_id is None when not applicable
                )
                add_message(message_dto)
                add_message_to_chat(content, "me", datetime.now().strftime("%H:%M"))
                message_input.value = ""
                page.update()

    # Text input for sending messages
    message_input = ft.TextField(
        hint_text="Message...",
        expand=True,
        border_color=ft.Colors.GREY_400,
        border_radius=ft.border_radius.all(16),
        bgcolor=ft.Colors.GREY_200,
    )

    # Send button
    send_button = ft.IconButton(
        icon=ft.icons.SEND,
        icon_color=ft.Colors.WHITE,
        bgcolor=ft.Colors.with_opacity(1, "#009c74"),
        on_click=send_message,
    )

    # Input row
    input_row = ft.Row(
        controls=[message_input, ft.Row(width=10), send_button],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10,
    )

    return ft.Container(
        content=ft.Column(
            controls=[
                header,
                ft.Divider(height=1, color=ft.Colors.GREY),
                messages_container,
                input_row,
            ],
            expand=True,
        ),
        padding=10,
        expand=True,
    )
