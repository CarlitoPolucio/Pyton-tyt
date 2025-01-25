students = range(1, 6)

stupid_count = 0

for student in students:
    grade = int(input("Enter the grade: " ))
    if grade <= 2:
        stupid_count += 1
    else:
        break

print(stupid_count)

