#simple div
str_input = input("Chislo A: ")
A = int(str_input)
#print(type(delimoe))
operation = input ("Operation (+ / * - ^): ")
str_input2 = input("Chislo B: ")
B = int(str_input2)
#print(type(delitel))
result = None

if operation == '/':
    result = A / B
elif operation == '+':
    result = A + B
elif operation == '*':
    result = A * B
elif operation == '^':
    result = A**B
else:
    result = "unknown"

#result = delimoe / delitel
#print(type(result))
print("Result: " + str(result))