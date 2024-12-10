#Create an empty list called my_list.
#Append the following elements to my_list: 10, 20, 30, 40.
#Insert the value 15 at the second position in the list.
#Extend my_list with another list: [50, 60, 70].
#Remove the last element from my_list.
#Sort my_list in ascending order.
#Find and print the index of the value 30 in my_list.

#creating an empty list
my_list = []
numbers = [50, 60, 70]
print(numbers)

#appending the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("After append:", my_list)

#Insert the value 15
my_list.insert(1, 15)
print("After insert:", my_list)

#Extending my_list with another list
my_list.extend(numbers)
print("List after Extend:", my_list)

#Removinng the last element
del my_list[-1]
print(my_list)

#Sort my_list in ascending order.
my_list.sort()
print(my_list)

#Find and print the index of the value 30
index_30 = my_list.index(30)
print("The index of 30 is:", index_30)