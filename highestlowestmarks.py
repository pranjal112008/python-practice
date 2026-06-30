marks=[]
for i in range(5):
    mark=int(input(f"enter mark {i+1}:"))
    marks.append(mark)
print("Highest marks:",max(marks))
print("Lowest marks:",min(marks))
print("Total marks:",sum(marks))