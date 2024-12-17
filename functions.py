#custom function
#Constant 
FILEPATH = "todos.txt"

# Open the 'todos.txt' file in read mode to read existing to-do items.
"""file variable hold the file object when the open() is call. when the file is open,
it allow other method such as read and write for me to manipulate my txt file. 
"""
def get_todos(file_path=FILEPATH):
    """
    Reads all the lines from a specified file and returns them as a list.

    Parameters:
        file_path (str): The path to the file to be read. Defaults to "todos.txt".

    Returns:
        list: A list of strings, where each string is a line from the file.
    """
    with open(file_path, 'r') as file_local:
        # Read all lines from the file and store them in a list.
        todos_list_local = file_local.readlines()
    return todos_list_local


def write_todos(todos_local, file_path=FILEPATH):
    """
    Writes a list of todos to a specified text file.

    Parameters:
        todos_local (list): A list of todo items to write into the file.
        file_path (str): The path to the file where the todos will be written. Defaults to "todos.txt".

    Returns:
        None: This function does not return anything. It simply updates the specified file.
    """
    with open(file_path, 'w') as file:
        # Write each todo item from the list into the file.
        file.writelines(todos_local)
        
if __name__ == "__main__":
    print("Hello")
    print(get_todos())
    