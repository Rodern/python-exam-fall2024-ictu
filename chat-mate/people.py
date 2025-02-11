import flet as ft
from datetime import datetime
from db.crud import get_user, session
from db.models import User, Message

def People(page: ft.Page):
    page.title = "ChatMate - People"
    page.bgcolor = "#FFFFFF"

    # Header section
    header = ft.Row(
        [
            ft.Image(
                src=r"C:\Users\Rodern\git-repos\python-exam-fall2024-ictu\chat-mate\assets\ictu-logo.png",  # Replace with your app logo URL
                width=40,
                height=40,
                visible=False,
            ),
            ft.Text("People", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.with_opacity(1, "#009c74")),
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=10,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # Function to get the list of people
    def get_people_list(user_id):
        return session.query(User).filter(User.user_id != user_id).all()

    # Get the current user's ID
    user_id = page.user_id
    people_list = get_people_list(user_id)

    # People container
    people_container = ft.ListView(
        controls=[
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.CircleAvatar(
                            foreground_image_url=person.profile_picture_url,
                            radius=30,
                        ),
                        ft.Column(
                            controls=[
                                ft.Text(person.user_name, size=16, weight=ft.FontWeight.BOLD),
                                ft.Text(person.phone_number, size=12, color=ft.Colors.GREY),
                            ],
                            alignment=ft.MainAxisAlignment.START,
                            spacing=5,
                            expand=True,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    spacing=10,
                ),
                padding=ft.padding.all(10),
                margin=ft.margin.symmetric(vertical=5),
                border_radius=ft.border_radius.all(10),
                bgcolor=ft.Colors.with_opacity(1, "#f2f2f2"),
                on_click=lambda e, person=person: page.go(f"/chat/{person.user_name}?avatar={person.profile_picture_url}"),
            ) for person in people_list
        ],
        expand=True,
        padding=ft.padding.all(10),
    )

    return ft.Container(
        content=ft.Column(
            controls=[
                header,
                ft.Divider(height=1, color=ft.Colors.GREY),
                people_container,
            ],
            expand=True,
        ),
        expand=True,
    )
