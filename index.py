records = [
    ["Alice", "Engineering", "Palo City"],
    ["Bob", "Sales", "San Francisco"],
    ["Carol", "Sales", "San Francisco"],
    ["Dave", "Engineering", "Palo City"],
    ["Erin", "Engineering", "Denver"],
    ["Frank", "Engineering", "Omaha"],
    ["Grace", "Marketing", "San Francisco"]
]

city_index = {}

# Build up the city_index
for name, _, city in records:  # O(n) over the number of records
    if city not in city_index:
        city_index[city] = []

    city_index[city].append(name)
print(city_index)
dept_index = {}

# Build up the dept_index
for name, dept, _ in records:  # O(n) over the number of records
    if dept not in dept_index:
        dept_index[dept] = []

    dept_index[dept].append(name)
        
#print(dept_index)

# For a given department, which employees are in it?

def emp_by_dept_linear(dept):
    emps = []

    for r in records:  # O(n) over the number of records
        if r[1] == dept:
            emps.append(r[0])

    return emps

def emp_by_dept(dept):
    return dept_index[dept]  # O(1) over the number of records

print(emp_by_dept("Engineering"))
print(emp_by_dept("Sales"))
print(emp_by_dept("Marketing"))

