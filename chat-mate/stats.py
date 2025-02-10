import flet as ft
from flet import *

def Stats(page: ft.Page):
    page.title = "STACK - Inventory and Finance Management"
    
    # Header section
    header = ft.Row(
        [
            ft.Image(
                src=r"assets/favicon.png",  # Replace with your app logo URL
                width=80,
                height=80,
            ),
            ft.Column(
                [
                    ft.Text("STACK", size=24, weight=ft.FontWeight.BOLD, color="#FFFFFF"),
                    ft.Text("Where Smart Management Meets Simplicity", size=16, weight=ft.FontWeight.NORMAL, color="#FFFFFF"),
                ],
                spacing=5,
                alignment=ft.MainAxisAlignment.START,
            ),
        ],
        spacing=20,
        alignment=ft.MainAxisAlignment.START,
    )

    # Tabs for navigation
    tab_content = ft.Tabs(
        selected_index=0,
        tabs=[
            ft.Tab(text="Statistics"),
        ],
        expand=True,
    )

    stats_finances = ft.Container(
        ft.Column(
            [
                ft.Text("Finances", size=20, weight=ft.FontWeight.BOLD),
                ft.Container(
                    ft.Column(
                        [
                            ft.Text("Monthly Balance: 2500000 FCFA", size=16),
                            ft.Text("Monthly Expenses: 450000 FCFA", size=16),
                            ft.Text("Monthly Income: 450000 FCFA", size=16),
                            ft.Text("Monthly Savings : 150000 ", size=16),
                        ],
                        spacing=10,
                    ),
                    bgcolor="#EDEDED",
                    padding=10,
                    border_radius=5,
                    gradient=ft.LinearGradient(
                    begin=ft.alignment.top_center,
                    end=ft.alignment.bottom_center,
                    colors=["#001F67","#000E2F"]),
                ),
            ],
            spacing=15,
        ),
        padding=15,
    )


    # Statistiques content
    stats_inventaire = ft.Container(
        ft.Column(
            [
                ft.Text(" Inventory", size=20, weight=ft.FontWeight.BOLD),
                ft.Container(
                    ft.Column(
                        [
                            ft.Text("Total Value: 1500000 FCFA", size=16),
                            ft.Text("Number Of Items: 188", size=16),
                            
                        ],
                        spacing=10,
                    ),
                    bgcolor="#EDEDED",
                    padding=10,
                    border_radius=5,
                    gradient=ft.LinearGradient(
                    begin=ft.alignment.top_center,
                    end=ft.alignment.bottom_center,
                    colors=["#001F67","#000E2F"]),
                ),
            ],
            spacing=15,
        ),
        padding=15,
    )


    # Page content
    return ft.Column(
        [
            header,
            ft.Divider(height=1, color="#D3D3D3"),
            tab_content,
            stats_finances,
            stats_inventaire,
        ],
        expand=True,
    )
