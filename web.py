import streamlit as st
import functions
import web_functions

# Load the todos into session_state only once
if "todos" not in st.session_state:
    st.session_state.todos = functions.get_todos()

if "edit_index" not in st.session_state:
    st.session_state.edit_index = None  # Track the selected item for editing

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase productivity.")

# Add/Edit/Show Actions
action = st.radio("Choose an action:", ("Add", "Edit", "Show"))

if action == "Add":
    new_todo = st.text_input("Enter a new to-do:", key="new_todo_input")
    if st.button("Add"):
        if new_todo.strip():  # Only add non-empty todos
            web_functions.add_todos(new_todo)
            st.session_state.todos = functions.get_todos()  # Reload updated todos
            st.query_params["refresh"] = "true"  # Force a refresh
        else:
            st.warning("To-do cannot be empty!")

elif action == "Edit":
    st.write("### Click a Task to Edit")
    for index, todo in enumerate(st.session_state.todos):
        if st.button(todo.strip(), key=f"edit_button_{index}"):
            st.session_state.edit_index = index

    # If an item is selected for editing
    if st.session_state.edit_index is not None:
        st.write(f"Editing Task: {st.session_state.todos[st.session_state.edit_index]}")
        new_value = st.text_input(
            "Update the to-do:",
            value=st.session_state.todos[st.session_state.edit_index].strip(),
        )
        if st.button("Save"):
            if new_value.strip():  # Ensure the new value is not empty
                web_functions.edit_todo(st.session_state.edit_index, new_value)
                st.session_state.todos = functions.get_todos()  # Reload updated todos
                st.session_state.edit_index = None  # Clear the edit state
                st.query_params["refresh"] = "true"  # Force a refresh
            else:
                st.warning("Updated to-do cannot be empty!")


elif action == "Show":
    st.write("### Current To-Do List")
    for index, todo in enumerate(st.session_state.todos):
        st.write(f"- {todo.strip()}")
