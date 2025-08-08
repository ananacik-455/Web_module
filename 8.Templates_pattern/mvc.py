class TODOListModel:
    def __init__(self):
        self._tasks = []

    @property
    def tasks(self):
        return self._tasks

    def create_task(self, task: str):
        new_tasks = {"title": task, "is_completed": False}
        self.tasks.append(new_tasks)

    def complete_task(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["is_completed"] = True

    def remove_task(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

class ToDoListView:

    def display_tasks(self, tasks:list):
        print("ToDoList\n")
        if not tasks:
            print("Empty list")
        else:
            for task in tasks:
                # [✔️️] | [ ] | Title of task
                if task["is_completed"]:
                    status = "[✔️️]"
                else:
                    status = "[ ]"
                print(f"{status} | {task["title"]}", end="\n===========================\n")
            print("===========================")

    def display_message(self, message:str):
        print(f"Message: {message}")


class Controller:
