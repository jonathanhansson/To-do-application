class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.pop(task - 1)

    def list_tasks(self):
        if not self.tasks:
            print("No tasks yet")

        print("_" * 20)
        for i, task in enumerate(self.tasks, start=1):
            print(f"Task {i}:")
            print(task)
            print("_" * 20)

    def find_task(self, title):
        for task in self.tasks:
            if task.name_of_task == title:
                print(f"Found task:\n{task}")
        return None

    def mark_done(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_as_done()




