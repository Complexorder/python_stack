
# def countDown(n):
#     list=[]
#     for x in range (n,-1,-1) :
#         list.append(x)
#     return list 
    

# print(countDown(5))

# def print_and_return(list) :
#     print(list[0])
#     return list[1]

# print(print_and_return([1,2]))


# def first_plus_length(list):
#     x=(list[0]+len(list))
#     return x
    
# print(first_plus_length([1,2,3,4,5]))


# arr=[]
# def greater_than_secound(arrayy):
#     if len(arrayy) < 2 :
#             return False
#     for x in range (0, len(arrayy) ,1):
#         if arrayy[x]> arrayy[1] and len(arrayy)>2:
#             arr.append(arrayy[x])
       
#     y= len(arr)
#     print(y)
#     return arr
# print(greater_than_secound([5,3,5,6,7]))


def length_and_value(size,value):
    list = []
    for i in range(size):
        list.append(value)
    return list
print(length_and_value(6,2))


