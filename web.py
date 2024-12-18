import streamlit as st 
import functions, web_functions
  
todos = functions.get_todos()
st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("this app is to increase productivity.")

#show existing todos 
for index,todo in enumerate(todos):
    st.checkbox(todo.strip(), key= f"todo_{index}")
    
#gettin todos from user
user_input = st.text_input("Enter a todo: ")

#button dictionary to loop through instead of lots of if
buttons = {
    "Add": lambda: web_functions.add_todos(user_input),
    "Edit": "You have selected edit",
    "Show": "You have selected show",
    "Complete": "You have selected complete"
    
    }

#loop through each button
for lable,func in buttons.items():
    if st.button(lable):
        #call the function
        func()


    

