studentMarks = float(input("Enter Students Marks: "))
grade = "None"
if studentMarks < 0 or studentMarks > 20:
    print("Marks are inValid !!")
elif studentMarks >= 16:
    grade = "Very good"
elif studentMarks >= 14:
    grade = "Good"
elif studentMarks >= 12:
    grade = "Fairly good"
elif studentMarks >= 10:
    grade = "Pass"
else:
    grade = "Fail"
print(f"Student Grade is {grade}")