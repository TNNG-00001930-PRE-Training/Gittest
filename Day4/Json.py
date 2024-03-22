import json

# creating dict for json
emp_dic = {"name": "Mozammil", "hobbies":["Chess", "Keybord", "Dance"]}
print(type(emp_dic))
employee_dic = json.dumps(emp_dic)
print(type(employee_dic))
emp = json.loads(employee_dic)
print(type(emp))

print("Employee info: ", employee_dic)


print("Employee hobbies are: ", emp["hobbies"])