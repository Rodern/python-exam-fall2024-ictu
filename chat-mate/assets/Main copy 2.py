import flet 
from flet import*
from Dash_F import*

def main(page: ft.Page):

    page.theme_mode = "dark"
    page.title = "STACK"
    page.padding=0
    page.windows_resizable= False

    page.on_route_change = router.route_change
    router.page = page
    page.add(
    )

ft.app(target=main, assets_dir="assets")