#import functions.py 
import functions, time


 #display date and time 
date = time.strftime("%Y-%m-%d | %H:%M:%S", time.localtime())
print(f"Current Time: {date}" )
    
# while loop to keep asking user for input
while True:

    user_action = input("Type add or show or exit or edit or complete:  ")
    #remove the space after the string 
    user_action = user_action.strip()
    
    if user_action.startswith('add'):
        # slicing the user input to take everything after the word add and storing it in todo
        todo = user_action [4:]
        #use the function to open the todos.txt
        todos_list= functions.get_todos()
            
        # Add the new to-do item to the list of existing to-dos.
        todos_list.append(todo +'\n')

        # Open the 'todos.txt' file in write mode to update it with the new list.
        # Write the updated list of to-do items back to the file.
        functions.write_todos(todos_list)
        
    elif user_action.startswith('show'): 
        #use the function to open the todos.txt
        todos_list= functions.get_todos()
             
        """
        for item in todos_list is to iterate over the todos_list, the item is remvoe of any space using strip
        and then return the item and store in a new list called new_todos
        """
          #list comprehension to edit the exisitng list 
        new_todos_list = [item.strip('\n') for item in todos_list]
            
        
        #display the list using for loop
        #display the list with it index using enumerating the list
        for index, item in enumerate(new_todos_list):
            #start the index count at 1 instead of 0
            row = f"{index + 1 }.{item}"
            print(row)
            
    elif  user_action.startswith('edit'):
        #try the code first and run it wihtout crashing
        try:
            #ask user to chose which item they want to edit
            number = int(user_action[5:])
            """
            list indexing to edit indiviaul item in the list
            and put the number into the todos_list in order to find the individual item to edit
            """
            number = number - 1 #since py list start with 0 
            #open exisitng todos
            #todoslist now hold all the exisitng item within todos.txt
            #use the function to open the todos.txt
            todos_list= functions.get_todos()
            #user enter what to replace it with
            new_todo = input("Enter what you want to replace it in: ")
            #list indexing accessing a specific index item to change
            todos_list [number] = new_todo +'\n'
            #once the todo_list change, put the string list back into the text file by write
            functions.write_todos(todos_list)
            #if this specifie error occur, dont crash the program, show the message and re direct user to the prompt and enter correct command
        except ValueError:
            print("Your command is not valid")
            #ignore everything after this line and go back to the begining of the loop
            continue

        
        #complete option for user
    elif user_action.startswith('complete'):
        try:
            #ask user what number they want to get rid
            number_to_mark_complete = int(user_action[9:])
            
            #open the todos.txt and put all content into the todos_List var 
            #todo_list now hold all the item of the text file as a list of string
            #use the function to open the todos.txt
            todos_list= functions.get_todos()
            
            index = number_to_mark_complete-1
            #list indexing to access the specific item that is being removed
            removed_item = todos_list[index].strip('\n')
            print(f"the task {removed_item} will be removed")
            #remove item of the list of string
            todos_list.pop(index)
            #write it back into the text file 
            functions.write_todos(todos_list)
            #message of completion
            message = f"the item {removed_item} was successfully removed"
            print(message)
        except ValueError:
            print("Your command is invalid")
            continue
        except IndexError:
            print("Item doesn't exist")
            continue

    elif user_action.startswith('exit'):
            
            break
    else: 
        print("check command")
            
            
            
            








































