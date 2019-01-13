class Project:
    def __init__(self, tasks=None):
        self.tasks = tasks or {}

    def add_task(self, taskname, task):
        raise NotImplementedError

    def remove_task(self, taskname):
        raise NotImplementedError