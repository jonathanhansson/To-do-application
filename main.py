import tkinter as tk

import sys
from tasks import *
from todolist import *
from ToDoApp import *


# Skapa ToDoList- och Tkinter-root
root = tk.Tk()
my_todolist = ToDoList()
app = ToDoApp(root, my_todolist)

# Starta Tkinter-händelseloopen
root.mainloop()

task_choices = ["Show all tasks", "Add task", "Delete task", "Search based on title", "Mark task as completed", "Exit program"]

while (True):
    i = 0
    print("\n")
    while i < len(task_choices):
        print(i + 1, task_choices[i])
        i += 1

    choice = input("\nChoose an alternative (1-4)?")

    if choice == "1":
        jonathan_todolist.list_tasks()
        input("Press enter to continue...")
        continue

    elif choice == "2":
        title = input("\nGive the task a name: ")
        description = input("\nDescribe the task: ")
        deadline = input("\nDeadline: ")
        task = Task(title, description, deadline)
        jonathan_todolist.add_task(task)
        continue

    elif choice == "3":
        jonathan_todolist.list_tasks()
        title = input("\nGive the task title: ")
        jonathan_todolist.remove_task(title)
        continue

    elif choice == "4":
        title = input("\nGive the task title: ")

        jonathan_todolist.find_task(title)
        continue

    elif choice == "5":
        jonathan_todolist.list_tasks()
        done_index = int(input("\nWhich task is done (input just the num): ")) - 1
        jonathan_todolist.tasks[done_index].status = True

    elif choice == "6":
        sys.exit(0)












