import flet as ft
from flet import *
from helpers.datahelpers import *
from hashlib import sha256

def About(page: ft.Page):

    return ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Image(
                            src=r"C:\Users\Rodern\git-repos\python-exam-fall2024-ictu\chat-mate\assets\chatmate-logo+text-square.png",  # Replace with your app logo URL
                            width=150,
                            height=150,
                        ),
                        ft.Text("About ChatMate", size=32, color=ft.Colors.with_opacity(1, "#1f1f1f"))
                    ],
                    spacing=20,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            width=610,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        ),
        bgcolor=ft.Colors.GREY_200,
        padding=ft.padding.all(20),
        border_radius=10,
    )
