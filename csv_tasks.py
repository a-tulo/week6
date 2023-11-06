import csv
def read_csv(path):
    with open(path) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        print(f"Headings:\n{headings}")
        print("Values:")
        for values in csv_reader:
            print(values)

def extract(path):
    print("Extracting...")

    with open(path) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        names = ""
        for values in csv_reader:
            names += f"{values[1]}\n"
    print("Done!")
    print(f"The extracted items are: \n{names}")

def run_task1():
    read_csv("clothing.csv")
def run_task2():
    extract("clothing.csv")


if __name__ == "__main__":
    run_task2()