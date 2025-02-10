""" 
import flet as ft
from flet import *

def About(page: Page):
    content = ft.Container(
        [
            ft.Container(
                [
                    ft.Text(
                        value="About",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.with_opacity(1, "#1f1f1f"),
                        text_align=ft.TextAlign.CENTER
                    )
                ]
            )
        ],
        width= 710,
        bgcolor=ft.Colors.WHITE,
        expand=True,
    )
    return content """

import flet as ft
from flet import *
from db.inventoryplusdb import *
from helpers.datahelpers import *
from hashlib import sha256

def About(page: ft.Page):

    return ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [ft.Text("About STACK", size=32, color=ft.Colors.with_opacity(1, "#1f1f1f"))],
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
