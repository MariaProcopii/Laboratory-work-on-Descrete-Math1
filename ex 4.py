def decimalToBinary(num, requiredLength):
	binaryString = []
	while (num > 0):
		binaryString = binaryString + [num % 2]
		num = num // 2
	while (len(binaryString) < requiredLength):
		binaryString = binaryString + [0]
	return (binaryString)        # putem intoarce

def expression(possibleAlplhaValues, listOfValues):
	evalExpressionString = ""
	for x in range(0, len(inputStr)):
		if (inputStr[x] == "("):
			evalExpressionString = evalExpressionString + "("
		if (inputStr[x] == ")"):
			evalExpressionString = evalExpressionString + ") "
		if (inputStr[x] == "!"):
			evalExpressionString = evalExpressionString + "not "
		if (inputStr[x] == "+"):
			evalExpressionString = evalExpressionString + "or "
		if (inputStr[x] == "*"):
			evalExpressionString = evalExpressionString + "and "
		for i in range(0, len(possibleAlplhaValues)):
			if (inputStr[x] == possibleAlplhaValues[i]):
				evalExpressionString = evalExpressionString + str(listOfValues[i]) + " "
	return(evalExpressionString)


inputStr = input()
list = []

for i in inputStr:
	if (i.isalpha() == 1):#daca este litera
		if (i not in list):# daca nu e in lista - adauga
			list = list + [i]
			print(i, "|", end=" ")
print(inputStr)

for x in range(0, 2**len(list)):#iterarea valorilor 2^n
	currentValues = decimalToBinary(x, len(list))
	for i in range(0, len(list)):
		print(currentValues[i], "|", end=" ")
	expressionString = expression(list, currentValues)
	valueString = eval(expressionString)
	if (valueString == False):
		valueString = 0
	if (valueString == True):
		valueString = 1
	print(valueString)