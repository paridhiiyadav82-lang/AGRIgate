subjects=['math', 'eng', 'compsci', 'chem']
print(subjects)
print("how many items in this list?", len(subjects))
print("do you wanna know whats my  fav subject? its", subjects[0])
print(subjects[-1]) #instead of -1 you could write 3 but -1 is helpful when you don't know the length of the list
print(subjects[0:2]) # first index i.e 0 is incluse but last index i.e 2 isnt
#if you want to add items to the list 
subjects.append("physics")
print(subjects)
#if you want to add the item at a specific position 
subjects.insert(2, "physics")
print(subjects)

#inserting list under a list 
subjects_2 = ["art", "psychology"]
#subjects.insert(0, subjects_2)
#print(subjects)

#adding the items of one list into another
subjects.extend(subjects_2)
print(subjects)

#to remove 
subjects.remove("eng")
print(subjects)

#reverse
subjects.reverse()
print(subjects)

#in alphabetical order
subjects.sort()
print(subjects)

#or 
sorted_subjects=sorted(subjects)
print(sorted_subjects)

numbers=[1,2,5,3,8,4,6,7,9,0,8]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#to find out the positon of an item 
print(subjects.index("compsci"))

#to check if an item is in the list 
print("math" in subjects)

#to print out all items in the list one below each other 
for items in subjects:
    print(items)

#along with their index number 
for index,course in enumerate(subjects, start=1):
    print(index,course)

#to define how u wanna join the list 
courses_joined=', '.join(subjects)
print(courses_joined)  

#change an item in the list 
subjects[0]="Marketing"
print(subjects)

#for lists = []
#for tuples = ()
#for sets = {} - dont care about order 

humanities_subjects={"pol sci", "geography", "history", "econ", "econ", "marketing"} #dont show duplicates
print(humanities_subjects)

commerce_subjects={"accounts", "math", "econ", "marketing"}
print(commerce_subjects.intersection(humanities_subjects))
print(commerce_subjects.difference(humanities_subjects))
print(commerce_subjects.union(humanities_subjects))
