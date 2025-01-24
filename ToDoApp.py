
import tkinter as tk
from tkinter import Toplevel, messagebox
from tasks import *
from todolist import *

class ToDoApp:
        def __init__(self, root, todolist):
            self.todolist = todolist

            self.root = root
            self.root.title("What to do today?")
            self.root.configure(bg="#212738")

            self.add_task_button = tk.Button(self.root, text="+", font=("Arial", 16), command=self.open_new_task_window, bg="#F2AF29")
            self.add_task_button.grid(row=0, column=0, padx=15, pady=10, sticky="nw")

            # Skapa etiketter och textfält med grid
            empty_row = tk.Label(root, bg="#212738")  # Bakgrundsfärgen matchar fönstret
            empty_row.grid(row=6, column=0, columnspan=10, pady=10, sticky="nsew")

            self.info_button = tk.Button(self.root, text="Instructions?", command=self.show_instructions, bg="#F2AF29")
            self.info_button.grid(row=4, column=5, padx=15, pady=5, sticky="e")

            self.pending_info = tk.Label(self.root, text="Tasks in progress", bg="lightgrey")
            self.pending_info.grid(row=1, column=0, padx=15, pady=5, sticky="w")

            self.completed_info = tk.Label(self.root, text="Completed tasks", bg="lightgrey")
            self.completed_info.grid(row=1, column=3, padx=15, pady=5, sticky="w")

            # Lista och knappar
            self.task_listbox = tk.Listbox(self.root, width=70, height=10, bg="white")
            self.task_listbox.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

            self.task_listbox2 = tk.Listbox(self.root, width=70, height=10, bg="white")
            self.task_listbox2.grid(row=2, column=3, columnspan=3, padx=10, pady=10)


            self.remove_button = tk.Button(self.root, text="Del task", command=self.remove_task, bg="#F2AF29")
            self.remove_button.grid(row=4, column=0, padx=15, pady=5, sticky="w")

            self.mark_done_button = tk.Button(self.root, text="Mark done", command=self.move_to_completed, bg="#F2AF29")
            self.mark_done_button.grid(row=4, column=0, padx=2, pady=5)

            self.refresh_task_list()

            # NYTT: Lägg till trace på textrutorna
            self.name_entry_var = tk.StringVar()
            self.description_entry_var = tk.StringVar()
            self.date_entry_var = tk.StringVar()


            self.name_entry_var.trace("w", lambda *args: self.check_entries())
            self.description_entry_var.trace("w", lambda *args: self.check_entries())
            self.date_entry_var.trace("w", lambda *args: self.check_entries())

        def open_new_task_window(self):
            # Skapa ett nytt fönster
            new_task_window = Toplevel(self.root)
            new_task_window.title("Add New Task")
            new_task_window.configure(bg="#212738")

            # Etiketter och fält
            tk.Label(new_task_window, text="Task:", bg="#F2AF29").grid(row=0, column=0, padx=5, pady=5, sticky="e")
            task_entry = tk.Entry(new_task_window, width=30)
            task_entry.grid(row=0, column=1, padx=5, pady=5)

            tk.Label(new_task_window, text="Desc:", bg="#F2AF29").grid(row=1, column=0, padx=5, pady=5, sticky="e")
            desc_entry = tk.Entry(new_task_window, width=30)
            desc_entry.grid(row=1, column=1, padx=5, pady=5)

            tk.Label(new_task_window, text="Deadline:", bg="#F2AF29").grid(row=2, column=0, padx=5, pady=5, sticky="e")
            deadline_entry = tk.Entry(new_task_window, width=30)
            deadline_entry.grid(row=2, column=1, padx=5, pady=5)



            new_task_window.bind('<Return>', lambda event: self.add_task(task_entry, desc_entry, deadline_entry, new_task_window))

            # Förändring: Använd lambda för att skicka textrutor till add_task-metoden
            add_button = tk.Button(new_task_window, text="Add task", command=lambda: self.add_task(task_entry, desc_entry, deadline_entry), bg="#F2AF29")
            add_button.grid(row=3, column=0, padx=5, pady=5, sticky="e")

        # NYTT: Metod för att kontrollera textrutorna
        def check_entries(self):
            if self.name_entry_var.get() and self.description_entry_var.get() and self.date_entry_var.get():
                self.add_button.config(state="normal")
            else:
                self.add_button.config(state="disabled")

        def add_task(self, task_entry, desc_entry, deadline_entry, new_task_window):
            name = task_entry.get()
            description = desc_entry.get()
            deadline = deadline_entry.get()

            task = Task(name, description, deadline)
            self.todolist.add_task(task)
            self.refresh_task_list()

            new_task_window.destroy()

        def mark_task_done(self):
            selected_task_index = self.task_listbox.curselection()
            if selected_task_index:
                task_index = selected_task_index[0]
                self.todolist.mark_done(task_index)
                self.refresh_task_list()
            else:
                messagebox.showwarning("Selection Error", "No task selected.")

        def remove_task(self):
            selected_index = self.task_listbox.curselection()
            if selected_index:
                index = selected_index[0]
                self.task_listbox.delete(index)
                del self.todolist.tasks[index]  # Ta bort från self.todolist.tasks
                self.refresh_task_list()
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
            messagebox.showwarning("Instructions", "1. Click the +\n2. Enter task name\n3. Enter task description\n4. Enter task deadline\n5. Click add task\n\ni. Click on task and then Del task to delete\ni. Click on task and then Mark done to make it completed")

        def display_task_entry(self):
            self.name_entry = tk.Entry(self.root, width=40)
            self.name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        def display_desc_entry(self):
            self.description_entry = tk.Entry(self.root, width=40)
            self.description_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        def display_date_entry(self):
            self.date_entry = tk.Entry(self.root, width=40)
            self.date_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
