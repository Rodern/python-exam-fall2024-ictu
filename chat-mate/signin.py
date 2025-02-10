import flet as ft
from flet import *
from db.inventoryplusdb import *
from helpers.datahelpers import *
from hashlib import sha256

def login_user(username: str, password: str):
    try:
        data_store = create_inventory_db()
        hashed_password = sha256(password.encode()).hexdigest()
        user = data_store.read_record('user', f'username = "{username}"') #'userId = "1"')
        if user:
            if hashed_password == user[2]:
                return True, user
            else:
                return False, "Wrong password"
        else:
            return False, f"No user with username: {username}."
    except Exception as e:
        return False, e

def UserLogin(page: ft.Page):
    global user_logged_in

    def signin_clicked(e):
        global user_logged_in

        # Validate input fields
        if not username_field.value or not password_field.value:
            page.snack_bar = ft.SnackBar(
                ft.Text("All fields are required!", color=ft.Colors.RED)
            )
            page.snack_bar.open = True
            page.update()
        else:
            username = username_field.value.strip()
            password = password_field.value.strip()

            success, result = login_user(username, password)
            if success:
                page.snack_bar = ft.SnackBar(
                    ft.Text("Login successfull!", color=ft.Colors.BLUE)
                )
                page.snack_bar.open = True
                page.update()

                username_field.value = ""
                password_field.value = ""

                page.user_id = result[0]
                page.user_logged_in = True
                
                SaveSignin(result[0])

                page.update()
                page.go('/home')
            else:
                page.snack_bar = ft.SnackBar(
                    ft.Text(result, color=ft.Colors.RED)
                )
                page.snack_bar.open = True
                page.update()


    username_field = ft.TextField(label="Username", width=610, color=ft.Colors.with_opacity(1, "#1f1f1f"), bgcolor=ft.Colors.WHITE, border_radius=5, border=ft.InputBorder.OUTLINE)
    password_field = ft.TextField(label="Password", password=True, can_reveal_password=True, width=610, color=ft.Colors.with_opacity(1, "#1f1f1f"), bgcolor=ft.Colors.WHITE, border_radius=5, border=ft.InputBorder.OUTLINE)
    signin_button = ft.ElevatedButton(text="Signin", on_click=lambda e: signin_clicked(e), height=36, width=200, bgcolor=ft.Colors.with_opacity(1, "#0078D4"), color=ft.Colors.WHITE, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)))
    signup = ft.TextButton(text="Create account", on_click=lambda _: page.go('/registration'))

    return ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [ft.Text("Account login", size=32, color=ft.Colors.with_opacity(1, "#1f1f1f"))],
                    alignment=ft.MainAxisAlignment.START,
                    width=610,
                ),
                username_field,
                password_field,
                ft.Row(
                    [signin_button],
                    alignment=ft.MainAxisAlignment.END,
                    width=610,
                ),
                ft.Row(
                    [
                        ft.Container(height=100),  # Add some space
                        ft.Text("Don't have an account?", color=ft.Colors.with_opacity(1, "#1f1f1f")),
                        signup
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    width=610,
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
