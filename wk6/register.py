def print_reversed(arr):
    for el in reversed(arr):
        print(f" > {el}")

students = []

for _ in range(5):
    name =  input("Please input a students name > ")
    students.append(name)

print("Here are the students in reverse:")
print_reversed(students)
