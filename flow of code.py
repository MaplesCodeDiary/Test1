#boolean value
#can only be true or false
#uses == < <= easiest way to create it is with conparison operators 

# this is the simpleist print(5 > 4) 
 
#if and else statements
#if 4 > 7:
#    print('correct result')

#elif 2 > 1:
#    print('im confused')
#    if len([1,2,3]) > 2:
#        print("list not long enough")

#elif 0 == 0:
#    print('im confused2')

#else:
#    print('incorect result')

#while loop
counter = 0
while counter <= 10:
    print(counter)
    counter += 1
    if counter == 5:
        print('counter is 5')
print('while loop is finished')

#for loop
#test_dictonary = {3: 1, 1: 2, 4: 3}
#test_list3 = [1,3,4,5,6]
#test_list = [1,2,3,4,5]
#for k,v in test_dictonary.items(): #can use keys() values() items()
#    print(k) #can change x to k and v

    #truthy and falsy, when a data type moves to boolean
    #in python every empty container, string withoult letters and 0 are auto faulse
    #everything else is trute

#truthy and falsy
if 1:    #empty = falsy, full = truthy
    print('truthy')
else:
    print('falsy')

#any() and all() return true or false, they want a container for an argument. if there are no values they are dead'


#prints each value, 2 is married to "is 2" anything not 2 is married to "not 2"
final_test = [1,2,3,4,5]
for x in final_test:
    print(x)
    if x == 2:
        print("the value is 2")
    else:  #this could be else for less code
        print("the value is not 2")
    loopcount = 0 #creates a variable outside of the while loop to cactch it from going for ever
    while x == 5: 
        print("last item") #we are printing last item 6 times here and once its over printing we done. each loop adds +1 and loopcount kills it once it hits 6
        loopcount += 1
        if loopcount == 6:
            print("we done")
            x = 0