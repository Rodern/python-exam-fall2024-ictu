import flet as ft
from flet import *
from db.crud import get_user, session
from helpers.datahelpers import *
from hashlib import sha256
import sys
from pydantic import BaseModel
sys.path.append('./db')
from db.models import User, Message, Status, Group

def login_user(phone_number: str, password: str):
    try:
        hashed_password = sha256(password.encode()).hexdigest()
        user = session.query(User).filter(User.phone_number == phone_number).first()
        if user:
            if hashed_password == user.password:
                return True, user
            else:
                return False, "Wrong password"
        else:
            return False, f"No user with phone number: {phone_number}."
    except Exception as e:
        return False, str(e)

def UserLogin(page: ft.Page):
    def signin_clicked(e):
        # Validate input fields
        if not phone_number_field.value or not password_field.value:
            page.snack_bar = ft.SnackBar(
                ft.Text("All fields are required!", color=ft.Colors.RED)
            )
            page.snack_bar.open = True
            page.update()
        else:
            phone_number = phone_number_field.value.strip()
            password = password_field.value.strip()

            success, result = login_user(phone_number, password)
            if success:
                page.snack_bar = ft.SnackBar(
                    ft.Text("Login successful!", color=ft.Colors.BLUE)
                )
                page.snack_bar.open = True
                page.update()

                phone_number_field.value = ""
                password_field.value = ""

                page.user_id = result.user_id
                page.user_logged_in = True

                SaveSignin(result.user_id)

                page.update()
                page.go('/home')
            else:
                page.snack_bar = ft.SnackBar(
                    ft.Text(result, color=ft.Colors.RED)
                )
                page.snack_bar.open = True
                page.update()

    phone_number_field = ft.TextField(label="Phone number", width=610, color=ft.Colors.with_opacity(1, "#1f1f1f"), bgcolor=ft.Colors.WHITE, border_radius=5, border=ft.InputBorder.OUTLINE)
    password_field = ft.TextField(label="Password", password=True, can_reveal_password=True, width=610, color=ft.Colors.with_opacity(1, "#1f1f1f"), bgcolor=ft.Colors.WHITE, border_radius=5, border=ft.InputBorder.OUTLINE)
    signin_button = ft.ElevatedButton(text="Signin", on_click=lambda e: signin_clicked(e), height=36, width=200, bgcolor=ft.Colors.with_opacity(1, "#009c74"), color=ft.Colors.WHITE, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)))
    signup = ft.TextButton(text="Create account", on_click=lambda _: page.go('/registration'))

    return ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [ft.Text("Account login", size=32, color=ft.Colors.with_opacity(1, "#1f1f1f"))],
                    alignment=ft.MainAxisAlignment.START,
                    width=610,
                ),
                phone_number_field,
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
    )
