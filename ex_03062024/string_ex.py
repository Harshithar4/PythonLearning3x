#How do you remove whitespace from the beginning or end of a string?
text="  Hello world   "
print(text.strip())#removes whitespace on both the side
text=" Hello, world  "
print(text.lstrip())#removes white space on the lft side of the string
text=" Hello, world  "
print(text.rstrip())