import flet as ft
from flet import *
from database import *
from signin import *
from signup import *
from home import *
from about import *
from dashboard import *
from stats import *

class Router:
    def __init__(self, page):
        self.page = page

        self.page.user_id = ""
        self.page.user_logged_in = False

        self.ft = ft
        self.routes = {
            '/': self.main(page),
            '/login': UserLogin(page),
            '/registration': UserSignup(page),
            '/home': Home(page),
            '/dashboard': Dashboard(page),
            '/statistics': Stats(page),
            '/about': About(page),
        }
        self.body = ft.Container(
            content=self.routes['/'],
            expand=True,
            margin=ft.margin.all(0),
            padding=ft.padding.all(0),
        )
    
    def on_route_changed(self, route):
        try:
            if self.page.user_logged_in:
                self.page.controls[0].controls[0].controls[0].content.controls[1].visible = True
                self.page._controls[0]._Stack__controls[0]._Column__controls[1]._Row__controls[0]._Container__content._Column__controls[2].visible = True
                self.page._controls[0]._Stack__controls[0]._Column__controls[1]._Row__controls[0]._Container__content._Column__controls[3].visible = True
                self.page.update()
            else:
                self.page.controls[0].controls[0].controls[0].content.controls[1].visible = False
                self.page._controls[0]._Stack__controls[0]._Column__controls[1]._Row__controls[0]._Container__content._Column__controls[2].visible = False
                self.page._controls[0]._Stack__controls[0]._Column__controls[1]._Row__controls[0]._Container__content._Column__controls[3].visible = False
                self.page.update()

            self.body.content = self.routes[route.route]
            self.body.update()
        except KeyError:
            self.body.content = ft.Text("404 - Page not found", color=ft.Colors.RED)
            self.body.update()
        except Exception as e:
            self.body.content = ft.Text(f"An error occurred: {str(e)}", color=ft.Colors.RED)
            self.body.update()

    # Main content area
    def main(self, page):
        # Create welcome message
        welcome_message = ft.Text(
            value="Welcome to Stack",
            size=24,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.with_opacity(1, "#1f1f1f"),
            text_align=ft.TextAlign.CENTER
        )

        # Create 'Create account' button
        create_account_button = ft.ElevatedButton(
            text="Create account",
            on_click=lambda _: page.go('/registration'),
            height=36,
            width=200,
            bgcolor=ft.Colors.with_opacity(1, "#0d7fd7"),
            color=ft.Colors.WHITE,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))
        )

        # Create 'Login' button
        login_button = ft.ElevatedButton(
            text="Login",
            on_click=lambda _: page.go('/login'),
            height=36,
            width=200,
            bgcolor=ft.Colors.with_opacity(0.2, "#0d7fd7"),
            color=ft.Colors.WHITE,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))
        )

        # Create prompts for buttons
        create_account_prompt = ft.Text(
            value="Sign into the application to start managing home and finances.",
            size=14,
            color=ft.Colors.with_opacity(1, "#1f1f1f"),
            text_align=ft.TextAlign.START,
            overflow=ft.TextOverflow.ELLIPSIS,
            max_lines=2,
        )

        login_prompt = ft.Text(
            value="Sign into your account to continue achieving more in home management.",
            size=14,
            color=ft.Colors.with_opacity(1, "#1f1f1f"),
            text_align=ft.TextAlign.START,
            overflow=ft.TextOverflow.ELLIPSIS,
            max_lines=2,
        )

        # Create a column to hold all elements
        column = ft.Column(
            controls=[
                ft.Image(
                    src=r"assets/favicon.png",  # Replace with your app logo URL
                    width=150,
                    height=150,
                ),
                welcome_message,
                ft.Container(height=50),  # Add some space
                ft.Row(
                    controls = [
                        ft.Container(height=20),  # Add some space
                        ft.Column(
                            controls = [
                                create_account_prompt,
                                create_account_button
                            ],
                            width=300,
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                        ft.Container(height=20),  # Add some space
                        ft.Column(
                            controls = [
                                login_prompt,
                                login_button
                            ],
                            width=300,
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                        ft.Container(height=20),  # Add some space
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        content = ft.Container(
            content=column,
            bgcolor=ft.Colors.WHITE,
            expand=True,
            margin=ft.margin.all(0)
        )
        return content




# Custom Title Bar
def create_title_bar(page: Page, side_nav, toggle_side_nav):
    global user_logged_in
    return ft.Container(
        content=ft.Row(
            [
                ft.Row(
                    [
                        ft.IconButton(icon=ft.Icons.MENU, icon_color="white", on_click=toggle_side_nav),
                        ft.Text("Stack", size=20, color="white", weight="bold"),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    height=50,
                ),
                ft.Row(
                    [
                        ft.OutlinedButton(
                            "Logout",
                            icon=ft.Icons.PERSON,
                            icon_color="white",
                            on_click=lambda _: logout(page),
                        ),
                        ft.Container(width=5),
                    ],
                    alignment=ft.MainAxisAlignment.END,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    height=50,
                    expand=True,
                    spacing=10,
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            height=50,
        ),
        bgcolor=ft.Colors.with_opacity(1, "#0d7fd7"),
        expand=False,
        margin=ft.margin.all(0),
        padding=ft.padding.all(0),
    )


def logout(page: Page):
    page.user_id = ""
    page.user_logged_in = False
    SaveSignin("")
    page.update
    page.go('/')

def go_home(page: Page):
    if page.user_logged_in:
        page.go('/home')
    else:
        page.go('/')

# Side Navigation
def create_side_nav(page: Page):
    return ft.Container(
        content=ft.Column(
            [
                ft.Text(" Menu", size=24, weight="bold", color=ft.Colors.BLUE_800),
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.HOME, color=ft.Colors.with_opacity(1, "#0d7fd7")),
                    title=ft.Text("Home", color=ft.Colors.with_opacity(1, "#0d7fd7")),
                    on_click=lambda _: go_home(page),
                    bgcolor=ft.Colors.with_opacity(1, "#f2f2f2"),
                ),
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.DASHBOARD, color=ft.Colors.with_opacity(1, "#0d7fd7")),
                    title=ft.Text("Dashboard", color=ft.Colors.with_opacity(1, "#0d7fd7")),
                    on_click=lambda _: page.go('/dashboard'),
                    bgcolor=ft.Colors.with_opacity(1, "#f2f2f2"),
                ),
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.ANALYTICS, color=ft.Colors.with_opacity(1, "#0d7fd7")),
                    title=ft.Text("Statistics", color=ft.Colors.with_opacity(1, "#0d7fd7")),
                    on_click=lambda _: page.go('/statistics'),
                    bgcolor=ft.Colors.with_opacity(1, "#f2f2f2"),
                ),
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.INFO, color=ft.Colors.with_opacity(1, "#0d7fd7")),
                    title=ft.Text("About", color=ft.Colors.with_opacity(1, "#0d7fd7")),
                    on_click=lambda _: page.go('/about'),
                    bgcolor=ft.Colors.with_opacity(1, "#f2f2f2"),
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=10,
            expand=True,
        ),
        bgcolor=ft.Colors.with_opacity(1, "#f2f2f2"),
        width=250,
        expand=False,
        margin=ft.margin.all(0),
        padding=ft.padding.all(0),
        offset=ft.transform.Offset(0, 0)  # Initially hidden
    )

def main(page: ft.Page):
    page.title = "STACK"
    page.window.resizable = True
    page.window.min_width = 1007
    page.window.min_height = 641
    page.window.width = 1007
    page.window.height = 641
    page.user_id = ""
    page.user_logged_in = False
    page.padding=ft.padding.all(0)

    # Create side navigation
    side_nav = create_side_nav(page)

    # Initialize the router
    myRouter = Router(page)

    # Function to toggle side navigation
    def toggle_side_nav(e):
        if side_nav.offset.x == 0:
            side_nav.offset.x = -1
            side_nav.visible = False
        else:
            side_nav.offset.x = 0
            side_nav.visible = True
        page.update()

    # Custom Title Bar
    title_bar = create_title_bar(page, side_nav, toggle_side_nav)
    title_bar.content.controls[1].visible = False

    # Set the initial route
    page.on_route_change = myRouter.on_route_changed

    # Add controls to the page
    page.add(
        ft.Stack(
            [
                ft.Column(
                    [
                        title_bar,
                        ft.Row(
                            [
                                side_nav,
                                myRouter.body
                            ],
                            expand=True,
                            vertical_alignment=ft.CrossAxisAlignment.START
                        ),
                    ],
                    expand=True,
                ),
            ],
            expand=True,
        )
    )

    if GetLogin(page):
        page.controls[0].controls[0].controls[0].content.controls[1].visible = True
        page.go('/home')
    else:
        page.controls[0].controls[0].controls[0].content.controls[1].visible = False
        page.go('/')

# Initialize the database
# initialize_database()

# Run the Flet app
ft.app(target=main, assets_dir="assets")