#student marks mean is 2f =56.00

# Step 1: Read number of students
n = int(input())

# Step 2: Store student data in a dictionary
students = {}

for _ in range(n):
    entry = input().split()        # split line by spaces
    name = entry[0]                # first part is name
    marks = list(map(float, entry[1:]))  # rest are marks as float
    students[name] = marks

# Step 3: Read query_name
query_name = input()

# Step 4: Compute average and print with 2 decimal places
average = sum(students[query_name]) / len(students[query_name])
print(f"{average:.2f}")
