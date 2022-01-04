student_list = [
    {"name": "zjh",
     "age": 18},
    {"name": "cwy",
     "age": 50}
]

# 完整的for循环
for student in student_list:
    print(student)
    if student["name"] == "zjh":
        print(student["name"])
        break
else:
    print("not found")
