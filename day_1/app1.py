import time
from day_1 import write
from day_1 import read


class Task:

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        content = ",".join(f"{str(key).replace('_', '')}='{value}'" for key, value in self.__dict__.items())
        return f"{Task.__name__}({content})"


class ToDoList:

    user_prompt = "Enter add, show, edit, complete or exit: "
    add_task = "Enter a todo: "
    empty_list = "List is empty!"
    edit_prompt = "Number of the todo to edit: "
    complete_prompt = "Number of the todo to complete: "
    file_name = "todos.txt"

    def start_app(self):
        todo_list = read.read_file(self.file_name)
        while 1:
            today_datetime = time.strftime("It is %B %d, %Y %H:%M:%S")
            print(today_datetime)
            user_input = input(self.user_prompt).strip().split()
            command, task = user_input[0].lower(), " ".join(user_input[1:]).title() + "\n"
            match command:
                case "exit":
                    break
                case "add":
                    # user_input = input(self.add_task).strip().title() + '\n'
                    todo_list.append(task)
                case "show":
                    for index, task in enumerate(todo_list, 1):
                        print(f"{index}. {task.strip()}")
                case "edit":
                    try:
                        number = int(task)
                    except ValueError:
                        print("Your command is not valid")
                    else:
                        number -= 1
                        new_task = input(self.add_task).strip().title() + '\n'
                        todo_list[number] = new_task
                case "complete":
                    try:
                        number = int(task)
                        number -= 1
                        completed = todo_list.pop(number)
                    except ValueError:
                        print("Your command is not valid")
                    except IndexError:
                        print("There is no item with provided number")
                    else:
                        completed = completed[:-1]
                        print(f"Task {completed} removed from the list")
                case _:
                    print("You entered unknown command!")
        write.write_file(self.file_name, todo_list)



