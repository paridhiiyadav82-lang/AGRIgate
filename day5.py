student={'name':'Paridhi', 'age':'17', 'stream':['Physics', 'chem', 'math']}
print(student['name'])
print(student.get('name'))
print(student.get('phone', 'not found')) #will return as none because this key isnt there in the dictionary - not found is whats going to show up now that we specifced it 

#if u want to add a key 
student['phone']='88888888'
print(student['phone'])

#if u wanna update the dic 
student.update({'name': 'kuhu', 'age':'21'})
print(student)

#delete a key 
del student['phone']
print(student)
#phone=student.pop('phone')

#how many keys?
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key,value in student.items():
    print(key, value)