import flet as ft
import os

# This is the file that will store the counter value
COUNTER_FILE = "counter.txt"

# Function to read the value from the file
def load_counter():
    if os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, "r") as f:
            return f.read().strip()
    else:
        return "0"

# Function to write the value to the file
def save_counter(value):
    with open(COUNTER_FILE, "w") as f:
        f.write(str(value))

def main(page: ft.Page):
    page.title = "Persistent Counter"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Load saved counter value
    counter = ft.Text(value=load_counter(), size=40)

    def add(e):
        counter.value = str(int(counter.value) + 1)
        save_counter(counter.value)
        page.update()

    def subtract(e):
        counter.value = str(int(counter.value) - 1)
        save_counter(counter.value)
        page.update()

    def reset(e):
        counter.value = "0"
        save_counter(counter.value)
        page.update()

    plus_button = ft.ElevatedButton(text="+", on_click=add)
    minus_button = ft.ElevatedButton(text="-", on_click=subtract)
    reset_button = ft.ElevatedButton(text="Reset", on_click=reset)

    page.add(
        counter,
        ft.Row(
            [minus_button, plus_button, reset_button],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(target=main)
