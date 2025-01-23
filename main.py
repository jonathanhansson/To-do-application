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













