import flet as ft
import re
from flet import *
from db.inventoryplusdb import *
from helpers.datahelpers import *
from hashlib import sha256


def register_user(first_name: str, last_name: str, username: str, phone_number: str, email: str, password: str):
    try:
        data_store = create_inventory_db()
        hashed_password = sha256(password.encode()).hexdigest()
        userId = data_store.create_user(generateGuid(), username, hashed_password, email, first_name, last_name, phone_number, 'User', "2023-01-01", "2023-01-01")
        return True, userId
    except Exception as e:
        return False, e

def UserSignup(page: ft.Page):
    # Define regex patterns
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    phone_pattern = r'^\+?[1-9]\d{8,14}$'

    global user_logged_in

    def signup_clicked(e):
        global user_logged_in
        # Validate input fields
        if not first_name_field.value or not last_name_field.value or not phone_number_field.value or not username_field.value or not email_field.value or not password_field.value or not confirm_password_field.value:
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
        elif not re.match(email_pattern, email_field.value):
            page.snack_bar = ft.SnackBar(
                ft.Text("Invalid email address!", color=ft.Colors.RED)
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
            first_name = first_name_field.value.strip()
            last_name = last_name_field.value.strip()
            username = username_field.value.strip()
            phone_number = phone_number_field.value.strip()
            password = password_field.value.strip()
            email = email_field.value.strip()

            success, result = register_user(first_name, last_name, username, phone_number, email, password)
            if success:
                page.snack_bar = ft.SnackBar(
                    ft.Text("Account created!", color=ft.Colors.BLUE)
                )
                page.snack_bar.open = True
                page.update()

                
                first_name_field.value = ""
                last_name_field.value = ""
                username_field.value = ""
                phone_number_field.value = ""
                password_field.value = ""
                email_field.value = ""

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


    first_name_field = ft.TextField(label="Firstname", width=300, color=ft.Colors.with_opacity(1, "#1f1f1f"), bgcolor=ft.Colors.WHITE, border_radius=5, border=ft.InputBorder.OUTLINE)
    last_name_field = ft.TextField(label="Lastname", width=300, color=ft.Colors.with_opacity(1, "#1f1f1f"), bgcolor=ft.Colors.WHITE, border_radius=5, border=ft.InputBorder.OUTLINE)
    username_field = ft.TextField(label="Username", width=300, color=ft.Colors.with_opacity(1, "#1f1f1f"), bgcolor=ft.Colors.WHITE, border_radius=5, border=ft.InputBorder.OUTLINE)
    phone_number_field = ft.TextField(label="Phone number", width=300, color=ft.Colors.with_opacity(1, "#1f1f1f"), bgcolor=ft.Colors.WHITE, border_radius=5, border=ft.InputBorder.OUTLINE)
    password_field = ft.TextField(label="Password", password=True, can_reveal_password=True, width=300, color=ft.Colors.with_opacity(1, "#1f1f1f"), bgcolor=ft.Colors.WHITE, border_radius=5, border=ft.InputBorder.OUTLINE)
    confirm_password_field = ft.TextField(label="Confirm password", password=True, can_reveal_password=True, width=300, color=ft.Colors.with_opacity(1, "#1f1f1f"), bgcolor=ft.Colors.WHITE, border_radius=5, border=ft.InputBorder.OUTLINE)
    email_field = ft.TextField(label="Email", width=610, color=ft.Colors.with_opacity(1, "#1f1f1f"), bgcolor=ft.Colors.WHITE, border_radius=5, border=ft.InputBorder.OUTLINE)
    signup_button = ft.ElevatedButton(text="Signup", on_click=lambda e: signup_clicked(e), height=36, width=200, bgcolor=ft.Colors.with_opacity(1, "#0078D4"), color=ft.Colors.WHITE, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)))
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
                        first_name_field,
                        last_name_field,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
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
                email_field,
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
        border_radius=10,
    )