# 1. TASK: print "Hello World"
print("hello world")
# 2. print "Hello Noelle!" with the name in a variable
name = "Yazan"
print( "hello", name)	# with a comma
print( "hello"+ name )	# with a +
# # 3. print "Hello 42!" with the number in a variable
name = 27
print( "hello" , name )	# with a comma
print( "hello" + str(name))	# with a +	-- this one should give us an error!
# # 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "shawirma"
fave_food2 = "msakhan"
print("i love {} and {}".format(fave_food1,fave_food2)) # with .format()
print( f"i love{fave_food1} and {fave_food2}" ) # with an f string