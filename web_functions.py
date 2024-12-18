import functions

def add_todos(user_input):
    if user_input.strip():  # Prevent adding empty or invalid inputs
        todos = functions.get_todos()
        todos.append(user_input.strip() + '\n')  # Add newline to the new input
        todos = [todo.strip() + '\n' for todo in todos]  # Clean up all items
        functions.write_todos(todos)

