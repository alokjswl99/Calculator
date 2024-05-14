from art import logo
#from replit import clear


def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

operations={
        "+": add,
        "=": subtract,
        "*": multiply,
        "/": divide
 }


def calculator():
  print(logo)
  n1=float(input("Enter the first number:\n"))

  should_continue=True

  while should_continue:
    for i in operations:
      print(i)
      symbol=input("Enter the operation you want to perform:\n")
      n2=float(input("Enter the next number:\n"))
      calculation=operations[symbol]
      answer=calculation(n1,n2)
      print(f"{n1} {symbol} {n2} = {answer}")
      con=input(f"Type y to continue calculating with {answer}, or type n to start a new calculation: ")
      if con=='y':
          n1=answer
      else:
          should_continue=False
          #clear()
          calculator()

calculator()
