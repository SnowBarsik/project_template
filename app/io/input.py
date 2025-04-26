import os.path
import pandas as pd

def console_input():
    """
    Returns data from console
    
    arguments: None
    return: string or list of strings
    
    Reads by one stroke while user not write "stop111" as a stroke. 
    Adds endline to each of element for comfortable writing in file.
    
    >console_input()
    >llll
    >hhhhh
    >stop111
    ['llll\n', 'hhhhh\n']
    """
    input_stroke=input()
    res=list()
    while(not input_stroke=="stop111"):
        res.append(input_stroke+"\n")
        input_stroke=input()
    return res

def file_read(file):
    """
    Returns data from file using python functional.
    
    arguments: (string) file_name
    return: (string) file_data
    
    Reads file if it exists as string and than returns.
    >file_read("data/output.txt")
    lol
    >file_read("da")
    None
    """
    if os.path.isfile(file):
        f = open(file, "r")
        return f.read()
    return None

def pandas_file_read(file):
    """
    Returns data from file using pandas functional.
    
    arguments: string
    return: string
    
    Reads file if it exists and have one of types: csv, xlsx or json as string and than returns.
    """
    data = None
    if os.path.isfile(file):
        match file.split('.')[-1]:
            case "csv": data = pd.read_csv(file)
            case "xlsx": data = pd.read_excel(file)
            case "json": data = pd.read_json(file)
        return data.to_string(index=False)
    return None