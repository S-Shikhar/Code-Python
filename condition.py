
n = int(input("Enter the number of the students: "))

while (n != 0):
    roll = int(input("Enter the roll of the student: "))
    marks = int(input("Enter the marks of the student: "))

    if marks >= 90:
        print("grade = A")
    elif marks >= 80 and marks < 90:
        print("grade = B")
    elif marks >= 70 and marks < 80:
        print("grade = C") 
    else:
        print("grade = D")
    n -= 1