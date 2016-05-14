#Returns the sum of num1 num2
def add(num1,num2):
	return num1 + num2
# *, -, /

def multiply(num1,num2):
	return num1 * num2
	
def minus(num1, num2):
	return num1 - num2
	
def divide(num1, num2):
	return num1 / num2
def main():
	operation = input("what do you want to do (+,-,/,*): ")
	if(operation != '+' and operation != '-' and operation != '*' and operation !='/'):
			#invalid operation
		print("ENter a valid operation")
	else:
		var1 = int(input("enter num1: "))
		var2 = int(input("enter num2: "))
		if(operation == '+'):
			print(add(var1, var2))
		elif(operation == '*'):
			print(multiply(var1, var2))
		elif(operation == '-'):
			print(minus(var1, var2))
		else: 
			print(divide(var1,var2))
main()