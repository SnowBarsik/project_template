import os.path

def console_output(data):
    """
    Writes data is console
    
    arguments: string or list
    return: None
    
    Do nothing if argument or element in list is not string.
    >console_output("jjjjjjjjj")
    >jjjjjjjjj
    >console_output(["1", "2", "3"])
    >1
    >2
    >3
    >console_output([1, 2, "3"])
    >3
    """
    if isinstance(data, list):
        for line in data:
            if isinstance(line, str):
                print(line)
    elif isinstance(data, str):
        print(data)
    return None

def file_write(data, file_name, clear_mode=True):
    """
    Writes data in file using python functional.
    
    
    arguments:  (string/list) data, 
                (string) file_name,
                (bool) clear_mode - choose if data in file need to be saved before writing or not
    return: None
    
    Do nothing if argument is not string/list or file is not exists.
    >file_write("data", "file.txt")
    file.txt>data
    >file_write("data", "da")
    None
    >file_write([1, 2, 3], "file.txt")
    file.txt>1
    file.txt>2
    file.txt>3
    >file_write("data", "file.txt", False)
    file.txt>1
    file.txt>2
    file.txt>3
    file.txt>data
    """
    if os.path.isfile(file_name) and (isinstance(data, str) or isinstance(data, list)):
        if not clear_mode:
            f = open(file_name, "r")
            save_data = f.read()
        f = open(file_name, "w")
        if not clear_mode:
            f.writelines(save_data+"\n")
        f.writelines(data)
    return None