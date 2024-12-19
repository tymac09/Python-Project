import streamlit as st
import functions
import uuid  # Import UUID for generating unique keys


def _update_todos(todos):
    """
    Helper function to clean up and save todos.

    Parameters:
        todos (list): List of todos to save.

    Returns:
        None
    """
    # Ensure all todos are consistently formatted with a newline
    formatted_todos = [todo.strip() + '\n' for todo in todos]
    functions.write_todos(formatted_todos)


def display_todos(todos, edit_key="edit_index"):
    """
    Display the list of todos as checkboxes in Streamlit.

    Parameters:
        todos (list): The list of todos to display.
        edit_key (str): The session_state key to track the selected index for editing.

    Returns:
        None
    """
    for index, todo in enumerate(todos):
        col1, col2 = st.columns([0.05, 0.95])
        with col1:
            # Generate a unique key for each checkbox
            unique_key = f"check_{index}_{str(uuid.uuid4())}"
            selected = st.checkbox("", key=unique_key)
            if selected:
                st.session_state[edit_key] = index
        with col2:
            st.write(todo.strip())


def add_todos(user_input):
    """
    Add a new to-do item to the list.

    Parameters:
        user_input (str): The new to-do item to add.

    Returns:
        None
    """
    if user_input.strip():  # Prevent adding empty or invalid inputs
        todos = functions.get_todos()
        todos.append(user_input.strip() + '\n')  # Add newline to the new input
        _update_todos(todos)


def edit_todo(index, new_value):
    """
    Edit a specific to-do item at a given index.

    Parameters:
        index (int): The position of the item to be edited.
        new_value (str): The updated value for the to-do item.

    Returns:
        None
    """
    todos = functions.get_todos()
    try:
        todos[index] = new_value.strip() + '\n'  # Update the value at the given index
        _update_todos(todos)
    except IndexError:
        raise ValueError(f"Invalid index {index}. Unable to edit to-do.")


def complete_todo(index):
    """
    Remove a specific to-do item from the list.

    Parameters:
        index (int): The position of the item to remove.

    Returns:
        None
    """
    todos = functions.get_todos()
    try:
        todos.pop(index)  # Remove the item at the given index
        _update_todos(todos)
    except IndexError:
        raise ValueError(f"Invalid index {index}. Unable to complete to-do.")
