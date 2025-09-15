string = input("Enter a string: ")
stack = []
for char in string:
    stack.append(char)
reversed_string = ""
while stack:
    reversed_string += stack.pop()
print("Original string:", string)
print("Reversed string:", reversed_string)
