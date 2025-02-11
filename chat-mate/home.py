import flet as ft
from datetime import datetime
from db.crud import get_user, session
from db.models import User, Message
from helpers.datahelpers import *

def Home(page: ft.Page):
    page.title = "ChatMate - Instant Messaging"
    page.bgcolor = "#FFFFFF"

    GetLogin(page)

    # Header section
    header = ft.Row(
        [
            ft.Image(
                src=r"C:\Users\Rodern\git-repos\python-exam-fall2024-ictu\chat-mate\assets\ictu-logo.png",  # Replace with your app logo URL
                width=40,
                height=40,
                visible=False,
            ),
            ft.Text("Chats", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.with_opacity(1, "#009c74")),
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=10,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # Function to get the last message from a sender to the current user
    def get_last_message(user_id, sender_id):
        message = session.query(Message).filter(
            (Message.sender_id == sender_id) & (Message.receiver_id == user_id)
        ).order_by(Message.timestamp.desc()).first()
        return message

    # Function to get chat list
    def get_chat_list(user_id):
        messages = session.query(Message).filter(Message.receiver_id == user_id).all()
        senders = {message.sender_id for message in messages}
        chat_list = []
        for sender_id in senders:
            sender = session.query(User).filter(User.user_id == sender_id).first()
            last_message = get_last_message(user_id, sender_id)
            if last_message:
                chat_list.append({
                    "contact": sender,
                    "last_message": last_message.content,
                    "timestamp": last_message.timestamp.strftime("%I:%M %p")
                })
        return chat_list

    # Get the current user's chat list
    user_id = page.user_id
    chat_list = get_chat_list(user_id)

    # Chats container
    chats_container = ft.ListView(
        controls=[
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.CircleAvatar(
                            foreground_image_url=chat["contact"].profile_picture_url,
                            radius=30,
                        ),
                        ft.Column(
                            controls=[
                                ft.Text(chat["contact"].user_name, size=16, weight=ft.FontWeight.BOLD),
                                ft.Text(chat["last_message"], size=12, color=ft.Colors.GREY),
                            ],
                            alignment=ft.MainAxisAlignment.START,
                            spacing=5,
                            expand=True,
                        ),
                        ft.Column(
                            controls=[
                                ft.Text(chat["timestamp"], size=12, color=ft.Colors.GREY, text_align=ft.TextAlign.END),
                            ],
                            alignment=ft.MainAxisAlignment.END,
                            horizontal_alignment=ft.CrossAxisAlignment.END,
                            spacing=5,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    spacing=10,
                ),
                padding=ft.padding.all(10),
                margin=ft.margin.symmetric(vertical=5),
                border_radius=ft.border_radius.all(10),
                bgcolor=ft.Colors.with_opacity(1, "#f2f2f2"),
                on_click=lambda e, contact=chat["contact"]: page.go(f"/chat/{contact.user_name}?avatar={contact.profile_picture_url}"),
            ) for chat in chat_list
        ],
        expand=True,
        padding=ft.padding.all(10),
    )

    # Floating action button to open people page
    floating_button = ft.FloatingActionButton(
        icon=ft.icons.PEOPLE,
        right=10,
        bottom=10,
        bgcolor=ft.Colors.with_opacity(1, "#009c74"),
        on_click=lambda _: page.go('/people'),
    )

    return ft.Container(
        content=ft.Stack(
            [
                ft.Column(
                    controls=[
                        header,
                        ft.Divider(height=1, color=ft.Colors.GREY),
                        chats_container,
                    ],
                    expand=True,
                ),
                floating_button,
            ],
            expand=True,
            alignment=ft.alignment.bottom_right,
        ),
        expand=True,
    )
