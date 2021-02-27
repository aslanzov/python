ishod = open('ishod.txt', 'r')
deliMOE = float(ishod.readline())
deliTEL = float(ishod.readline(2))
ishod.close()

result = deliMOE/deliTEL

resultat = open('resultat.txt', 'w')
resultat.write(str(result))