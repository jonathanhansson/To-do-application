import tkinter as tk
from tkinter import messagebox
from tasks import *

class ToDoApp:
        def __init__(self, root, todolist):
            self.todolist = todolist

            self.root = root
            self.root.title("Checkpoints")

            # Skapa etiketter och textfält med grid
            self.name_label = tk.Label(self.root, text="Enter task: ")
            self.name_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

            self.name_entry = tk.Entry(self.root)
            self.name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

            self.description_label = tk.Label(self.root, text="Enter description: ")
            self.description_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

            self.description_entry = tk.Entry(self.root)
            self.description_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

            self.date_label = tk.Label(self.root, text="Enter deadline: ")
            self.date_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")

            self.date_entry = tk.Entry(self.root)
            self.date_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

            # Lista och knappar
            self.task_listbox = tk.Listbox(self.root, width=100, height=15)
            self.task_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

            self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
            self.add_button.grid(row=4, column=0, padx=10, pady=5)

            self.mark_done_button = tk.Button(self.root, text="Mark as Done", command=self.mark_task_done)
            self.mark_done_button.grid(row=4, column=1, padx=10, pady=5)

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
