# strings are immutable once a value has assigned we cannot change the content directly
name = "Ganishka"
# name[2] = "w"
# print(name)  # 'str' object does not support item assignment
print(name)
name = "Amit"
print(name)
# if we want to change the content
new_name = "w" + (name)[1:]
print(new_name)
