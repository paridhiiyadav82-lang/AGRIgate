message="hello, world"
print(message.count('l'))
replaced_message=message.replace('world' , 'universe')
print(replaced_message)
name=input("hi whats ur name? ")
print("hello", name)
x=7
print(x*7)
x="7"
print(x*7)
greeting='hello'
print(greeting+ ', ' , name + '. Welcome to learning python!')

placeholder='{}, {}. Welcome to learning python!'.format(greeting, name)
print(placeholder)

#or do this using the f string
placeholder_with_fstring=f"{greeting}, {name.upper()}. Welcome to learning python!"
print(placeholder_with_fstring)