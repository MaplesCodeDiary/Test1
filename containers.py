#tuple = ("this", "is", "a", "variable", "with", "an", "array", "of data",) its immutable
#list = ["the", "same", "thing", "but needs [] and a tuple cant change"]
#set = {1,2,3, 'test'} every ently is unique, if there is any duplicates it will be removed
#dictonary = {has a key value pair: bob is the value, we can add more: this is the value}

#a_tuple = (1,2,3,'a string')
#a_list = [1,2,3, 3, 'a string']
#print(a_list)
#print(len(a_tuple))
#a_list.append('another word')
#print(a_list) you cant do this with tuple
#a_set = {1,2,3, 'a string'} #each value must be uniqe, if there is a 3 twice it will skip it
#print(set(a_list)) makes any container a set, in this case, a_list
#a_dictonary = {'key': 'value', 1: 2}
#print(a_dictonary[1])
#a_dictonary['new key'] = 1.5
#print(a_dictonary)

#how to get values from a container
#indexing, each item in a list has a number attached to it. you call the nummber 2 then you get the second item
#slicing is the same but you [1:6:10] and it yoiu will grab you those numbers from the index
#index startr from 0

#user_list = ('lisa', 'emily', 'john', 'jerry', 'jax')
#print(user_list[0:3:2]) #0 is starting point 3 is end point 2 is jump between. 3 prints the first 3 index including 0
test_list = [1,2,3,4,5,6,7,8,9,10]
print(test_list[7::-2])
