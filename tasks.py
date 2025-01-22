class Task:
    def __init__(self, name_of_task, description, deadline, status=False):
        self.name_of_task = name_of_task
        self.description = description
        self.deadline = deadline
        self.status = status

    def mark_as_done(self):
        self.status = True

    def __str__(self):
        status = "Completed" if self.status else "Not completed"
        return f'Task name: {self.name_of_task}\nDescription: {self.description}\nDeadline: {self.deadline}\nIs completed: {self.status}'




