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
[{'opr' : '' , 'val': -2}, {}, ...]
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

result = None
error = False
#премся по строчке, карент -- текущее, парсим на операции и числа
#пока не понимаю, как работает алгоритм с отрицательными числами

#cur = ''
#i=0

for i, letter in enumerate(instr): 
    if letter in supported_ops and (i>0) and actions[-1]['val'] != '':
        #cur = ''
        #операции
        actions.append({'opr': letter, 'val': ''})
    
    elif letter in digital_chars:
        #cur+=letter
        #чиселки
        actions [-1]['val'] += letter
 

#print (actions)

#вычислить операции 1го приоритета (возведение в степень)
"""
на вход наш набор значений и операций
на выход обновленная ?структура данных? с операциями +- и значениями
2+3.5*2-3^2
2+3.5*2-9
"""

i = 0
actions.reverse()
while i < len(actions):
    do = actions[i]
    operation = do.get('opr')
    if operation in hp_ops:
        if operation == '^':
            cur_res = float(actions[i+1].get('val'))**float(do.get('val'))
            actions[i+1]['val'] = str(cur_res)
            del actions[i]
    else:
        i += 1
# pass
actions.reverse()



#вычислить операции 2го приоритета (умножение и деление)
"""
на вход наш набор значений и операций
на выход обновленная ?структура данных? с операциями +- и значениями
-2+3.5*2-9
2+7-9

сначала чекаем ошибку деления, если всё ок, то работаем дальше
"""

i = 0
while i < len(actions):
    do = actions[i]
    operation = do.get('opr')
    if operation in mp_ops:
        if float(do.get('val')) == 0 and operation == '/':
            result = 'inf'
            error = True
        else:
            eval_str = (actions[i-1].get('val') + operation + do.get('val'))
            cur_res = eval(eval_str)
            actions[i-1]['val'] = str(cur_res)
        actions.pop(i)
    else:
        i += 1

#вычислить операции 3го приоритета (сложение и вычитание)
""" 
Если выше все отработало, то выполняем +-
-2+7-9 = -4
"""
if not error:
    for do in actions:
       chislo_A = result
       chislo_B = do.get('val')
       operation = do.get('opr')
       if operation in lp_ops:
          result = str(eval(chislo_A + operation + chislo_B))
       else:
          result = chislo_B

#вывести результат
print("Result: " + str(result))