from app.io.input import *
from app.io.output import *

def main():
    for i in range(0,3):
        input_data = console_input() if i==0 else file_read("data\demofile.txt") if i==1 else pandas_file_read("data\demofile.csv")
        console_output(input_data)
        file_write(input_data, "data\output.txt", False)
    return None


if __name__ == "__main__":
    main()