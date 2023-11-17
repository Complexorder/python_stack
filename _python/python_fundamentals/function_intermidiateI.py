import random
def randint(min=" ",max=" "):
    if  min ==" " and max==" ":
        x=random.random()*100
        return (round(x))


    elif  min =="":
        x=random.random()*max
        return (round(x))

    elif  max==" ":
        x=random.random()*(100-min)+min
        return (round(x))

    else:
        x=random.random()*(max-min)*min



