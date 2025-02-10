import flet as ft
from datetime import datetime

def Home(page: ft.Page):
    page.title = "STACK - Inventory and Finance Management"
    # page.window.width = 900
    # page.window.height = 700
    page.bgcolor = "#000E2F"

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
                    ft.Text("STACK", size=24, weight=ft.FontWeight.BOLD),
                    ft.Text("Where Smart Management Meets Simplicity", size=16),
                ],
                spacing=5,
                alignment=ft.MainAxisAlignment.START,
            ),
        ],
        spacing=0,
        alignment=ft.MainAxisAlignment.START,
    )

    # Tab content containers
    finances_container = ft.Column(
        expand=True,
        controls=[]
    )
    inventory_container = ft.Column(
        expand=True,
        controls=[]
    )

    # Finances tab content
    amount_input = ft.TextField(label="Amount:", expand=True, bgcolor="#001F67")
    description_input = ft.TextField(label="Description:", expand=True, bgcolor="#001F67")
    category_dropdown = ft.Dropdown(
        label="Category:",
        bgcolor="#001F67",
        options=[
            ft.dropdown.Option("Rent"),
            ft.dropdown.Option("Transport"),
            ft.dropdown.Option("Food"),
            ft.dropdown.Option("Leisure"),
            ft.dropdown.Option("Other"),
        ],
    )
    type_dropdown = ft.Dropdown(
        label="Type:",
        bgcolor="#001F67",
        options=[
            ft.dropdown.Option("Expenses"),
            ft.dropdown.Option("Income"),
            ft.dropdown.Option("Savings"),
        ],
    )
    transaction_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Date")),
            ft.DataColumn(ft.Text("Category")),
            ft.DataColumn(ft.Text("Amount")),
            ft.DataColumn(ft.Text("Type")),
            ft.DataColumn(ft.Text("Description")),
        ],
        rows=[],
        expand=True,
        bgcolor="#001F67",
        gradient=ft.LinearGradient(
                    begin=ft.alignment.top_center,
                    end=ft.alignment.bottom_center,
                    colors=["#001F67","#000E2F"]),
    )

    def add_transaction(e):
        if amount_input.value.isdigit() and category_dropdown.value and type_dropdown.value:
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            transaction_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(date)),
                        ft.DataCell(ft.Text(category_dropdown.value)),
                        ft.DataCell(ft.Text(amount_input.value)),
                        ft.DataCell(ft.Text(type_dropdown.value)),
                        ft.DataCell(ft.Text(description_input.value)),
                    ]
                )
            )
            amount_input.value = ""
            description_input.value = ""
            category_dropdown.value = None
            type_dropdown.value = None
            page.update()

    add_button = ft.ElevatedButton("Add", color="#FFFFFF", on_click=add_transaction, bgcolor="#001F67")

    finances_container.controls.extend([
        ft.Text("New Transaction", size=18, weight=ft.FontWeight.BOLD),
        ft.Row([amount_input, category_dropdown], spacing=10),
        ft.Row([type_dropdown, description_input], spacing=10),
        add_button,
        ft.Divider(height=1, color="#D3D3D3"),
        ft.Text("Transactions", size=18, weight=ft.FontWeight.BOLD),
        transaction_table,
    
    ])

    # Inventory tab content
    inventory_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Item")),
            ft.DataColumn(ft.Text("Quantity")),
            ft.DataColumn(ft.Text("Category")),
            ft.DataColumn(ft.Text("Price")),
        ],
        rows=[],
        expand=True,
        bgcolor="#001F67"
    )

    item_input = ft.TextField(label="Item Name", expand=True, bgcolor="#001F67")
    quantity_input = ft.TextField(label="Quantity", expand=True, bgcolor="#001F67")
    inventory_category_dropdown = ft.Dropdown(
        label="Category",
        bgcolor="#001F67",
        options=[
            ft.dropdown.Option("Electronics"),
            ft.dropdown.Option("Groceries"),
            ft.dropdown.Option("Clothing"),
            ft.dropdown.Option("Furniture"),
            ft.dropdown.Option("Other"),
        ],
    )
    price_input = ft.TextField(label="Price", expand=True, bgcolor="#001F67")

    def add_inventory_item(e):
        if quantity_input.value.isdigit() and price_input.value.isdigit() and inventory_category_dropdown.value:
            inventory_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(item_input.value)),
                        ft.DataCell(ft.Text(quantity_input.value)),
                        ft.DataCell(ft.Text(inventory_category_dropdown.value)),
                        ft.DataCell(ft.Text(price_input.value)),
                    ]
                )
            )
            item_input.value = ""
            quantity_input.value = ""
            inventory_category_dropdown.value = None
            price_input.value = ""
            page.update()

    add_inventory_button = ft.ElevatedButton("Add Item", color="#FFFFFF", on_click=add_inventory_item, bgcolor="#001F67")

    inventory_container.controls.extend([
        ft.Text("Add Inventory Item", size=18, weight=ft.FontWeight.BOLD),
        ft.Row([item_input, quantity_input], spacing=10),
        ft.Row([inventory_category_dropdown, price_input], spacing=10),
        add_inventory_button,
        ft.Divider(height=1, color="#D3D3D3"),
        ft.Text("Inventory List", size=18, weight=ft.FontWeight.BOLD),
        inventory_table,
        
    ])

    # Tabs
    def tab_change(e):
        if tabs.selected_index == 0:
            tab_content.controls = finances_container.controls
        elif tabs.selected_index == 1:
            tab_content.controls = inventory_container.controls
        page.update()

    tabs = ft.Tabs(
        selected_index=0,
        tabs=[
            ft.Tab(text="Finances"),
            ft.Tab(text="Inventory"),
        ],
        on_change=tab_change,
        expand=False,
    )

    tab_content = ft.Column(finances_container.controls, expand=True)

    
    return ft.Container (
        content = ft.Column(
            [
                header,
                ft.Divider(height=1, color="#D3D3D3"),
                tabs,
                tab_content,
            ],
            expand=True,
            scroll='auto',
        ),
        padding=ft.padding.symmetric(horizontal=8)
    )
