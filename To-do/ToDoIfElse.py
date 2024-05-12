from modules import Functions
import time

curr = time.strftime("%b %m, %Y %H:%M:%S")
print("Currently it is ",curr)
while True:
    user_action = input("Add,show items, edit items,mark as complete or exit: ")
    user_action = user_action.strip()
    if user_action.startswith('add'): 
        todos = Functions.open_file_read()
        todos.append(user_action[4:] + '\n')
        
        Functions.write_to_file(todos)

        print(todos)
        
    elif user_action.startswith('show'):
        todos = Functions.open_file_read()
        for index,item in enumerate(todos):
            row=f"{index + 1}.{item.strip('\n')}"
            print(row)             
                
    elif user_action.startswith('exit'):
        print("List Complete!")
        break
    
    elif user_action.startswith('edit'):
        try:
            index = int(user_action[5:]) - 1
            todos = Functions.open_file_read()
                
            print("To-dos before editing: ",todos, '\n')
            
            new_item = input("Enter new item: ")   
            todos[index] = new_item + '\n'
            
            print("To-dos after editing: ",todos,'\n')
            
            Functions.write_to_file(todos)
        except ValueError:
            print("Enter a valid command.")
            continue
        
    elif user_action.startswith('complete'):
        try:
            todos = Functions.open_file_read()
            item_removed = todos[int(user_action[9:])-1]
            id = int(user_action[9:])    
            todos.pop(id-1)
            
            Functions.write_to_file(todos)
            print(f"Item \"{item_removed.strip('\n')}\" is removed from the list.\n")
        except IndexError:
            print("Enter a valid command!")
            continue
    else:
        print("Enter a valid command!")
        
print("Final To-do list: ",todos)