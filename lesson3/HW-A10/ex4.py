student = ""
grade = 0
name = []

while student != "$$$":
    student = input("insert student's name and grade: ")
    if student != "$$$":
        name_grade = student.split(" ")
        grade += int(name_grade[1])
        name.append(name_grade[0])

print(f"the names are: {name} \nthe average grade is: {grade / len(name)} \nthe amount of names is: {len(name)}")