def analyze_marks(marks):
    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)
    passed = sum(1 for m in marks if m >= 40)
    failed = len(marks) - passed
    
    return total, average, highest, lowest, passed, failed

# Main Program
n = int(input("How many students? "))
marks = []
for i in range(n):
    m = int(input(f"Enter marks of student {i+1}: "))
    marks.append(m)

total, average, highest, lowest, passed, failed = analyze_marks(marks)

print("\n" + "="*40)
print("          MARKS ANALYZER REPORT")
print("="*40)
print(f"Total Students   : {n}")
print(f"Marks List       : {marks}")
print(f"Total Marks      : {total}")
print(f"Average Score    : {average:.2f}")
print(f"Highest Score    : {highest}")
print(f"Lowest Score     : {lowest}")
print(f"Passed           : {passed}")
print(f"Failed           : {failed}")
print("="*40)
