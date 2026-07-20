def analyze_marks():
    try:
        n = int(input("How many students? "))
        if n <= 0:
            print("Please enter at least 1 student.")
            return
        marks = []
        for i in range(n):
            m = int(input(f"Enter marks of student {i+1}: "))
            marks.append(m)
        print("\n" + "="*40)
        print("          MARKS ANALYSIS")
        print("="*40)
        print(f"Total Students   : {n}")
        print(f"Marks List       : {marks}")
        print(f"Highest Marks    : {max(marks)}")
        print(f"Lowest Marks     : {min(marks)}")
        print(f"Total Marks      : {sum(marks)}")
        print(f"Average          : {sum(marks)/n:.2f}")
        print("="*40)
    except ValueError:
        print("Please enter valid numbers!")

analyze_marks()
