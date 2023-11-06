import csv
def read_csv(path):
    with open(path) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        print(f"Headings:\n{headings}")
        print("Values:")
        for values in csv_reader:
            print(values)

def run_task1():
    read_csv("clothing.csv")


if __name__ == "__main__":
    run_task1()