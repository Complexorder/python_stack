import random
def randInt(min= ""  , max= ""  ):
    if min =="" and max =="" :
        random.random() * 100
    print(randInt(min="",max=""))
    # if max == 50:
    #     random.random() * 50


# If no arguments are provided, the function should return a random integer between 0 and 100.

# If only a max number is provided, the function should return a random integer between 0 and the max number.

# If only a min number is provided, the function should return a random integer between the min number and 100

# If both a min and max number are provided, the function should return a random integer between those 2 values.
 

   