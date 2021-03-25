"""
хотим калькулятор выражений -2 +3.5 * 2 - 3 ^ 2
"""
#считать строчку от пользователя
instr = input ('Pleae, enter your task: ')

#почистить строку
# "-2 +3.5 * 2 - 3 ^ 2" -> "-2+3.5*2-3^2"
instr = instr.replace(' ', '')

#распарсить
"""
на вход строку
"-2+3.5*2-3^2"
на выход ?структура данных? с операциями +- и значениями
(+*-)
(-2 3.5 2 3 2)
[{'opr' :  , 'val': -2}, {}, ...]
"""

hp_ops = tuple('^')
mp_ops = tuple('*/')
lp_ops = tuple('+-')
supported_ops = hp_ops + mp_ops + lp_ops
#print (supported_ops)
digital_chars = tuple ('0123456789.-')

actions = list ()
d = dict()
d['opr']='First'
d['val']= ''
actions.append(d)
actions.append(d)

result = None

#премся по строчке, карент -- текущее, делим на операции и числа
#пока не понимаю, какой алгоритм с отрицательными числами
cur = ''
i=0
for i, letter in enumerate(instr): 
    if letter in supported_ops and (i>0) and cur!='': 
        actions[-1]['val'] = float (cur)
        cur = ''
        actions.append ({'opr': letter, 'val': ''})
    
    elif letter in digital_chars:
        cur+=letter
        actions [-1]['val'] += letter
 

print (actions)


#вычислить операции 1го приоритета (возведение в степень)
"""
на вход наш набор значений и операций
на выход обновленная ?структура данных? с операциями +- и значениями
2+3.5*2-3^2
2+3.5*2-9
"""


i = 0
while i < len(actions):
	do = actions[i]
	operation = do.get('opr')
	if operation == hp_ops[0]:
		actions[i+1]['val'] = actions[i+1].get('val') ** do.get('val')
		actions.remove(do)
	else:
		i += 1
   # pass



#вычислить операции 2го приоритета (умножение и деление)
"""
на вход наш набор значений и операций
на выход обновленная ?структура данных? с операциями +- и значениями
-2+3.5*2-9
2+7-9
"""

  

#вычислить операции 3го приоритета (сложение и вычитание)
# -2+7-9 = -4

#вывести результат
print("Result: " + str(result))