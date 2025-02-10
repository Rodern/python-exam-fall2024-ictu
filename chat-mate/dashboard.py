import flet as ft
from flet import*

def Dashboard(page: ft.Page):
    page.title = "Stack - Dashboard"
    # page.bgcolor = "white"
    # page.bgcolor = "#3e78ff"
    # page.scroll=ft.ScrollMode.ALWAYS
    
    # Dashboard Header
    header = ft.Row(
        [
            ft.Text(
                "Dashboard",
                size=28,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.WHITE,
            ),
            ft.TextField(
                hint_text="What are you looking for?",
                width=320,
                border_radius=10,
                bgcolor="#001F67",
                color=ft.Colors.WHITE,
                icon=ft.Icons.SEARCH,
            ),
            ft.Row(
                [
                    ft.Icon(ft.Icons.NOTIFICATIONS, color=ft.Colors.WHITE),
                    ft.Icon(ft.Icons.ACCOUNT_CIRCLE, color=ft.Colors.WHITE),
                ],
                spacing=20,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
        spacing=20,
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

    # Info Cards
    cards = [
        ("Total Amount", "187,000frs", ft.Icons.ATTACH_MONEY),
        ("Amount Deposit", "21,000frs", ft.Icons.SAVINGS),
        ("Amount Spent", "7,000frs", ft.Icons.SAVINGS),
        ("Expected Amount", "81,000frs", ft.Icons.ACCOUNT_BALANCE),
    ]

    info_cards = ft.Row(
        [
            ft.Container(
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_center,
                    end=ft.alignment.bottom_center,
                    colors=["#000E2F","#3e78ff"],
                ),
                content=ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Icon(icon, size=30, color=ft.Colors.WHITE),
                                ft.Text(
                                    title,
                                    size=16,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.WHITE70,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                        ft.Text(
                            value,
                            size=24,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.WHITE,
                        ),
                    ],
                    spacing=10,
                ),
                bgcolor="#001F67",
                padding=20,
                border_radius=8,
                width=250,
                height=120,
            )
            for title, value, icon in cards
        ],
        scroll='auto',
        spacing=20,
        alignment=ft.MainAxisAlignment.START,
    )

    # Graph Placeholder
    graph_placeholder = ft.Container(
        content=ft.Image(
            src=r"assets/chart_3.jpg",  # Replace with your app logo URL
            fit=ft.ImageFit.COVER,
            expand=True,
        ),
        bgcolor="#001F67",
        border_radius=10,
        expand=True,
    )

    # History & Upcoming Section
    history_items = [
        ("House Rent", "-4500frs"),
        ("Health", "-45000frs"),
        ("Car Expense", "-85000frs"),
        ("Deposited", "+95000frs"),
    ]

    upcoming_items = [
        ("Deposit", "+4500frs"),
        ("House Rent", "-4500frs"),
        ("Deposit", "+4700frs"),
        ("Health", "-450frs"),
    ]

    def create_list_section(title, items):
        return ft.Column(
            [
                ft.Text(title, size=20, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
                ft.ListView(
                    [
                        ft.Container(
                            ft.Row(
                                [
                                    ft.Text(item, size=16, color=ft.Colors.WHITE70),
                                    ft.Text(amount, size=16, color=ft.Colors.WHITE),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            ),
                            padding=15,
                            bgcolor="#001F67",
                            border_radius=8,
                            margin=5,
                        )
                        for item, amount in items
                    ],
                    height=300,
                    expand=True,
                ),
            ],
            spacing=10,
        )

    history_section = create_list_section("History", history_items)
    upcoming_section = create_list_section("Upcoming", upcoming_items)

    # Main Layout
    return ft.Row(
        [
            # Main Content
            ft.Container(
                ft.Column(
                    [
                        header,
                        ft.Container(
                            info_cards,
                            margin=ft.margin.symmetric(vertical=20),
                        ),
                        ft.Row(
                            [
                                graph_placeholder,
                                ft.Container(
                                    ft.Column(
                                        [
                                            history_section,
                                            upcoming_section
                                        ],
                                        spacing=2
                                    ),
                                    width=300,
                                ),
                            ],
                            spacing=20,
                            alignment=ft.MainAxisAlignment.START,
                            vertical_alignment=ft.CrossAxisAlignment.START,
                            height=300,
                            scroll=ft.ScrollMode.ALWAYS
                        ),
                    ],
                    spacing=20,
                ),
                expand=True,
                padding=20,
            ),
        ],
        expand=True
    )
