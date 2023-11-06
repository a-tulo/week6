import  os
def cwd():
    path = os.getcwd()
    print(f"The current working directory is {path}")
    print(f"The directory contains the following:")
    for file in os.listdir(path):
        print(file)

def display_chars(path, num_char):
    with open(path) as file:
        data = file.read(num_char)
    print(f"The first {num_char} characters are:")
    print(data)

def display_line(path):
    with open(path) as file:
        line = file.readline().strip()
    print("The first line is:")
    print(line)

def display_text(path):
    with open(path) as file:
        data = file.read()
    print("The full text is:")
    print(data)

def run_task2():
    path = "library.txt"
    display_chars(path, 5)
    print()
    display_line(path)
    print()
    display_text(path)

def run():
    print("Processsing...")
    cwd()

if __name__ == "__main__":
    run_task2()