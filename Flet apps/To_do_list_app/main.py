import flet as ft
import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f)

def main(page: ft.Page):
    page.title = "To-Do App"
    tasks = load_tasks()

    task_list = ft.Column()

    def refresh_task_list():
        task_list.controls.clear()
        for i, task in enumerate(tasks):
            task_checkbox = ft.Checkbox(
                label=task["name"],
                value=task["done"],
                on_change=lambda e, index=i: toggle_task(index, e.control.value),
            )
            delete_button = ft.IconButton(
                icon=ft.icons.DELETE,
                on_click=lambda e, index=i: delete_task(index),
            )
            task_row = ft.Row([task_checkbox, delete_button])
            task_list.controls.append(task_row)
        page.update()

    def toggle_task(index, done):
        tasks[index]["done"] = done
        save_tasks(tasks)
        refresh_task_list()

    def delete_task(index):
        tasks.pop(index)
        save_tasks(tasks)
        refresh_task_list()

    def add_task(e):
        if new_task.value:
            tasks.append({"name": new_task.value, "done": False})
            save_tasks(tasks)
            new_task.value = ""
            refresh_task_list()

    new_task = ft.TextField(hint_text="Enter a task", width=300)
    add_button = ft.ElevatedButton("Add", on_click=add_task)

    page.add(
        ft.Row([new_task, add_button]),
        task_list,
    )

    refresh_task_list()

ft.app(target=main)
