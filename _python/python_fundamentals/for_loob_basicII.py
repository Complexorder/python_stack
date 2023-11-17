# def biggie(list):
#     for i in range(len(list)):
#         if list[i]>0:
#             list[i]="big"
#     return list 
# print(biggie([-1,5,3,-4]))


# def countPositve(list):
#     number=0
#     for i in range (len(list)):
#         if list[i]>0:
#             number+=1
#     list.append(number)
#     return(list)

# print(countPositve([1,2,-3,-4,-5]))

# def returnPositve(list):
#     sum=0
#     for i in range(len(list)):
#         sum = sum + list[i]
#     return(sum)

# print(returnPositve([1,2,-1,5]))


# def avg(list):
#     sum=0
#     avg = 0 
#     for i in range(len(list)):
#         sum = sum + list[i]
#     avg= sum/len(list)
#     return avg 

# print(avg([1,2,-1,5]))

# def  length(list):
#     if len(list)=="" :
#         return 0 
#     else :
#         return len(list)
    
# print(length([2,5,7,8]))
    
# def minimum(list):
#     min= list[0]
#     if len(list)=="" :
#         return False
#     else :
#         for i in range (len(list)):
#             if list[i]< min:
#                 min = list[i]
#     return min 
# print(minimum([1,3,-9,-10]))

# def maximum(list):
#     max= list[0]
#     if len(list)=="" :
#         return False
#     else :
#         for i in range (len(list)):
#             if list[i]> max:
#                 max = list[i]
#     return max
# print(maximum([1,3,-9,-10]))

# def ultimate_analysis(list):
#     if not list:
#         return None  # Return None for an empty list

#     result = {
#         'sumTotal': sum(list),
#         'average': sum(list) / len(list),
#         'minimum': min(list),
#         'maximum': max(list),
#         'length': len(list)
#     }

#     return result

# # Example usage:
# numbers = [37, 2, 1, -9]
# analysis_result = ultimate_analysis(numbers)
# print(analysis_result)

# def revers(list):
#     new_list = []
#     for i in range(len(list)-1,-1,-1):
#         new_list.append(list[i])
#     return new_list

# print(revers([-1,4,5,9]))






