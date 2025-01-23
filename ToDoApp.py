
import tkinter as tk
from tkinter import messagebox
from tasks import *

class ToDoApp:
        def __init__(self, root, todolist):
            self.todolist = todolist

            self.root = root
            self.root.title("What to do today?")
            self.root.configure(bg="#212738")

            # Skapa etiketter och textfält med grid
            self.q_label = tk.Button(self.root, text="Instructions?", command=self.show_instructions, bg="#F2AF29")
            self.q_label.grid(row=7, column=5, padx=15, pady=5, sticky="e")

            self.pending_info = tk.Label(self.root, text="Pending tasks", bg="lightgrey")
            self.pending_info.grid(row=4, column=0, padx=15, pady=5, sticky="w")

            self.completed_info = tk.Label(self.root, text="Completed tasks", bg="lightgrey")
            self.completed_info.grid(row=4, column=3, padx=15, pady=5, sticky="w")

            self.name_label = tk.Label(self.root, text="Task: ", bg="#F2AF29")
            self.name_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

            self.name_entry = tk.Entry(self.root)
            self.name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="e")

            self.description_label = tk.Label(self.root, text="Desc: ", bg="#F2AF29")
            self.description_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

            self.description_entry = tk.Entry(self.root)
            self.description_entry.grid(row=1, column=1, padx=5, pady=5, sticky="e")

            self.date_label = tk.Label(self.root, text="Deadline: ", bg="#F2AF29")
            self.date_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")

            self.date_entry = tk.Entry(self.root)
            self.date_entry.grid(row=2, column=1, padx=5, pady=5, sticky="e")

            # Lista och knappar
            self.task_listbox = tk.Listbox(self.root, width=70, height=10, bg="lightgrey")
            self.task_listbox.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

            self.task_listbox2 = tk.Listbox(self.root, width=70, height=10, bg="lightgrey")
            self.task_listbox2.grid(row=6, column=3, columnspan=3, padx=10, pady=10)

            self.add_button = tk.Button(self.root, text="Add task", command=self.add_task, bg="#F2AF29")
            self.add_button.grid(row=7, column=0, padx=20, pady=5)

            self.remove_button = tk.Button(self.root, text="Del task", command=self.remove_task, bg="#F2AF29")
            self.remove_button.grid(row=7, column=1, padx=20, pady=5)  # Placera knappen var du vill

            self.mark_done_button = tk.Button(self.root, text="Mark done", command=self.move_to_completed, bg="#F2AF29")
            self.mark_done_button.grid(row=7, column=2, padx=20, pady=5)

            self.refresh_task_list()

            # NYTT: Lägg till trace på textrutorna
            self.name_entry_var = tk.StringVar()
            self.description_entry_var = tk.StringVar()
            self.date_entry_var = tk.StringVar()

            self.name_entry.config(textvariable=self.name_entry_var)
            self.description_entry.config(textvariable=self.description_entry_var)
            self.date_entry.config(textvariable=self.date_entry_var)

            self.name_entry_var.trace("w", lambda *args: self.check_entries())
            self.description_entry_var.trace("w", lambda *args: self.check_entries())
            self.date_entry_var.trace("w", lambda *args: self.check_entries())

        # NYTT: Metod för att kontrollera textrutorna
        def check_entries(self):
            if self.name_entry_var.get() and self.description_entry_var.get() and self.date_entry_var.get():
                self.add_button.config(state="normal")
            else:
                self.add_button.config(state="disabled")

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

        def remove_task(self):
            # Hämta valt index
            selected_index = self.task_listbox.curselection()
            if selected_index:  # Kontrollera om något är valt
                index = selected_index[0]

                # Ta bort från listan i Listbox
                self.task_listbox.delete(index)

                # Ta bort från listan i data (om du har en separat lista för tasks)
                if index < len(self.tasks):  # Om du lagrar tasks i en separat lista
                    del self.tasks[index]
            else:
                messagebox.showwarning("Selection Error", "No task selected.")

        def refresh_task_list(self):
            # Rensa listan och fyll på med uppgifter
            self.task_listbox.delete(0, tk.END)
            for task in self.todolist.tasks:
                self.task_listbox.insert(tk.END, f"Task: {task.name_of_task}, Description: {task.description}, Deadline: {task.deadline}, Is Completed: {task.status}")

        def move_to_completed(self):
            selected_task_index = self.task_listbox.curselection()
            if selected_task_index:
                # Hämta det valda task-indexet
                task_index = selected_task_index[0]

                # Hämta uppgiften från todolist
                completed_task = self.todolist.tasks[task_index]

                # Uppdatera status för uppgiften (om det används)
                completed_task.status = "Completed"

                # Ta bort uppgiften från den första listan
                self.task_listbox.delete(task_index)
                self.todolist.tasks.pop(task_index)

                # Lägg till uppgiften i den andra listboxen (completed)
                self.task_listbox2.insert(tk.END,f"Task: {completed_task.name_of_task}, Description: {completed_task.description}, Deadline: {completed_task.deadline}")
            else:
                # Om inget är valt, visa ett varningsmeddelande
                messagebox.showwarning("Selection Error", "No task selected.")


        def show_instructions(self):
            messagebox.showwarning("Instructions", "1. Enter task name\n2. Enter task description\n3. Enter task deadline\n4. Click add task")
