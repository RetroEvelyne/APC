student_grade_percentage = int(input("Whats the percentage the student got? > "))

if student_grade_percentage < 50:
    print("Failed")
elif student_grade_percentage < 60:
    print("Pass")
elif student_grade_percentage < 70:
    print("Merit")
else:
    print("Distinction")

