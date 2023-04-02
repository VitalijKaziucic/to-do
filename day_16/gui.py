import time
import PySimpleGUI as sg
from day_1 import write_file, read_file

sg.theme("Black")


class ToDoApp:
    file_name = "todo.txt"

    def __init__(self):
        self.todos = [todo.strip() for todo in read_file(self.file_name)]
        self.layout = [
            [sg.Text(size=(40, 1), key="time")],
            [sg.Text("Enter a to-do:")],
            [sg.InputText(key="-Input-"), sg.Button(size=(10, 1), button_text="Add")],
            [sg.Text(size=(40, 1), key="-Output-")],
            [sg.Listbox(size=(43, 10), values=self.todos, key="todo_list", bind_return_key=True),
             sg.Button(key="edit", button_text="Edit", size=(10, 1)),
             sg.Button(key="complete", button_text="Complete", size=(10, 1))
             ],
            [sg.Button(key="exit", button_text="Exit", pad=(10, 10), size=(10, 1))]
        ]
        self.old_value = None

        self.window = sg.Window("To Do App", self.layout, size=(580, 320))

    def run_app(self):
        while True:

            event, values = self.window.read(timeout=1)
            match event:
                case sg.WINDOW_CLOSED | "exit":
                    edit_todo_list = [todo + "\n" for todo in self.todos]
                    write_file(self.file_name, edit_todo_list)
                    break
                case "Add" | "edit" | "complete":
                    new_todo = values["-Input-"].title()
                    if new_todo and not self.old_value:
                        self.todos.append(new_todo)
                    elif new_todo and self.old_value:
                        todo_index = self.todos.index(self.old_value)
                        if event != "complete":
                            self.todos[todo_index] = new_todo
                        else:
                            self.todos.remove(self.old_value)
                        self.old_value = None
                    self.window["-Input-"].update("")
                    self.window["todo_list"].update(self.todos)
                case "todo_list":
                    selected_value = values["todo_list"][0]
                    self.window["-Input-"].update(selected_value)
                    self.old_value = selected_value
                case _:
                    self.window["time"].update(time.strftime("%Y-%m-%d %H:%M:%S"))

        self.window.close()


app = ToDoApp()
app.run_app()
