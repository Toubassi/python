students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

#Part 1
def iterateDictionary(some_list):
  for student in some_list:
    print(f"first_name - {student['first_name']}, last_name - {student['last_name']}")

iterateDictionary(students) 

#Part 2
def itrateDictionary2(key, some_list):
  for x in some_list:
    print(x[key])

itrateDictionary2('first_name', students)
itrateDictionary2('last_name', students)
