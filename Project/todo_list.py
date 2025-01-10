class TodoList:
    def __init__(self):
        self.tasks = []
        
    def add_task(self, task_name):
        task = {"name": task_name, "status": "Pending"}
        self.tasks.append(task)
        
    def list_tasks(self):
        return self.tasks
    
    def mark_task_as_completed(self, task_name):
        for task in self.tasks:
            if task["name"] == task_name:
                task["status"] = "Completed"
                break
    
    def clear_tasks(self):
        self.tasks.clear()

    def delete_task(self, task_name):
        self.tasks = [task for task in self.tasks if task["name"] != task_name]
    
    def edit_task(self, old_name, new_name):
        for task in self.tasks:
            if task["name"] == old_name:
                task["name"] = new_name
                break
