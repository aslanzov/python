str_command = input("Enter your task: ").replace(' ','')

sign_A = '' 
sign_B = ''

str_A = ''
str_B = ''

operation = '' 
i = 0

while i < len(str_command) :
    if str_command[i] == '+' or str_command[i] == '-' or str_command[i] == '*' or str_command[i] == '/' or str_command[i] == '^' :
        if str_A == '': 
            sign_A = str_command[i]
        elif operation != '':
            sign_B = str_command[i]
        else:
            operation = str_command[i]
    else:
        if operation == '':
            str_A += str_command[i]
        else:
            str_B += str_command[i]
    i += 1

A=float(sign_A + str_A)
B=float(sign_B + str_B)

result = None

if operation=='/' :
    if B == 0:
        result = "Division by 0 is not possible"
    else:
        result = A/B
elif operation=='*' : 
    result=A*B
elif operation=='-' : 
    result=A-B 
elif operation=='+' : 
    result=A+B
elif operation=='^' : 
    result=A**B
else : 
    result='Something went wrong'

print("Result: " + str(result))