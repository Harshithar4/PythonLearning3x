my_lst=[2,3,4,5,6]

def f1(lst):
    lst.append(100)
    return lst

#print(f1(my_lst))
l=f1(my_lst)
print(l)