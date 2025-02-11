import flet as ft
import re
from flet import *
from db.crud import add_user, get_user, session
from db.dtos import UserRegistrationDto
from helpers.datahelpers import *
from hashlib import sha256
import sys
from pydantic import BaseModel
sys.path.append('./db')
from db.models import User, Message, Status, Group

def register_user(username: str, phone_number: str, password: str):
    try:
        # Check for duplicate username
        existing_user = session.query(User).filter(User.user_name == username).first()
        if (existing_user):
            return False, "Username already exists."

        # Check for duplicate phone number
        existing_phone = session.query(User).filter(User.phone_number == phone_number).first()
        if (existing_phone):
            return False, "Phone number already exists."

        hashed_password = sha256(password.encode()).hexdigest()
        user_dto = UserRegistrationDto(
            user_id=0,  # This will be auto-incremented by the database
            first_name="",
            last_name="",
            user_name=username,
            phone_number=phone_number,
            password=hashed_password  # Include hashed password
        )
        user = add_user(user_dto)
        return True, user.user_id
    except Exception as e:
        return False, str(e)

def UserSignup(page: ft.Page):
    # Define regex patterns
    phone_pattern = r'^\+?[1-9]\d{8,14}$'

    def signup_clicked(e):
        # Validate input fields
        if not username_field.value or not phone_number_field.value or not password_field.value or not confirm_password_field.value:
            page.snack_bar = ft.SnackBar(
                ft.Text("All fields are required!", color=ft.Colors.RED)
            )
            page.snack_bar.open = True
            page.update()
        elif not re.match(phone_pattern, phone_number_field.value):
            page.snack_bar = ft.SnackBar(
                ft.Text("Invalid phone number! Only digits and at least 9 digits.", color=ft.Colors.RED)
            )
            page.snack_bar.open = True
            page.update()
        elif password_field.value != confirm_password_field.value:
            page.snack_bar = ft.SnackBar(
                ft.Text("Passwords do not match!", color=ft.Colors.RED)
            )
            page.snack_bar.open = True
            page.update()
        else:
            username = username_field.value.strip()
            phone_number = phone_number_field.value.strip()
            password = password_field.value.strip()

            success, result = register_user(username, phone_number, password)
            if success:
                page.snack_bar = ft.SnackBar(
                    ft.Text("Account created!", color=ft.Colors.BLUE)
                )
                page.snack_bar.open = True
                page.update()

                username_field.value = ""
                phone_number_field.value = ""
                password_field.value = ""
                confirm_password_field.value = ""

                page.user_id = result
                page.user_logged_in = True

                SaveSignin(result)

                page.update()
                page.go('/home')
            else:
                page.snack_bar = ft.SnackBar(
                    ft.Text(result, color=ft.Colors.RED)
                )
                page.snack_bar.open = True
                page.update()

    username_field = ft.TextField(label="Username", width=300, color=ft.Colors.with_opacity(1, "#1f1f1f"), bgcolor=ft.Colors.WHITE, border_radius=5, border=ft.InputBorder.OUTLINE)
    phone_number_field = ft.TextField(label="Phone number", width=300, color=ft.Colors.with_opacity(1, "#1f1f1f"), bgcolor=ft.Colors.WHITE, border_radius=5, border=ft.InputBorder.OUTLINE)
    password_field = ft.TextField(label="Password", password=True, can_reveal_password=True, width=300, color=ft.Colors.with_opacity(1, "#1f1f1f"), bgcolor=ft.Colors.WHITE, border_radius=5, border=ft.InputBorder.OUTLINE)
    confirm_password_field = ft.TextField(label="Confirm password", password=True, can_reveal_password=True, width=300, color=ft.Colors.with_opacity(1, "#1f1f1f"), bgcolor=ft.Colors.WHITE, border_radius=5, border=ft.InputBorder.OUTLINE)
    signup_button = ft.ElevatedButton(text="Signup", on_click=lambda e: signup_clicked(e), height=36, width=200, bgcolor=ft.Colors.with_opacity(1, "#009c74"), color=ft.Colors.WHITE, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)))
    login = ft.TextButton(text="Login", on_click=lambda _: page.go('/login'))

    return ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [ft.Text("Create account", size=32, color=ft.Colors.with_opacity(1, "#1f1f1f"))],
                    alignment=ft.MainAxisAlignment.START,
                    width=610,
                ),
                ft.Row(
                    [
                        username_field,
                        phone_number_field,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        password_field,
                        confirm_password_field,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    width=610,
                ),
                ft.Row(
                    [signup_button],
                    alignment=ft.MainAxisAlignment.END,
                    width=610,
                ),
                ft.Row(
                    [
                        ft.Container(height=100),  # Add some space
                        ft.Text("Already have an account?", color=ft.Colors.with_opacity(1, "#1f1f1f")),
                        login,
                    ],
                    width=610,
                    alignment=ft.MainAxisAlignment.START
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