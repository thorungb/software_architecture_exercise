import json
import os

# data layer
class TodoDatabase:
    FILE_PATH = "tasks.json"

    def load_tasks():
        if not os.path.exists(TodoDatabase.FILE_PATH):
            return []
        with open(TodoDatabase.FILE_PATH, "r") as file:
            return json.load(file)

    def save_tasks(tasks):
        with open(TodoDatabase.FILE_PATH, "w") as file:
            json.dump(tasks, file, indent=4)


# business layer
class TodoController:
    def __init__(self):
        self.tasks = TodoDatabase.load_tasks()

    def add_task(self, title):
        task = {"id": len(self.tasks) + 1, "title": title, "completed": False}
        self.tasks.append(task)
        TodoDatabase.save_tasks(self.tasks)
        return task

    def list_tasks(self):
        return self.tasks

    def mark_completed(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                TodoDatabase.save_tasks(self.tasks)
                return task
        return None

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task["id"] != task_id]
        TodoDatabase.save_tasks(self.tasks)


# presentation layer
class TodoApp:
    def __init__(self):
        self.service = TodoController()

    def show_menu(self):
        while True:
            print("\nTODO List Application")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task as Completed")
            print("4. Delete Task")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.complete_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                print("Thank you!")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_task(self):
        title = input("Enter task title: ")
        task = self.service.add_task(title)
        print(f"Task alreay added with ID: {task['id']}")

    def view_tasks(self):
        tasks = self.service.list_tasks()
        if not tasks:
            print("No tasks found.")
        else:
            for task in tasks:
                status = "✔" if task["completed"] else "✖"
                print(f"[{status}] {task['id']}: {task['title']}")

    def complete_task(self):
        task_id = int(input("Enter task ID to mark as completed: "))
        task = self.service.mark_completed(task_id)
        if task:
            print(f"Task {task_id} marked as completed.")
        else:
            print("Task not found.")

    def delete_task(self):
        task_id = int(input("Enter task ID to delete: "))
        self.service.delete_task(task_id)
        print(f"Task {task_id} deleted.")

if __name__ == "__main__":
    app = TodoApp()
    app.show_menu()
