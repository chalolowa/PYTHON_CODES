def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("This content i've just learned.\n")
            file.write("Honestly, i never liked files both reading n writing.\n")
            file.write("So this is me 6 years down the line in programming returning to learn file manipulation. In the year 2024. \n")
        print("Opreration Successful!!")
    except FileExistsError:
        print("File with same name already exists!!!")
    except Exception as e:
        print(f"Error writinf to file: \n {e}")
        
def read_display_file():
    try:
        with open("my_file.txt", "r") as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print("File not found!!")
    except Exception as e:
        print(f"Error reading file: \n {e}")
        
def add_lines_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Okay, I'm supposed to add 3 more lines. \n")
            file.write("Honestly, i do not know what to add. \n")
            file.write("Am just gonna go with the above sentences if you don't mind. \n")
        print("Operation Successful")
    except Exception as e:
        print(f"Error appending to file: \n {e}")
        

create_file()
read_display_file()
add_lines_to_file()
read_display_file()
