#functions
print('a value') #prints the text
print(input('ask for a value')) #prints the text and a prompt, then prints the value given by the user
#function_name call the function with () then provite an 'argument' in the call to return a value
#methods -> functions of datatypes. always have to be attacthed to a value
print('value'.upper()) #prints the text in upercase
print('value'.lower()) #prints the text in lowercase
print('value'.replace('e', '3')) #prints the text but finds all instances of E and makes them 3

#new functions
print(abs(-1)) #makes the intager in the argument from a negitive to a positive
print(max(10,3)) #finds the biggest number in the argument
print(min(10,1)) #finds the smallest number in the argument
print(len('test')) #counts the letters in the argument

#pythagorus therum calcuator
A = int(input('What is your length of side A? ')) #asks user for what lenght 1 is, then converts the string to a #
B = int(input('What is your length of side B? ')) #asks user for lenhght 2, makes the output a # cause input is always a string
A_squared = A * A #the therum is a2 + b2 = c2 so we have to find a times a
B_squared = B * B #finds b times b
sum_of_squares = A_squared + B_squared #adds the result of the last 2 lines into one number repersented by a variable (cause its gona change)
print('The sum of the squares is:', sum_of_squares) #prints the result

#how the video said to do it
side_a = int(input('the width of the triangle'))
side_b = int(input('the height of the triangle'))
print(type(int(side_a))) #prints the type of the value strng or int after converting it int an int. 
print(type(int(side_b))) #it always starts from the most inside interger
hypotenuse = (side_a ** 2 + pow(side_b, 2)) ** (1/2) #a2 + b2 to the power of 1/2
print('the hypoto is: ', round(hypotenuse, 2))