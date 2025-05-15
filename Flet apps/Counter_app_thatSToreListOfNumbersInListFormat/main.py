import flet as ft
import os

HISTORY_FILE = "counter.txt"

# Get last value from file
def load_last_counter():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            lines = f.readlines()
            for line in reversed(lines):
                line = line.strip()
                if line.isdigit() or (line.startswith("-") and line[1:].isdigit()):
                    return line
    return "0"

# Append values to file
def append_to_history(value):
    with open(HISTORY_FILE, "a") as f:
        f.write(f"{value}\n")

def log_reset():
    with open(HISTORY_FILE, "a") as f:
        f.write("Reset to 0\n")

def read_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return f.read()
    return "No history yet."

def main(page: ft.Page):
    # Style the page
    page.title = "Styled Counter with History"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLUE_GREY_50
    page.padding = 40
    page.scroll = "auto"

    # Styled counter display
    counter = ft.Text(
        value=load_last_counter(),
        size=60,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
        color=ft.colors.BLUE_900
    )

    # Styled history box (initially hidden)
    history_display = ft.Text(
        value="",
        size=16,
        visible=False,
        color=ft.colors.BLACK87,
        text_align=ft.TextAlign.LEFT
    )

    # Event handlers
    def add(e):
        counter.value = str(int(counter.value) + 1)
        append_to_history(counter.value)
        page.update()

    def subtract(e):
        counter.value = str(int(counter.value) - 1)
        append_to_history(counter.value)
        page.update()

    def reset(e):
        counter.value = "0"
        log_reset()
        append_to_history(counter.value)
        page.update()

    def show_history(e):
        history_display.value = read_history()
        history_display.visible = True
        page.update()

    # Styled buttons
    plus_button = ft.ElevatedButton(text="+", on_click=add, bgcolor=ft.colors.GREEN_400)
    minus_button = ft.ElevatedButton(text="-", on_click=subtract, bgcolor=ft.colors.RED_400)
    reset_button = ft.ElevatedButton(text="Reset", on_click=reset, bgcolor=ft.colors.GREY_500)
    show_button = ft.OutlinedButton(text="Show History", on_click=show_history)

    # Layout using Column
    page.add(
        counter,
        ft.Row(
            [minus_button, plus_button, reset_button],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        ),
        ft.Container(height=20),  # Spacer
        show_button,
        ft.Container(height=20),  # Spacer
        ft.Container(content=history_display, padding=10, bgcolor=ft.colors.WHITE, border_radius=10)
    )

ft.app(target=main)
