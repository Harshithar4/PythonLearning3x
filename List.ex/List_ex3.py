#How do you sort a list in ascending or descending order?
my_list=[4,67,89,13,0,56]
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)
#How do you reverse a list in Python?
my_list=[4,67,89,13,0,56]
my_list.reverse()
print(my_list)
#How do you check if an element is in a list?
my_list=[4,67,89,13,0,56]
new_list=90
if new_list in my_list:
    print(new_list)
else:
    print("Not found")