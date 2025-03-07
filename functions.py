def read_files():
    with open('todos.txt', 'r') as file:
        todos = file.readlines()
    return todos

def write_files(todos):
    with open('todos.txt', 'w') as file:
        file.writelines(todos)

def add_todos(user_input):
    todo = user_input.strip()
    todos = read_files()
    todos.append(todo + '\n')
    write_files(todos)

def show_todos():
    todos = read_files()
    if len(todos) == 0:
        print("No todos to show!")
    else:
        for index, item in enumerate(todos,1):
            item = item.strip('\n')
            row = f"{index} - {item} "
            print(row)

def edit_todos():

    todos = read_files()
    if len(todos) == 0:
        print("No todo to edit")
        return

    else:
        show_todos()

        edit = int(input("Which todo you want to edit"))-1
        new_task = input("Enter task")
        todos[edit] = new_task + '\n'
        write_files(todos)
        print("Task Updated")

def delete_todos():
    todos = read_files()
    if len(todos) == 0:
        print("No todos to delete!")
        return
    else:
        show_todos()

        delete_index = int(input("Which item to delete : ")) - 1
        deleted_task = todos.pop(delete_index).strip()
        write_files(todos)
        print(f"{deleted_task} has been deleted")