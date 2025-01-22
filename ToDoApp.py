import tkinter as tk
from tkinter import messagebox
from tasks import *

class ToDoApp:
        def __init__(self, root, todolist):
            self.todolist = todolist

            self.root = root
            self.root.title("Checkpoints")

            self.name_entry = tk.Entry(self.root)  # Skapa textfält
            self.name_entry.pack()  # Lägg till i GUI

            self.description_entry = tk.Entry(self.root)  # Skapa textfält
            self.description_entry.pack()

            self.date_entry = tk.Entry(self.root)  # Skapa textfält
            self.date_entry.pack()

            # Skapa GUI-element
            self.task_listbox = tk.Listbox(self.root, width=100, height=15)
            self.task_listbox.pack(padx=10, pady=10)

            self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
            self.add_button.pack(pady=5)

            self.mark_done_button = tk.Button(self.root, text="Mark as Done", command=self.mark_task_done)
            self.mark_done_button.pack(pady=5)

            self.refresh_task_list()

        def add_task(self):
            name = self.name_entry.get()
            description = self.description_entry.get()
            deadline = self.date_entry.get()

            task = Task(name, description, deadline)
            self.todolist.add_task(task)

            self.refresh_task_list()

        def mark_task_done(self):
            selected_task_index = self.task_listbox.curselection()
            if selected_task_index:
                task_index = selected_task_index[0]
                self.todolist.mark_done(task_index)
                self.refresh_task_list()
            else:
                messagebox.showwarning("Selection Error", "No task selected.")

        def refresh_task_list(self):
            # Rensa listan och fyll på med uppgifter
            self.task_listbox.delete(0, tk.END)
            for task in self.todolist.tasks:
                self.task_listbox.insert(tk.END, f"Task: {task.name_of_task}, Description: {task.description}, Deadline: {task.deadline}")
