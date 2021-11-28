def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
  return num1 - num2

def multiplication(num1, num2):
  return num1 * num2

def division(num1, num2):
  return num1 / num2

def invalid(num1,num2):
    return "Invalid option"

operations = {
    'add': addition,
    'sub': subtraction,
    'mul': multiplication,
    'div': division
}
def switcher(choice):
   return operations.get(choice)(num1, num2)
# print('''you can perform opeartion
# 1.addition
# 2.subtraction
# 3.multiplication
# 4.division
# 5.module ''')
# choice= (input("select choice from (add,sub,mul,div): "))
# num1= int(input("enter first number: "))
# num2= int(input("enter second number: "))
# print(switcher(choice))

