str_command = input("Enter your task: ").replace(' ','')

operation_all = ('^', '*', '/', '+', '-')
str_A = ''
str_B = ''
variable = ['']
operation = []

for i, pos in enumerate(str_command):
	if pos in operation_all and i > 0 and variable[len(operation)] != '':
		operation.append(pos)
		variable.append('')
	else:
		position = len(operation)
		variable[position] += pos
        
variable = list(map(float, variable))
result = variable[0]

for i, oper in enumerate(operation): 
    if type (result) == str:
        break
    A=result
    B=variable[i+1]
    if oper=='/' :
        if B == 0:
            result = "Division by 0 is not possible"
        else:
            result = A/B
    elif oper=='*' : 
        result=A*B
    elif oper=='-' : 
        result=A-B 
    elif oper=='+' : 
        result=A+B
    elif oper=='^' : 
        result=A**B
    else : 
        result='Something went wrong'

print("Result: " + str(result))