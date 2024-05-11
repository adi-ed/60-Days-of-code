while True:
    user_action = input("Add,show items, edit items,mark as complete or exit: ")
    user_action = user_action.strip()
    
    match user_action:
        #Match case conditions
        case 'add':           
            with open("todo.txt",'r') as file:
                todos = file.readlines()
            # Input new element to add in the list    
            todo = input('Enter Item to add: ')
            todos.append(todo + '\n')
            # Append the item back to textfile
            with open("todo.txt", 'w') as file:
                file.writelines(todos)
            #Print current list of items
            print(todos)
            
        case 'show':
            with open("todo.txt",'r') as file:
                todos = file.readlines()
            for index,item in enumerate(todos):
                row=f"{index + 1}.{item.strip('\n')}"
                print(row)             
        case 'exit':
            break
        case 'edit':
            index = int(input("Enter index: "))
            index = index -1
            
            with open("todo.txt",'r') as file:
                todos = file.readlines()
            
            print("To-dos before editing: ",todos)
            
            new_item = input("Enter new item: ")   
            todos[index] = new_item + '\n'
            
            print("To-dos after editing: ",todos)
            
            with open("todo.txt", 'w') as file:
                file.writelines(todos)
            
        case 'complete':
            id = int(input("Enter item no you want to mark as completed: "))
            with open("todo.txt",'r') as file:
                todos = file.readlines()
                
            todos.pop(id-1)
            
            with open("todo.txt", 'w') as file:
                file.writelines(todos)
            
print("Final To-do list: ",todos)