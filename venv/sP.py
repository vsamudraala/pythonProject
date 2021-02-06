# print("|    |  |--- | |\\  |  |  /  /--\\  -----")
# print("|    |  |----| | \\ |  |/   /    \\   |")
# print("\\   /   |      |  \\|  |\   |----|   |")
# print(" \\_/    |----  |   |  |  \ |    |   |")

print("CALCULATION BY getting user input :")
#num1=float(input("Enter 1st num"))
#num2=float(input("Enter 2nd num"))
#operation=input("select operation from below list ex: + , - , *, % ")
#add=num1+num2
#multiply=num1*num2
#print(add)

import sys
print("Getting python version using sys.version -- sys package" +sys.version[0])
if sys.version_info[0] < 3:
    raise Exception ("PYTHON VERSION IS  3.x")

import platform
print("Getting python version using python_version -- platfform package" +platform.python_version())


print("\"LIST\" can accept multiple data type entries in the same list ")
list=["index0","string at index 1", 12, 16, "randomStringValue"]
print(f'value at index 2 is: {list[2]}')
print(f'list[1:] function gets all the elements from the list staring from index 1: {list[1:]}')
print(f"list[-1] displays the last element in a list: Last entry in the cuttenty list is :  {list[-1]}")

####
# print("APPEND Function adds the element to the end of the list.")
# fruits = ["Apple", "Banana"]
# # print(f'Current Fruits List {fruits}')
# # f = input("Please enter a fruit name:\n")
# # fruits.append(f)
# # print(f'Updated Fruits List {fruits}')
# print("INSERT function adds an element at the given index of the list....")
# num_list = [1, 2, 3, 4, 5, 'NUMlIST']
# print(f'Current Numbers List {num_list}')
# num = (input("Please enter a number to add to list:\n"))
# index = int(input(f'Please enter the index between 0 and {len(num_list) - 1} to add the number:\n'))
# num_list.insert(index, num)
# print(f'Updated Numbers List {num_list}')
####

#an empty list
empty_list=[]
#a list of strings
str_list=['this', 'is', 'a', 'list']
#to remove a specific element, like 'is'
str_list.remove('is')
print(str_list)

#to remove an item of a specific index like 2
del str_list[2]
print(str_list)

bl=[0, '1', '2', 'list3']
print(bl)
del bl[2]
print(bl)

#there are yet another way to remove an item of a specific index
str_list.pop(0)
print(str_list)
##################
#TUPLES
#
#
print("TUPLE and List are Similar \n \"TUPLE\" is IMMUTABLE \n \"LIST\" is MUTABLE")
cood=(4,5,6)
print(f'{cood[2]}')
