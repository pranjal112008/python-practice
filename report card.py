def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"
try:
    marks = int(input("Enter marks obtained: "))
    if 0 <= marks <= 100:
        grade = get_grade(marks)
        print(f"Grade of the student: {grade}")
    else:
        print("Marks should be between 0 and 100.")
except ValueError:
    print("Please enter a valid number!")
