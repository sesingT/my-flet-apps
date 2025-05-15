import flet as ft

def main(page: ft.Page):
    page.title = "Plus and Minus Counter"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Counter text display
    counter = ft.Text(value="0", size=40)

    # ➕ Increment button function
    def add(e):
        counter.value = str(int(counter.value) + 1)
        page.update()

    # ➖ Decrement button function
    def subtract(e):
        counter.value = str(int(counter.value) - 1)
        page.update()

    # 🔁 Reset button function
    def reset(e):
        counter.value = "0"
        page.update()

    # Create buttons
    plus_button = ft.ElevatedButton(text="+", on_click=add)
    minus_button = ft.ElevatedButton(text="-", on_click=subtract)
    reset_button = ft.ElevatedButton(text="Reset", on_click=reset)

    # Add everything to the page
    page.add(
        counter,
        ft.Row(
            [minus_button, plus_button, reset_button],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(target=main)
