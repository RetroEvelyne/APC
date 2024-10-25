student_grades = {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 78,
        "David": 95,
        "Eve": 88
        }

print("Class Grades:")
for name, grade in student_grades.items():
    print(f"{name} : {grade}")


top_student_value = max(student_grades.values())

for name in student_grades.keys():
    if student_grades[name] == top_student_value:
        print(f"\nTop student: {name} with grade {top_student_value}")
        exit()


