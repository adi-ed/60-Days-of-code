FILEPATH = "todo.txt"

def open_file_read(filepath = FILEPATH):
    """Function to Read Contents of the file to-do

    Args:
        filepath (str, optional): _description_. Defaults to "todo.txt".

    Returns:
        _type_: _description_
    """
    with open(filepath,'r') as file:
                todos = file.readlines()
    return todos

def write_to_file(todos,filename = FILEPATH):
    """Function to Write Content to file to-do

    Args:
        todos (_type_): _description_
        filename (str, optional): _description_. Defaults to "todo.txt".
    """
    with open(filename, 'w') as file:
            file.writelines(todos)
            
if __name__ == "__main__":
    print("Inside the Modules File")