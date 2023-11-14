#1
# def a():
#     return 5
# print(a())
# when printing it back to the function and return the value 

# #2
# def a():
#     return 5
# print(a()+a())
# # in prtining it add the fuction speratly 

# #3
# def a():
#     return 5
#     return 10
# print(a())
# the function take the first retun and do not consider the second one 

#4
# def a():
#     return 5
#     print(10)
# print(a())
# the same as the previous one the return break out the function

#5
# def a():
#     print(5)
# x = a()
# print(x)
#  for x=a() it access the fuction but can not access the x it it called back in print 

#6
# def a(b,c):
#     print(b+c)
# print(a(1,2) + a(2,3))
#  it caculate the function and print the sum each one in seprate line 

# #7
# def a(b,c):
#     return str(b)+str(c)
# print(a(2,5))
# it ad the numberes as a string beside each other 

# #8
# def a():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(a())
# when we call the function it imediatly print b as the print inside the fuction then go to else and return the 10 and print it

# # #9
# def a(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(a(2,3))
# print(a(5,3))
# print(a(2,3) + a(5,3))
# first print it achive the if statment condtion and print the value 7 
# second print it achive the else statment condtion and print the value 14 
# and for the third print it passed the firt fucntion befor the plus and had an output of 7 and the after the plus fuction just passed the else statemnt and finally add the two coming value togather 


# # #10
# def a(b,c):
#     return b+c
#     return 10
# print(a(3,5))
# as we said previously the return break out the function go out of it 

#11
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
# print(b)
# a()
# print(b)
# print b it print the value despite of what inside the fuction 
# printing b again will after the function will not make any different
# printing a() will print the b and take the value of it from inside the function
# and finally it will do the same so what ever inside the function printin out side it will not be taken in considration


#12
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# a()
# print(b)
# there is no different with the previous example since the return is at the end of the function

#13
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=a()
# print(b)
#  evry thing is the same out put but when buting the variable = to a function it will ignore its first value and consider the fuction value 


#14
# def a():
#     print(1)
#     b()
#     print(2)
# def b():
#     print(3)
# a()

#  in this example when printin a it do the normal print and access the b function and activate it 

# #15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)

# the sequance is important when calling the function a it go throw line by line and even when it comes to b it run it and then went back to the main function





