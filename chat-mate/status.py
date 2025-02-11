import flet as ft
from flet import *

def Statuses(page: ft.Page):
    page.title = "ChatMate - Status"
    page.bgcolor = "#FFFFFF"

    # Header section
    header = ft.Row(
        [
            ft.Image(
                src=r"C:\Users\Rodern\git-repos\python-exam-fall2024-ictu\chat-mate\assets\ictu-logo.png",  # Replace with your app logo URL
                width=40,
                height=40,
            ),
            ft.Text("Status", size=16, weight=ft.FontWeight.BOLD),
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=10,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        # padding=ft.padding.all(10),
        #bgcolor="#0d7fd7",
    )

    # Status container
    status_container = ft.Column(
        expand=True,
        scroll="auto",
        controls=[]
    )

    # Function to add a status to the list
    def add_status(name, time, image_url):
        status = ft.Container(
            content=ft.Row(
                controls=[
                    ft.CircleAvatar(
                        foreground_image_url=image_url,
                        radius=30,
                    ),
                    ft.Column(
                        controls=[
                            ft.Text(name, size=16, weight=ft.FontWeight.BOLD),
                            ft.Text(time, size=12, color=ft.Colors.GREY),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
                spacing=10,
            ),
            padding=10,
            margin=ft.margin.symmetric(vertical=5),
            bgcolor=ft.Colors.GREY_100,
            border_radius=ft.border_radius.all(10),
        )
        status_container.controls.append(status)
        page.update()

    # Add some sample statuses
    add_status("You", "Today, 4:30 PM", "https://avatars.githubusercontent.com/u/54691684?v=4")
    add_status("Donald Trump", "Today, 3:15 PM", "https://th.bing.com/th/id/OIP.TFV8UijE_HpTBu5rQpBksQHaHZ?rs=1&pid=ImgDetMain")
    add_status("John Doe", "Yesterday, 8:45 PM", "https://avatars.githubusercontent.com/u/5041459?s=88&v=4")

    return ft.Container(
        content=ft.Column(
            controls=[
                header,
                ft.Divider(height=1, color=ft.Colors.GREY),
                status_container,
            ],
            expand=True,
        ),
        padding=10,
        expand=True,
    )
