# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# def chane_value1():
#     x[1][0]=15
#     return x

# print(chane_value1())

# def  change_last_name():
#     students[0]["last_name"] = "briant"    
#     return students

# print(change_last_name())

# def changeDirectory():
#     sports_directory['soccer'][0]='andres'
#     return sports_directory

# print(changeDirectory())



# # Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# # Change the last_name of the first student from 'Jordan' to 'Bryant'
# # In the sports_directory, change 'Messi' to 'Andres'
# # Change the value 20 in z to 30


# students = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}

#     ]
# # iterateDictionary(students) 
# # # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # # bonus to get them to appear exactly as below!)
# # first_name - Michael, last_name - Jordan
# # first_name - John, last_name - Rosales
# # first_name - Mark, last_name - Guillen
# # first_name - KB, last_name - Tonel


# def iterateDictionary(student_list):
#     for student in student_list:
#         print(f"first_name -{student['first_name']} ,last_name-{student['last_name']}")
        
# iterateDictionary(students)

# def iterateDictionary(student_list):
#     for student in student_list:
#         print(f"{student['first_name']} - {student['last_name']}")





    # students = [
    #     {'first_name': 'Michael', 'last_name': 'Jordan'},
    #     {'first_name': 'John', 'last_name': 'Rosales'},
    #     {'first_name': 'Mark', 'last_name': 'Guillen'},
    #     {'first_name': 'KB', 'last_name': 'Tonel'}
    # ]

    # def iterateDictionary2(key_name, some_list):
    #     for dictionary in some_list:
    #         print(dictionary[key_name])

    # iterateDictionary2('first_name', students)


    # iterateDictionary2('last_name', students)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}



def printInfo(some_dict):
    for key, values in some_dict.items():
        print(f"{len(values)} {key.upper()}")
        for value in values:
            print(value)
        print()

printInfo(dojo)
